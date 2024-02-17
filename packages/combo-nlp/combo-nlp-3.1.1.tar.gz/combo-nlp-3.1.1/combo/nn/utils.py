"""
Adapted from AllenNLP
https://github.com/allenai/allennlp/blob/80fb6061e568cb9d6ab5d45b661e86eb61b92c82/allennlp/nn/util.py
"""
from typing import Union, Dict, Optional, List, Any, NamedTuple

import torch

from combo.common.util import int_to_device
from combo.utils import ConfigurationError
import torch.nn.functional as F

StateDictType = Union[Dict[str, torch.Tensor], "OrderedDict[str, torch.Tensor]"]

def masked_cross_entropy(pred: torch.Tensor, true: torch.Tensor, mask: torch.BoolTensor) -> torch.Tensor:
    pred = pred + (mask.float().unsqueeze(-1) + 1e-45).log()
    return F.cross_entropy(pred, true, reduction="none") * mask

def tiny_value_of_dtype(dtype: torch.dtype):
    """
    Returns a moderately tiny value for a given PyTorch data type that is used to avoid numerical
    issues such as division by zero.
    This is different from `info_value_of_dtype(dtype).tiny` because it causes some NaN bugs.
    Only supports floating point dtypes.
    """
    if not dtype.is_floating_point:
        raise TypeError("Only supports floating point dtypes.")
    if dtype == torch.float or dtype == torch.double:
        return 1e-13
    elif dtype == torch.half:
        return 1e-4
    else:
        raise TypeError("Does not support dtype " + str(dtype))


def get_device_of(tensor: torch.Tensor) -> int:
    """
    Returns the device of the tensor.
    """
    if not tensor.is_cuda:
        return -1
    else:
        return tensor.get_device()


def combine_initial_dims(tensor: torch.Tensor) -> torch.Tensor:
    """
    Given a (possibly higher order) tensor of ids with shape
    (d1, ..., dn, sequence_length)
    Return a view that's (d1 * ... * dn, sequence_length).
    If original tensor is 1-d or 2-d, return it as is.
    """
    if tensor.dim() <= 2:
        return tensor
    else:
        return tensor.view(-1, tensor.size(-1))


def uncombine_initial_dims(tensor: torch.Tensor, original_size: torch.Size) -> torch.Tensor:
    """
    Given a tensor of embeddings with shape
    (d1 * ... * dn, sequence_length, embedding_dim)
    and the original shape
    (d1, ..., dn, sequence_length),
    return the reshaped tensor of embeddings with shape
    (d1, ..., dn, sequence_length, embedding_dim).
    If original size is 1-d or 2-d, return it as is.
    """
    if len(original_size) <= 2:
        return tensor
    else:
        view_args = list(original_size) + [tensor.size(-1)]
        return tensor.view(*view_args)


def get_range_vector(size: int, device: int) -> torch.Tensor:
    """
    Returns a range vector with the desired size, starting at 0. The CUDA implementation
    is meant to avoid copy data from CPU to GPU.
    """
    if device > -1:
        return torch.cuda.LongTensor(size, device=device).fill_(1).cumsum(0) - 1
    else:
        return torch.arange(0, size, dtype=torch.long)


def flatten_and_batch_shift_indices(indices: torch.Tensor, sequence_length: int) -> torch.Tensor:
    if torch.max(indices) >= sequence_length or torch.min(indices) < 0:
        raise ConfigurationError(
            f"All elements in indices should be in range (0, {sequence_length - 1})"
        )
    offsets = get_range_vector(indices.size(0), get_device_of(indices)) * sequence_length
    for _ in range(len(indices.size()) - 1):
        offsets = offsets.unsqueeze(1)

    # Shape: (batch_size, d_1, ..., d_n)
    offset_indices = indices + offsets

    # Shape: (batch_size * d_1 * ... * d_n)
    offset_indices = offset_indices.view(-1)
    return offset_indices


