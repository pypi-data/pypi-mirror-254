import torch
import torch.nn as nn
from overrides import overrides

from combo.config import FromParameters
from combo.config.registry import Registry


class Activation(nn.Module, FromParameters):
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        raise NotImplementedError


@Registry.register('linear')
class LinearActivation(Activation):
    @overrides
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return x


@Registry.register('relu')
class ReLUActivation(Activation):
    def __init__(self):
        super().__init__()
        self.__torch_activation = torch.nn.ReLU()
    @overrides
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.__torch_activation.forward(x)


@Registry.register('leaky_relu')
class ReLUActivation(Activation):
    def __init__(self):
        super().__init__()
        self.__torch_activation = torch.nn.LeakyReLU()
    @overrides
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.__torch_activation.forward(x)


@Registry.register('gelu')
class ReLUActivation(Activation):
    def __init__(self):
        super().__init__()
        self.__torch_activation = torch.nn.GELU()
    @overrides
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.__torch_activation.forward(x)


@Registry.register('sigmoid')
class SigmoidActivation(Activation):
    def __init__(self):
        super().__init__()
        self.__torch_activation = torch.nn.Sigmoid()
    @overrides
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.__torch_activation.forward(x)


@Registry.register('tanh')
class TanhActivation(Activation):
    def __init__(self):
        super().__init__()
        self.__torch_activation = torch.nn.Tanh()
    @overrides
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.__torch_activation.forward(x)


@Registry.register('mish')
class MishActivation(Activation):
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return x * torch.tanh(torch.nn.functional.softplus(x))


@Registry.register('swish')
class SwishActivation(Activation):
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return x * torch.sigmoid(x)


@Registry.register('gelu_new')
class GeluNew(Activation):
    """
    Implementation of the GELU activation function currently in Google BERT repo (identical to OpenAI GPT). Also
    see the Gaussian Error Linear Units paper: https://arxiv.org/abs/1606.08415
    """

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return (
                0.5
                * x
                * (1.0 + torch.tanh(torch.math.sqrt(2.0 / torch.math.pi) * (x + 0.044715 * torch.pow(x, 3.0))))
        )


@Registry.register('gelu_fast')
class GeluFast(Activation):
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return 0.5 * x * (1.0 + torch.tanh(x * 0.7978845608 * (1.0 + 0.044715 * x * x)))
