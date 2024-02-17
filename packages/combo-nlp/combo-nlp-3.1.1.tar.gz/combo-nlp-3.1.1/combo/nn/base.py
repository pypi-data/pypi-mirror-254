from typing import Optional, List, Union, Tuple

import torch
import torch.nn as nn

import combo.utils.checks as checks
from combo.config.from_parameters import FromParameters, register_arguments
from combo.config.registry import Registry


@Registry.register("linear_layer")
class Linear(nn.Linear, FromParameters):
    @register_arguments
    def __init__(self,
                 in_features: int,
                 out_features: int,
                 activation: "Activation" = None,
                 dropout_rate: Optional[float] = 0.0):
        super().__init__(in_features, out_features)
        self.activation = activation if activation else self.identity
        self.dropout = nn.Dropout(p=dropout_rate) if dropout_rate else self.identity

    def forward(self, x: torch.FloatTensor) -> torch.FloatTensor:
        x = super().forward(x)
        x = self.activation(x)
        return self.dropout(x)

    def get_output_dim(self) -> int:
        return self.out_features

    @staticmethod
    def identity(x):
        return x

@Registry.register("feedforward_layer")
class FeedForward(torch.nn.Module, FromParameters):
    """
    Modified copy of allennlp.modules.feedforward.FeedForward

    This `Module` is a feed-forward neural network, just a sequence of `Linear` layers with
    activation functions in between.

    # Parameters

    input_dim : `int`, required
        The dimensionality of the input.  We assume the input has shape `(batch_size, input_dim)`.
    num_layers : `int`, required
        The number of `Linear` layers to apply to the input.
    hidden_dims : `Union[int, List[int]]`, required
        The output dimension of each of the `Linear` layers.  If this is a single `int`, we use
        it for all `Linear` layers.  If it is a `List[int]`, `len(hidden_dims)` must be
        `num_layers`.
    activations : `Union[Activation, List[Activation]]`, required
        The activation function to use after each `Linear` layer.  If this is a single function,
        we use it after all `Linear` layers.  If it is a `List[Activation]`,
        `len(activations)` must be `num_layers`. Activation must have torch.nn.Module type.
    dropout : `Union[float, List[float]]`, optional (default = `0.0`)
        If given, we will apply this amount of dropout after each layer.  Semantics of `float`
        versus `List[float]` is the same as with other parameters.

    # Examples

    ```python
    FeedForward(124, 2, [64, 32], torch.nn.ReLU(), 0.2)
    #> FeedForward(
    #>   (_activations): ModuleList(
    #>     (0): ReLU()
    #>     (1): ReLU()
    #>   )
    #>   (_linear_layers): ModuleList(
    #>     (0): Linear(in_features=124, out_features=64, bias=True)
    #>     (1): Linear(in_features=64, out_features=32, bias=True)
    #>   )
    #>   (_dropout): ModuleList(
    #>     (0): Dropout(p=0.2, inplace=False)
    #>     (1): Dropout(p=0.2, inplace=False)
    #>   )
    #> )
    ```
    """
    @register_arguments
    def __init__(
            self,
            input_dim: int,
            num_layers: int,
            hidden_dims: Union[int, List[int]],
            activations: List["Activation"], # Change to Union[Activation, List[Activation]]
            dropout: Union[float, List[float]] = 0.0,
    ) -> None:

        super().__init__()
        if not isinstance(hidden_dims, list):
            hidden_dims = [hidden_dims] * num_layers  # type: ignore
        if not isinstance(activations, list):
            activations = [activations] * num_layers  # type: ignore
        if not isinstance(dropout, list):
            dropout = [dropout] * num_layers  # type: ignore
        if len(hidden_dims) != num_layers:
            raise checks.ConfigurationError(
                "len(hidden_dims) (%d) != num_layers (%d)" % (len(hidden_dims), num_layers)
            )
        if len(activations) != num_layers:
            raise checks.ConfigurationError(
                "len(activations) (%d) != num_layers (%d)" % (len(activations), num_layers)
            )
        if len(dropout) != num_layers:
            raise checks.ConfigurationError(
                "len(dropout) (%d) != num_layers (%d)" % (len(dropout), num_layers)
            )
        self._activations = torch.nn.ModuleList(activations)
        input_dims = [input_dim] + hidden_dims[:-1]
        linear_layers = []
        for layer_input_dim, layer_output_dim in zip(input_dims, hidden_dims):
            linear_layers.append(torch.nn.Linear(layer_input_dim, layer_output_dim))
        self._linear_layers = torch.nn.ModuleList(linear_layers)
        dropout_layers = [torch.nn.Dropout(p=value) for value in dropout]
        self._dropout = torch.nn.ModuleList(dropout_layers)
        self._output_dim = hidden_dims[-1]
        self.input_dim = input_dim

    def get_output_dim(self):
        return self._output_dim

    def get_input_dim(self):
        return self.input_dim

    def forward(self, inputs: torch.Tensor) -> Tuple[torch.Tensor, List[torch.Tensor]]:

        output = inputs
        feature_maps = []
        for layer, activation, dropout in zip(
                self._linear_layers, self._activations, self._dropout
        ):
            feature_maps.append(output)
            output = dropout(activation(layer(output)))
        return output, feature_maps