def batched_index_select(
        target: torch.Tensor,
        indices: torch.LongTensor,
        flattened_indices: Optional[torch.LongTensor] = None,
) -> torch.Tensor:
    if flattened_indices is None:
        # Shape: (batch_size * d_1 * ... * d_n)
        flattened_indices = flatten_and_batch_shift_indices(indices, target.size(1))

        # Shape: (batch_size * sequence_length, embedding_size)
    flattened_target = target.view(-1, target.size(-1))

    # Shape: (batch_size * d_1 * ... * d_n, embedding_size)
    flattened_selected = flattened_target.index_select(0, flattened_indices)
    selected_shape = list(indices.size()) + [target.size(-1)]
    # Shape: (batch_size, d_1, ..., d_n, embedding_size)
    selected_targets = flattened_selected.view(*selected_shape)
    return selected_targets


def move_to_device(obj, device: Union[torch.device, int]):
    """
    Given a structure (possibly) containing Tensors,
    move all the Tensors to the specified device (or do nothing, if they are already on
    the target device).
    """
    device = int_to_device(device)

    if isinstance(obj, torch.Tensor):
        # You may be wondering why we don't just always call `obj.to(device)` since that would
        # be a no-op anyway if `obj` is already on `device`. Well that works fine except
        # when PyTorch is not compiled with CUDA support, in which case even calling
        # `obj.to(torch.device("cpu"))` would result in an error.
        return obj if obj.device == device else obj.to(device=device)
    elif isinstance(obj, dict):
        for key, value in obj.items():
            obj[key] = move_to_device(value, device)
        return obj
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            obj[i] = move_to_device(item, device)
        return obj
    elif isinstance(obj, tuple) and hasattr(obj, "_fields"):
        # This is the best way to detect a NamedTuple, it turns out.
        return obj.__class__(*(move_to_device(item, device) for item in obj))
    elif isinstance(obj, tuple):
        return tuple(move_to_device(item, device) for item in obj)
    else:
        return obj


def device_mapping(cuda_device: int):
    """
    In order to `torch.load()` a GPU-trained model onto a CPU (or specific GPU),
    you have to supply a `map_location` function. Call this with
    the desired `cuda_device` to get the function that `torch.load()` needs.
    """

    def inner_device_mapping(storage: torch.Storage, location) -> torch.Storage:
        if cuda_device >= 0:
            return storage.cuda(cuda_device)
        else:
            return storage

    return inner_device_mapping


def find_text_field_embedder(model: torch.nn.Module) -> torch.nn.Module:
    """
    Takes a `Model` and returns the `Module` that is a `TextFieldEmbedder`.  We return just the
    first one, as it's very rare to have more than one.  If there isn't a `TextFieldEmbedder` in the
    given `Model`, we raise a `ValueError`.
    """
    from combo.modules.text_field_embedders.text_field_embedder import TextFieldEmbedder

    for module in model.modules():
        if isinstance(module, TextFieldEmbedder):
            return module
    raise ValueError("Couldn't find TextFieldEmbedder!")


def get_lengths_from_binary_sequence_mask(mask: torch.BoolTensor) -> torch.LongTensor:
    """
    Compute sequence lengths for each batch element in a tensor using a
    binary mask.
    # Parameters
    mask : `torch.BoolTensor`, required.
        A 2D binary mask of shape (batch_size, sequence_length) to
        calculate the per-batch sequence lengths from.
    # Returns
    `torch.LongTensor`
        A torch.LongTensor of shape (batch_size,) representing the lengths
        of the sequences in the batch.
    """
    return mask.sum(-1)


