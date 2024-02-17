"""
Adapted parts from AllenNLP
and COMBO (Author: Mateusz Klimaszewski)
"""

from typing import Optional, Tuple, List
import torch
import torch.nn.utils.rnn as rnn
from torch.nn.utils.rnn import PackedSequence, pack_padded_sequence, pad_packed_sequence

from combo.config import FromParameters, Registry
from combo.config.from_parameters import register_arguments
from combo.modules import input_variational_dropout
from combo.modules.augmented_lstm import AugmentedLstm
from combo.modules.input_variational_dropout import InputVariationalDropout
from combo.modules.seq2seq_encoders.seq2seq_encoder import Seq2SeqEncoder
from combo.utils import ConfigurationError

TensorPair = Tuple[torch.Tensor, torch.Tensor]


@Registry.register('stacked_bilstm')
class StackedBidirectionalLstm(torch.nn.Module, FromParameters):
    """
    A standard stacked Bidirectional LSTM where the LSTM layers
    are concatenated between each layer. The only difference between
    this and a regular bidirectional LSTM is the app alication of
    variational dropout to the hidden states and outputs of each layer apart
    from the last layer of the LSTM. Note that this will be slower, as it
    doesn't use CUDNN.

    [0]: https://arxiv.org/abs/1512.05287

    # Parameters

    input_size : `int`, required
        The dimension of the inputs to the LSTM.
    hidden_size : `int`, required
        The dimension of the outputs of the LSTM.
    num_layers : `int`, required
        The number of stacked Bidirectional LSTMs to use.
    recurrent_dropout_probability : `float`, optional (default = `0.0`)
        The recurrent dropout probability to be used in a dropout scheme as
        stated in [A Theoretically Grounded Application of Dropout in Recurrent
        Neural Networks][0].
    layer_dropout_probability : `float`, optional (default = `0.0`)
        The layer wise dropout probability to be used in a dropout scheme as
        stated in [A Theoretically Grounded Application of Dropout in Recurrent
        Neural Networks][0].
    use_highway : `bool`, optional (default = `True`)
        Whether or not to use highway connections between layers. This effectively involves
        reparameterising the normal output of an LSTM as::

            gate = sigmoid(W_x1 * x_t + W_h * h_t)
            output = gate * h_t  + (1 - gate) * (W_x2 * x_t)
    """

    @register_arguments
    def __init__(
            self,
            input_size: int,
            hidden_size: int,
            num_layers: int,
            recurrent_dropout_probability: float = 0.0,
            layer_dropout_probability: float = 0.0,
            use_highway: bool = True,
    ) -> None:
        super().__init__()

        # Required to be wrapped with a `PytorchSeq2SeqWrapper`.
        self.__input_size = input_size
        self.__hidden_size = hidden_size
        self.__num_layers = num_layers
        self.__bidirectional = True

        layers = []
        lstm_input_size = input_size
        for layer_index in range(num_layers):
            forward_layer = AugmentedLstm(
                lstm_input_size,
                hidden_size,
                go_forward=True,
                recurrent_dropout_probability=recurrent_dropout_probability,
                use_highway=use_highway,
                use_input_projection_bias=False,
            )
            backward_layer = AugmentedLstm(
                lstm_input_size,
                hidden_size,
                go_forward=False,
                recurrent_dropout_probability=recurrent_dropout_probability,
                use_highway=use_highway,
                use_input_projection_bias=False,
            )

            lstm_input_size = hidden_size * 2
            self.add_module("forward_layer_{}".format(layer_index), forward_layer)
            self.add_module("backward_layer_{}".format(layer_index), backward_layer)
            layers.append([forward_layer, backward_layer])
        self.lstm_layers = layers
        self.layer_dropout = InputVariationalDropout(layer_dropout_probability)

    @property
    def input_size(self) -> int:
        return self.__input_size

    @property
    def hidden_size(self) -> int:
        return self.__hidden_size

    @property
    def num_layers(self) -> int:
        return self.__num_layers

    @property
    def bidirectional(self) -> int:
        return self.__bidirectional

    def forward(
            self, inputs: PackedSequence, initial_state: Optional[TensorPair] = None
    ) -> Tuple[PackedSequence, TensorPair]:
        """
        # Parameters

        inputs : `PackedSequence`, required.
            A batch first `PackedSequence` to run the stacked LSTM over.
        initial_state : `Tuple[torch.Tensor, torch.Tensor]`, optional, (default = `None`)
            A tuple (state, memory) representing the initial hidden state and memory
            of the LSTM. Each tensor has shape (num_layers, batch_size, output_dimension * 2).

        # Returns

        output_sequence : `PackedSequence`
            The encoded sequence of shape (batch_size, sequence_length, hidden_size * 2)
        final_states: `torch.Tensor`
            The per-layer final (state, memory) states of the LSTM, each with shape
            (num_layers * 2, batch_size, hidden_size * 2).
        """
        if initial_state is None:
            hidden_states: List[Optional[TensorPair]] = [None] * len(self.lstm_layers)
        elif initial_state[0].size()[0] != len(self.lstm_layers):
            raise ConfigurationError(
                "Initial states were passed to forward() but the number of "
                "initial states does not match the number of layers."
            )
        else:
            hidden_states = list(zip(initial_state[0].split(1, 0), initial_state[1].split(1, 0)))

        output_sequence = inputs
        final_h = []
        final_c = []
        for i, state in enumerate(hidden_states):
            forward_layer = getattr(self, "forward_layer_{}".format(i))
            backward_layer = getattr(self, "backward_layer_{}".format(i))
            # The state is duplicated to mirror the Pytorch API for LSTMs.
            forward_output, final_forward_state = forward_layer(output_sequence, state)
            backward_output, final_backward_state = backward_layer(output_sequence, state)

            forward_output, lengths = pad_packed_sequence(forward_output, batch_first=True)
            backward_output, _ = pad_packed_sequence(backward_output, batch_first=True)

            output_sequence = torch.cat([forward_output, backward_output], -1)
            # Apply layer wise dropout on each output sequence apart from the
            # first (input) and last
            if i < (self.num_layers - 1):
                output_sequence = self.layer_dropout(output_sequence)
            output_sequence = pack_padded_sequence(output_sequence, lengths, batch_first=True)

            final_h.extend([final_forward_state[0], final_backward_state[0]])
            final_c.extend([final_forward_state[1], final_backward_state[1]])

        final_h = torch.cat(final_h, dim=0)
        final_c = torch.cat(final_c, dim=0)
        final_state_tuple = (final_h, final_c)
        return output_sequence, final_state_tuple




