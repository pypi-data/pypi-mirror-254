"""
Adapted from AllenNLP
https://github.com/allenai/allennlp/blob/main/allennlp/predictors/predictor.py
"""

import json
import logging
import re
from contextlib import contextmanager
from typing import List, Iterator, Dict, Tuple, Any

import numpy
import pytorch_lightning as pl
import torch
from overrides import overrides
from torch import Tensor
from torch import backends
from torch.utils.hooks import RemovableHandle

from combo.common.util import sanitize
from combo.config import FromParameters
from combo.data.batch import Batch
from combo.data.dataset_readers.dataset_reader import DatasetReader
from combo.data.instance import JsonDict, Instance
from combo.modules.model import Model
from combo.nn import utils
from combo.nn.utils import move_to_device

logger = logging.getLogger(__name__)


class PredictorModule(pl.LightningModule, FromParameters):
    """
    a `Predictor` is a thin wrapper around an AllenNLP model that handles JSON -> JSON predictions
    that can be used for serving models through the web API or making predictions in bulk.
    """

    def __init__(self, model: Model, dataset_reader: DatasetReader, frozen: bool = True) -> None:
        super().__init__()
        if frozen:
            model.eval()
        self._model = model
        self.dataset_reader = dataset_reader
        self.cuda_device = next(self._model.named_parameters())[1].get_device()
        self._token_offsets: List[Tensor] = []

    def forward(self, inputs: Instance) -> Dict[str, torch.Tensor]:
        r"""
        Same as :meth:`torch.nn.Module.forward`.

        Args:
            *args: Whatever you decide to pass into the forward method.
            **kwargs: Keyword arguments are also possible.

        Return:
            Your model's output
        """
        return self._model.forward(inputs)

    @overrides(check_signature=False)
    def training_step(self, *args: Any, **kwargs: Any) -> Dict[str, torch.Tensor]:
        raise NotImplementedError()

    @overrides(check_signature=False)
    def configure_optimizers(self) -> Any:
        raise NotImplementedError()


    def load_line(self, line: str) -> JsonDict:
        """
        If your inputs are not in JSON-lines format (e.g. you have a CSV)
        you can override this function to parse them correctly.
        """
        return json.loads(line)

    def dump_line(self, outputs: Any) -> Any:
        """
        If you don't want your outputs in JSON-lines format
        you can override this function to output them differently.
        """
        return json.dumps(outputs) + "\n"

    def predict_json(self, inputs: JsonDict) -> Any:
        instance = self._json_to_instance(inputs)
        return self.predict_instance(instance)

    def json_to_labeled_instances(self, inputs: JsonDict) -> List[Instance]:
        """
        Converts incoming json to a [`Instance`](../data/instance.md),
        runs the model on the newly created instance, and adds labels to the
        `Instance`s given by the model's output.

        # Returns

        `List[instance]`
            A list of `Instance`'s.
        """

        instance = self._json_to_instance(inputs)
        outputs = self._model.forward_on_instance(instance)
        new_instances = self.predictions_to_labeled_instances(instance, outputs)
        return new_instances

    def get_gradients(self, instances: List[Instance]) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        """
        Gets the gradients of the loss with respect to the model inputs.

        # Parameters

        instances : `List[Instance]`

        # Returns

        `Tuple[Dict[str, Any], Dict[str, Any]]`
            The first item is a Dict of gradient entries for each input.
            The keys have the form  `{grad_input_1: ..., grad_input_2: ... }`
            up to the number of inputs given. The second item is the model's output.

        # Notes

        Takes a `JsonDict` representing the inputs of the model and converts
        them to [`Instances`](../data/instance.md)), sends these through
        the model [`forward`](../models/model.md#forward) function after registering hooks on the embedding
        layer of the model. Calls `backward` on the loss and then removes the
        hooks.
        """
        # set requires_grad to true for all parameters, but save original values to
        # restore them later
        original_param_name_to_requires_grad_dict = {}
        for param_name, param in self._model.named_parameters():
            original_param_name_to_requires_grad_dict[param_name] = param.requires_grad
            param.requires_grad = True

        embedding_gradients: List[Tensor] = []
        hooks: List[RemovableHandle] = self._register_embedding_gradient_hooks(embedding_gradients)

        dataset = Batch(instances)
        dataset.index_instances(self._model.vocab)
        dataset_tensor_dict = move_to_device(dataset.as_tensor_dict(), self.cuda_device)
        # To bypass "RuntimeError: cudnn RNN backward can only be called in training mode"
        with backends.cudnn.flags(enabled=False):
            outputs = self._model.make_output_human_readable(
                self._model.forward(**dataset_tensor_dict)  # type: ignore
            )

            loss = outputs["loss"]
            # Zero gradients.
            # NOTE: this is actually more efficient than calling `self._model.zero_grad()`
            # because it avoids a read op when the gradients are first updated below.
            for p in self._model.parameters():
                p.grad = None
            loss.backward()

        for hook in hooks:
            hook.remove()

        grad_dict = dict()
        for idx, grad in enumerate(embedding_gradients):
            key = "grad_input_" + str(idx + 1)
            grad_dict[key] = grad.detach().cpu().numpy()

        # restore the original requires_grad values of the parameters
        for param_name, param in self._model.named_parameters():
            param.requires_grad = original_param_name_to_requires_grad_dict[param_name]

        return grad_dict, outputs

    def get_interpretable_layer(self) -> torch.nn.Module:
        """
        Returns the input/embedding layer of the model.
        If the predictor wraps around a non-AllenNLP model,
        this function should be overridden to specify the correct input/embedding layer.
        For the cases where the input layer _is_ an embedding layer, this should be the
        layer 0 of the embedder.
        """
        try:
            return utils.find_embedding_layer(self._model)
        except RuntimeError:
            raise RuntimeError(
                "If the model does not use `TextFieldEmbedder`, please override "
                "`get_interpretable_layer` in your predictor to specify the embedding layer."
            )

    def get_interpretable_text_field_embedder(self) -> torch.nn.Module:
        """
        Returns the first `TextFieldEmbedder` of the model.
        If the predictor wraps around a non-AllenNLP model,
        this function should be overridden to specify the correct embedder.
        """
        try:
            return utils.find_text_field_embedder(self._model)
        except RuntimeError:
            raise RuntimeError(
                "If the model does not use `TextFieldEmbedder`, please override "
                "`get_interpretable_text_field_embedder` in your predictor to specify "
                "the embedding layer."
            )

    def _register_embedding_gradient_hooks(self, embedding_gradients):
        """
        Registers a backward hook on the embedding layer of the model.  Used to save the gradients
        of the embeddings for use in get_gradients()

        When there are multiple inputs (e.g., a passage and question), the hook
        will be called multiple times. We append all the embeddings gradients
        to a list.

        We additionally add a hook on the _forward_ pass of the model's `TextFieldEmbedder` to save
        token offsets, if there are any.  Having token offsets means that you're using a mismatched
        token indexer, so we need to aggregate the gradients across wordpieces in a token.  We do
        that with a simple sum.
        """

        def hook_layers(module, grad_in, grad_out):
            grads = grad_out[0]
            if self._token_offsets:
                # If you have a mismatched indexer with multiple TextFields, it's quite possible
                # that the order we deal with the gradients is wrong.  We'll just take items from
                # the list one at a time, and try to aggregate the gradients.  If we got the order
                # wrong, we should crash, so you'll know about it.  If you get an error because of
                # that, open an issue on github, and we'll see what we can do.  The intersection of
                # multiple TextFields and mismatched indexers is pretty small (currently empty, that
                # I know of), so we'll ignore this corner case until it's needed.
                offsets = self._token_offsets.pop(0)
                span_grads, span_mask = utils.batched_span_select(grads.contiguous(), offsets)
                span_mask = span_mask.unsqueeze(-1)
                span_grads *= span_mask  # zero out paddings

                span_grads_sum = span_grads.sum(2)
                span_grads_len = span_mask.sum(2)
                # Shape: (batch_size, num_orig_tokens, embedding_size)
                grads = span_grads_sum / torch.clamp_min(span_grads_len, 1)

                # All the places where the span length is zero, write in zeros.
                grads[(span_grads_len == 0).expand(grads.shape)] = 0

            embedding_gradients.append(grads)

        def get_token_offsets(module, inputs, outputs):
            offsets = utils.get_token_offsets_from_text_field_inputs(inputs)
            if offsets is not None:
                self._token_offsets.append(offsets)

        hooks = []
        text_field_embedder = self.get_interpretable_text_field_embedder()
        hooks.append(text_field_embedder.register_forward_hook(get_token_offsets))
        embedding_layer = self.get_interpretable_layer()
        hooks.append(embedding_layer.register_backward_hook(hook_layers))
        return hooks

    @contextmanager
    def capture_model_internals(self, module_regex: str = ".*") -> Iterator[dict]:
        """
        Context manager that captures the internal-module outputs of
        this predictor's model. The idea is that you could use it as follows:

        ```
            with predictor.capture_model_internals() as internals:
                outputs = predictor.predict_json(inputs)

            return {**outputs, "model_internals": internals}
        ```
        """
        results = {}
        hooks = []

        # First we'll register hooks to add the outputs of each module to the results dict.
        def add_output(idx: int):
            def _add_output(mod, _, outputs):
                results[idx] = {"name": str(mod), "output": sanitize(outputs)}

            return _add_output

        regex = re.compile(module_regex)
        for idx, (name, module) in enumerate(self._model.named_modules()):
            if regex.fullmatch(name) and module != self._model:
                hook = module.register_forward_hook(add_output(idx))
                hooks.append(hook)

        # If you capture the return value of the context manager, you get the results dict.
        yield results

        # And then when you exit the context we remove all the hooks.
        for hook in hooks:
            hook.remove()

    def predict_instance(self, instance: Instance) -> Any:
        outputs = self._model.forward_on_instance(instance)
        return sanitize(outputs)

    def predictions_to_labeled_instances(
        self, instance: Instance, outputs: Dict[str, numpy.ndarray]
    ) -> List[Instance]:
        """
        This function takes a model's outputs for an Instance, and it labels that instance according
        to the output. For example, in classification this function labels the instance according
        to the class with the highest probability. This function is used to to compute gradients
        of what the model predicted. The return type is a list because in some tasks there are
        multiple predictions in the output (e.g., in NER a model predicts multiple spans). In this
        case, each instance in the returned list of Instances contains an individual
        entity prediction as the label.
        """

        raise RuntimeError("implement this method for model interpretations or attacks")

    def _json_to_instance(self, json_dict: JsonDict) -> Instance:
        """
        Converts a JSON object into an [`Instance`](../data/instance.md)
        and a `JsonDict` of information which the `Predictor` should pass through,
        such as tokenised inputs.
        """
        raise NotImplementedError

    def predict_batch_json(self, inputs: List[JsonDict]) -> List[Any]:
        instances = self._batch_json_to_instances(inputs)
        return self.predict_batch_instance(instances)

    def predict_batch_instance(self, instances: List[Instance]) -> List[Any]:
        outputs = self._model.forward_on_instances(instances)
        return sanitize(outputs)

    def _batch_json_to_instances(self, json_dicts: List[JsonDict]) -> List[Instance]:
        """
        Converts a list of JSON objects into a list of `Instance`s.
        By default, this expects that a "batch" consists of a list of JSON blobs which would
        individually be predicted by `predict_json`. In order to use this method for
        batch prediction, `_json_to_instance` should be implemented by the subclass, or
        if the instances have some dependency on each other, this method should be overridden
        directly.
        """
        instances = []
        for json_dict in json_dicts:
            instances.append(self._json_to_instance(json_dict))
        return instances