def sort_batch_by_length(tensor: torch.Tensor, sequence_lengths: torch.Tensor):
    """
    Sort a batch first tensor by some specified lengths.
    # Parameters
    tensor : `torch.FloatTensor`, required.
        A batch first Pytorch tensor.
    sequence_lengths : `torch.LongTensor`, required.
        A tensor representing the lengths of some dimension of the tensor which
        we want to sort by.
    # Returns
    sorted_tensor : `torch.FloatTensor`
        The original tensor sorted along the batch dimension with respect to sequence_lengths.
    sorted_sequence_lengths : `torch.LongTensor`
        The original sequence_lengths sorted by decreasing size.
    restoration_indices : `torch.LongTensor`
        Indices into the sorted_tensor such that
        `sorted_tensor.index_select(0, restoration_indices) == original_tensor`
    permutation_index : `torch.LongTensor`
        The indices used to sort the tensor. This is useful if you want to sort many
        tensors using the same ordering.
    """

    if not isinstance(tensor, torch.Tensor) or not isinstance(sequence_lengths, torch.Tensor):
        raise ConfigurationError("Both the tensor and sequence lengths must be torch.Tensors.")

    sorted_sequence_lengths, permutation_index = sequence_lengths.sort(0, descending=True)
    sorted_tensor = tensor.index_select(0, permutation_index)

    index_range = torch.arange(0, len(sequence_lengths), device=sequence_lengths.device)
    # This is the equivalent of zipping with index, sorting by the original
    # sequence lengths and returning the now sorted indices.
    _, reverse_mapping = permutation_index.sort(0, descending=False)
    restoration_indices = index_range.index_select(0, reverse_mapping)
    return sorted_tensor, sorted_sequence_lengths, restoration_indices, permutation_index


def get_text_field_mask(
        text_field_tensors: Dict[str, Dict[str, torch.Tensor]],
        num_wrapping_dims: int = 0,
        padding_id: int = 0,
) -> torch.BoolTensor:
    """
    Takes the dictionary of tensors produced by a `TextField` and returns a mask
    with 0 where the tokens are padding, and 1 otherwise. `padding_id` specifies the idx of padding tokens.
    We also handle `TextFields` wrapped by an arbitrary number of `ListFields`, where the number of wrapping
    `ListFields` is given by `num_wrapping_dims`.
    If `num_wrapping_dims == 0`, the returned mask has shape `(batch_size, num_tokens)`.
    If `num_wrapping_dims > 0` then the returned mask has `num_wrapping_dims` extra
    dimensions, so the shape will be `(batch_size, ..., num_tokens)`.
    There could be several entries in the tensor dictionary with different shapes (e.g., one for
    word ids, one for character ids).  In order to get a token mask, we use the tensor in
    the dictionary with the lowest number of dimensions.  After subtracting `num_wrapping_dims`,
    if this tensor has two dimensions we assume it has shape `(batch_size, ..., num_tokens)`,
    and use it for the mask.  If instead it has three dimensions, we assume it has shape
    `(batch_size, ..., num_tokens, num_features)`, and sum over the last dimension to produce
    the mask.  Most frequently this will be a character idx tensor, but it could also be a
    featurized representation of each token, etc.
    If the input `text_field_tensors` contains the "mask" key, this is returned instead of inferring the mask.
    """
    masks = []
    for indexer_name, indexer_tensors in text_field_tensors.items():
        if "mask" in indexer_tensors:
            masks.append(indexer_tensors["mask"].bool())
    if len(masks) == 1:
        return masks[0]
    elif len(masks) > 1:
        # TODO(mattg): My guess is this will basically never happen, so I'm not writing logic to
        # handle it.  Should be straightforward to handle, though.  If you see this error in
        # practice, open an issue on github.
        raise ValueError("found two mask outputs; not sure which to use!")

    tensor_dims = [
        (tensor.dim(), tensor)
        for indexer_output in text_field_tensors.values()
        for tensor in indexer_output.values()
    ]
    tensor_dims.sort(key=lambda x: x[0])

    smallest_dim = tensor_dims[0][0] - num_wrapping_dims
    if smallest_dim == 2:
        token_tensor = tensor_dims[0][1]
        return token_tensor != padding_id
    elif smallest_dim == 3:
        character_tensor = tensor_dims[0][1]
        return (character_tensor != padding_id).any(dim=-1)
    else:
        raise ValueError("Expected a tensor with dimension 2 or 3, found {}".format(smallest_dim))