# TODO: merge into one
@Registry.register('combo_stacked_bilstm')
class ComboStackedBidirectionalLSTM(StackedBidirectionalLstm, FromParameters):
    @register_arguments
    def __init__(self, input_size: int, hidden_size: int, num_layers: int, recurrent_dropout_probability: float,
                 layer_dropout_probability: float, use_highway: bool = False):
        super().__init__(input_size=input_size,
                         hidden_size=hidden_size,
                         num_layers=num_layers,
                         recurrent_dropout_probability=recurrent_dropout_probability,
                         layer_dropout_probability=layer_dropout_probability,
                         use_highway=use_highway)

    # @overrides
    def forward(self,
                inputs: rnn.PackedSequence,
                initial_state: Optional[Tuple[torch.Tensor, torch.Tensor]] = None
                ) -> Tuple[rnn.PackedSequence, Tuple[torch.Tensor, torch.Tensor]]:
        """Changes when compared to stacked_bidirectional_lstm.StackedBidirectionalLstm
        * dropout also on last layer
        * accepts BxTxD tensor
        * state from n-1 layer used as n layer initial state

        :param inputs:
        :param initial_state:
        :return:
        """
        output_sequence = inputs
        state_fwd = None
        state_bwd = None
        for i in range(self.num_layers):
            forward_layer = getattr(self, f"forward_layer_{i}")
            backward_layer = getattr(self, f"backward_layer_{i}")

            forward_output, state_fwd = forward_layer(output_sequence, state_fwd)
            backward_output, state_bwd = backward_layer(output_sequence, state_bwd)

            forward_output, lengths = rnn.pad_packed_sequence(forward_output, batch_first=True)
            backward_output, _ = rnn.pad_packed_sequence(backward_output, batch_first=True)

            output_sequence = torch.cat([forward_output, backward_output], -1)

            output_sequence = self.layer_dropout(output_sequence)
            output_sequence = rnn.pack_padded_sequence(output_sequence, lengths, batch_first=True)

        return output_sequence, (state_fwd, state_bwd)


@Registry.register('combo_encoder')
class ComboEncoder(Seq2SeqEncoder, FromParameters):
    """COMBO encoder (https://www.aclweb.org/anthology/K18-2004.pdf).

    This implementation uses Variational Dropout on the input and then outputs of each BiLSTM layer
    (instead of used Gaussian Dropout and Gaussian Noise).
    """

    @register_arguments
    def __init__(self,
                 stacked_bilstm: ComboStackedBidirectionalLSTM,
                 layer_dropout_probability: float):
        super().__init__(stacked_bilstm, stateful=False)
        self.layer_dropout = input_variational_dropout.InputVariationalDropout(p=layer_dropout_probability)

    def forward(self,
                inputs: torch.Tensor,
                mask: torch.BoolTensor,
                hidden_state: torch.Tensor = None) -> torch.Tensor:
        x = self.layer_dropout(inputs)
        x = super().forward(x, mask)
        return self.layer_dropout(x)
