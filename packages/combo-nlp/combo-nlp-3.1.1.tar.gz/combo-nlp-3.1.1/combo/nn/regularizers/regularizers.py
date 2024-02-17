"""
Adapted from AllenNLP
https://github.com/allenai/allennlp/blob/80fb6061e568cb9d6ab5d45b661e86eb61b92c82/allennlp/nn/regularizers/regularizer.py
"""

import torch

from combo.config import FromParameters, Registry
from combo.config.from_parameters import register_arguments


class Regularizer(FromParameters):
    """
    An abstract class representing a regularizer. It must implement
    call, returning a scalar tensor.
    """

    def __call__(self, parameter: torch.Tensor) -> torch.Tensor:
        raise NotImplementedError


@Registry.register('l1_regularizer')
class L1Regularizer(Regularizer):
    """
    Represents a penalty proportional to the sum of the absolute values of the parameters
    Registered as a `Regularizer` with name "l1".
    """
    @register_arguments
    def __init__(self, alpha: float = 0.01) -> None:
        self.alpha = alpha

    def __call__(self, parameter: torch.Tensor) -> torch.Tensor:
        return self.alpha * torch.sum(torch.abs(parameter))


@Registry.register('l2_regularizer')
class L2Regularizer(Regularizer):
    """
    Represents a penalty proportional to the sum of squared values of the parameters
    Registered as a `Regularizer` with name "l2".
    """

    @register_arguments
    def __init__(self, alpha: float = 0.01) -> None:
        self.alpha = alpha

    def __call__(self, parameter: torch.Tensor) -> torch.Tensor:
        return self.alpha * torch.sum(torch.pow(parameter, 2))