def get_dropout_mask(dropout_probability: float, tensor_for_masking: torch.Tensor):
    """
    Computes and returns an element-wise dropout mask for a given tensor, where
    each element in the mask is dropped out with probability dropout_probability.
    Note that the mask is NOT applied to the tensor - the tensor is passed to retain
    the correct CUDA tensor type for the mask.
    # Parameters
    dropout_probability : `float`, required.
        Probability of dropping a dimension of the input.
    tensor_for_masking : `torch.Tensor`, required.
    # Returns
    `torch.FloatTensor`
        A torch.FloatTensor consisting of the binary mask scaled by 1/ (1 - dropout_probability).
        This scaling ensures expected values and variances of the output of applying this mask
        and the original tensor are the same.
    """
    binary_mask = (torch.rand(tensor_for_masking.size()) > dropout_probability).to(
        tensor_for_masking.device
    )
    # Scale mask by 1/keep_prob to preserve output statistics.
    dropout_mask = binary_mask.float().div(1.0 - dropout_probability)
    return dropout_mask


def find_embedding_layer(model: torch.nn.Module) -> torch.nn.Module:
    """
    Takes a model (typically an AllenNLP `Model`, but this works for any `torch.nn.Module`) and
    makes a best guess about which module is the embedding layer.  For typical AllenNLP models,
    this often is the `TextFieldEmbedder`, but if you're using a pre-trained contextualizer, we
    really want layer 0 of that contextualizer, not the output.  So there are a bunch of hacks in
    here for specific pre-trained contextualizers.
    """
    # We'll look for a few special cases in a first pass, then fall back to just finding a
    # TextFieldEmbedder in a second pass if we didn't find a special case.
    from transformers.models.gpt2.modeling_gpt2 import GPT2Model
    from transformers.models.bert.modeling_bert import BertEmbeddings
    from transformers.models.albert.modeling_albert import AlbertEmbeddings
    from transformers.models.roberta.modeling_roberta import RobertaEmbeddings

    for module in model.modules():
        if isinstance(module, BertEmbeddings):
            return module.word_embeddings
        if isinstance(module, RobertaEmbeddings):
            return module.word_embeddings
        if isinstance(module, AlbertEmbeddings):
            return module.word_embeddings
        if isinstance(module, GPT2Model):
            return module.wte

    return None

    # for module in model.modules():
    #     if isinstance(module, TextFieldEmbedder):
    #
    #         if isinstance(module, BasicTextFieldEmbedder):
    #             # We'll have a check for single Embedding cases, because we can be more efficient
    #             # in cases like this.  If this check fails, then for something like hotflip we need
    #             # to actually run the text field embedder and construct a vector for each token.
    #             if len(module._token_embedders) == 1:
    #                 embedder = list(module._token_embedders.values())[0]
    #                 if isinstance(embedder, Embedding):
    #                     if embedder._projection is None:
    #                         # If there's a projection inside the Embedding, then we need to return
    #                         # the whole TextFieldEmbedder, because there's more computation that
    #                         # needs to be done than just multiply by an embedding matrix.
    #                         return embedder
    #         return module
    raise RuntimeError("No embedding module found!")


def get_token_offsets_from_text_field_inputs(
        text_field_inputs: List[Any],
) -> Optional[torch.Tensor]:
    """
    Given a list of inputs to a TextFieldEmbedder, tries to find token offsets from those inputs, if
    there are any.  You will have token offsets if you are using a mismatched token embedder; if
    you're not, the return value from this function should be None.  This function is intended to be
    called from a `forward_hook` attached to a `TextFieldEmbedder`, so the inputs are formatted just
    as a list.
    It's possible in theory that you could have multiple offsets as inputs to a single call to a
    `TextFieldEmbedder`, but that's an extremely rare use case (I can't really imagine anyone
    wanting to do that).  In that case, we'll only return the first one.  If you need different
    behavior for your model, open an issue on github describing what you're doing.
    """
    for input_index, text_field_input in enumerate(text_field_inputs):
        if not isinstance(text_field_input, dict):
            continue
        for input_value in text_field_input.values():
            if not isinstance(input_value, dict):
                continue
            for embedder_arg_name, embedder_arg_value in input_value.items():
                if embedder_arg_name == "offsets":
                    return embedder_arg_value
    return None


