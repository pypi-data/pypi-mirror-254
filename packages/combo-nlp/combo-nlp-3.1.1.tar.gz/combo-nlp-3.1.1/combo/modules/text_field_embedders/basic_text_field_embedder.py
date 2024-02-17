"""
Adapted from AllenNLP
https://github.com/allenai/allennlp/blob/main/allennlp/modules/text_field_embedders/basic_text_field_embedder.py
"""
from typing import Dict
import inspect

import torch

from combo.common.params import Params
from combo.config import Registry
from combo.config.from_parameters import register_arguments, resolve
from combo.data.fields.text_field import TextFieldTensors
from combo.modules.text_field_embedders.text_field_embedder import TextFieldEmbedder
from combo.modules.token_embedders import EmptyEmbedder
from combo.modules.token_embedders.token_embedder import TokenEmbedder
from combo.utils import ConfigurationError
from combo.models.time_distributed import TimeDistributed


@Registry.register("base_text_field_embedder")
class BasicTextFieldEmbedder(TextFieldEmbedder):
    """
    This is a `TextFieldEmbedder` that wraps a collection of
    [`TokenEmbedder`](../token_embedders/token_embedder.md) objects.  Each
    `TokenEmbedder` embeds or encodes the representation output from one
    [`allennlp.data.TokenIndexer`](../../data/token_indexers/token_indexer.md). As the data produced by a
    [`allennlp.data.fields.TextField`](../../data/fields/text_field.md) is a dictionary mapping names to these
    representations, we take `TokenEmbedders` with corresponding names.  Each `TokenEmbedders`
    embeds its input, and the result is concatenated in an arbitrary (but consistent) order.

    Registered as a `TextFieldEmbedder` with name "basic", which is also the default.

    # Parameters

    token_embedders : `Dict[str, TokenEmbedder]`, required.
        A dictionary mapping token embedder names to implementations.
        These names should match the corresponding indexer used to generate
        the tensor passed to the TokenEmbedder.
    """

    @register_arguments
    def __init__(self, token_embedders: Dict[str, TokenEmbedder]) -> None:
        super().__init__()
        # NOTE(mattg): I'd prefer to just use ModuleDict(token_embedders) here, but that changes
        # weight locations in torch state dictionaries and invalidates all prior models, just for a
        # cosmetic change in the code.
        self._token_embedders = token_embedders
        for key, embedder in token_embedders.items():
            name = "token_embedder_%s" % key
            if isinstance(embedder, Params):
                embedder_params = dict(embedder)
                embedder = resolve(embedder_params)
            self.add_module(name, embedder)
        self._ordered_embedder_keys = sorted(self._token_embedders.keys())

    def get_output_dim(self) -> int:
        output_dim = 0
        for embedder in self._token_embedders.values():
            output_dim += embedder.get_output_dim()
        return output_dim

    def forward(
        self, text_field_input: TextFieldTensors, num_wrapping_dims: int = 0, **kwargs
    ) -> torch.Tensor:
        if sorted(self._token_embedders.keys()) != sorted(text_field_input.keys()):
            message = "Mismatched token keys: %s and %s" % (
                str(self._token_embedders.keys()),
                str(text_field_input.keys()),
            )
            embedder_keys = set(self._token_embedders.keys())
            input_keys = set(text_field_input.keys())
            if embedder_keys > input_keys and all(
                isinstance(embedder, EmptyEmbedder)
                for name, embedder in self._token_embedders.items()
                if name in embedder_keys - input_keys
            ):
                # Allow extra embedders that are only in the token embedders (but not input) and are empty to pass
                # config check
                pass
            else:
                raise ConfigurationError(message)

        embedded_representations = []
        for key in self._ordered_embedder_keys:
            # Note: need to use getattr here so that the pytorch voodoo
            # with submodules works with multiple GPUs.
            embedder = getattr(self, "token_embedder_{}".format(key))
            if isinstance(embedder, EmptyEmbedder):
                # Skip empty embedders
                continue
            forward_params = inspect.signature(embedder.forward).parameters
            forward_params_values = {}
            missing_tensor_args = set()
            for param in forward_params.keys():
                if param in kwargs:
                    forward_params_values[param] = kwargs[param]
                else:
                    missing_tensor_args.add(param)

            for _ in range(num_wrapping_dims):
                embedder = TimeDistributed(embedder)

            tensors: Dict[str, torch.Tensor] = text_field_input[key]
            if len(tensors) == 1 and len(missing_tensor_args) == 1:
                # If there's only one tensor argument to the embedder, and we just have one tensor to
                # embed, we can just pass in that tensor, without requiring a name match.
                token_vectors = embedder(list(tensors.values())[0], **forward_params_values)
            else:
                # If there are multiple tensor arguments, we have to require matching names from the
                # TokenIndexer.  I don't think there's an easy way around that.
                token_vectors = embedder(**tensors, **forward_params_values)
            if token_vectors is not None:
                # To handle some very rare use cases, we allow the return value of the embedder to
                # be None; we just skip it in that case.
                embedded_representations.append(token_vectors)
        return torch.cat(embedded_representations, dim=-1)
