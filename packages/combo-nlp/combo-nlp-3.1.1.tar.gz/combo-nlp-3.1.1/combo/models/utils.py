import torch
import torch.nn.functional as F


def masked_cross_entropy(pred: torch.Tensor, true: torch.Tensor, mask: torch.BoolTensor) -> torch.Tensor:
    pred = pred + (mask.float().unsqueeze(-1) + 1e-45).log()
    return F.cross_entropy(pred, true, reduction="none") * mask


"""
Adapted from AllenNLP
"""


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