def _check_incompatible_keys(
        module, missing_keys: List[str], unexpected_keys: List[str], strict: bool
):
    error_msgs: List[str] = []
    if missing_keys:
        error_msgs.append(
            "Missing key(s) in state_dict: {}".format(", ".join(f'"{k}"' for k in missing_keys))
        )
    if unexpected_keys:
        error_msgs.append(
            "Unexpected key(s) in state_dict: {}".format(
                ", ".join(f'"{k}"' for k in unexpected_keys)
            )
        )
    if error_msgs and strict:
        raise RuntimeError(
            "Error(s) in loading state_dict for {}:\n\t{}".format(
                module.__class__.__name__, "\n\t".join(error_msgs)
            )
        )


class _IncompatibleKeys(NamedTuple):
    missing_keys: List[str]
    unexpected_keys: List[str]

    def __repr__(self):
        if not self.missing_keys and not self.unexpected_keys:
            return "<All keys matched successfully>"
        return f"(missing_keys = {self.missing_keys}, unexpected_keys = {self.unexpected_keys})"


def batched_span_select(target: torch.Tensor, spans: torch.LongTensor) -> torch.Tensor:
    """
    The given `spans` of size `(batch_size, num_spans, 2)` indexes into the sequence
    dimension (dimension 2) of the target, which has size `(batch_size, sequence_length,
    embedding_size)`.

    This function returns segmented spans in the target with respect to the provided span indices.

    # Parameters

    target : `torch.Tensor`, required.
        A 3 dimensional tensor of shape (batch_size, sequence_length, embedding_size).
        This is the tensor to be indexed.
    indices : `torch.LongTensor`
        A 3 dimensional tensor of shape (batch_size, num_spans, 2) representing start and end
        indices (both inclusive) into the `sequence_length` dimension of the `target` tensor.

    # Returns

    span_embeddings : `torch.Tensor`
        A tensor with shape (batch_size, num_spans, max_batch_span_width, embedding_size]
        representing the embedded spans extracted from the batch flattened target tensor.
    span_mask: `torch.BoolTensor`
        A tensor with shape (batch_size, num_spans, max_batch_span_width) representing the mask on
        the returned span embeddings.
    """
    # both of shape (batch_size, num_spans, 1)
    span_starts, span_ends = spans.split(1, dim=-1)

    # shape (batch_size, num_spans, 1)
    # These span widths are off by 1, because the span ends are `inclusive`.
    span_widths = span_ends - span_starts

    # We need to know the maximum span width so we can
    # generate indices to extract the spans from the sequence tensor.
    # These indices will then get masked below, such that if the length
    # of a given span is smaller than the max, the rest of the values
    # are masked.
    max_batch_span_width = span_widths.max().item() + 1

    # Shape: (1, 1, max_batch_span_width)
    max_span_range_indices = get_range_vector(max_batch_span_width, get_device_of(target)).view(
        1, 1, -1
    )
    # Shape: (batch_size, num_spans, max_batch_span_width)
    # This is a broadcasted comparison - for each span we are considering,
    # we are creating a range vector of size max_span_width, but masking values
    # which are greater than the actual length of the span.
    #
    # We're using <= here (and for the mask below) because the span ends are
    # inclusive, so we want to include indices which are equal to span_widths rather
    # than using it as a non-inclusive upper bound.
    span_mask = max_span_range_indices <= span_widths
    raw_span_indices = span_starts + max_span_range_indices
    # We also don't want to include span indices which greater than the sequence_length,
    # which happens because some spans near the end of the sequence
    # have a start index + max_batch_span_width > sequence_length, so we add this to the mask here.
    span_mask = span_mask & (raw_span_indices < target.size(1)) & (0 <= raw_span_indices)
    span_indices = raw_span_indices * span_mask

    # Shape: (batch_size, num_spans, max_batch_span_width, embedding_dim)
    span_embeddings = batched_index_select(target, span_indices)

    return span_embeddings, span_mask
