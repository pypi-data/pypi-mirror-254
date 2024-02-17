"""
Adapted from AllenNLP
https://github.com/allenai/allennlp/blob/main/allennlp/modules/augmented_lstm.py
"""
from typing import Optional, Tuple

import torch
from torch.nn.utils.rnn import PackedSequence, pack_padded_sequence, pad_packed_sequence

from combo.config import FromParameters, Registry
from combo.config.from_parameters import register_arguments
from combo.modules.module import Module
from combo.nn.utils import get_dropout_mask

from combo.nn.initializers import block_orthogonal
from combo.utils import ConfigurationError


@Registry.register('augumented_lstm_cell')
class AugmentedLSTMCell(Module, FromParameters):
    """
    `AugmentedLSTMCell` implements a AugmentedLSTM cell.

    # Parameters

    embed_dim : `int`
        The number of expected features in the input.
    lstm_dim : `int`
        Number of features in the hidden state of the LSTM.
    use_highway : `bool`, optional (default = `True`)
        If `True` we append a highway network to the outputs of the LSTM.
    use_bias : `bool`, optional (default = `True`)
        If `True` we use a bias in our LSTM calculations, otherwise we don't.

    # Attributes

    input_linearity : `nn.Module`
        Fused weight matrix which computes a linear function over the input.
    state_linearity : `nn.Module`
        Fused weight matrix which computes a linear function over the states.
    """

    @register_arguments
    def __init__(
        self, embed_dim: int, lstm_dim: int, use_highway: bool = True, use_bias: bool = True
    ):
        super().__init__()
        self.embed_dim = embed_dim
        self.lstm_dim = lstm_dim
        self.use_highway = use_highway
        self.use_bias = use_bias

        if use_highway:
            self._highway_inp_proj_start = 5 * self.lstm_dim
            self._highway_inp_proj_end = 6 * self.lstm_dim

            # fused linearity of input to input_gate,
            # forget_gate, memory_init, output_gate, highway_gate,
            # and the actual highway value
            self.input_linearity = torch.nn.Linear(
                self.embed_dim, self._highway_inp_proj_end, bias=self.use_bias
            )
            # fused linearity of input to input_gate,
            # forget_gate, memory_init, output_gate, highway_gate
            self.state_linearity = torch.nn.Linear(
                self.lstm_dim, self._highway_inp_proj_start, bias=True
            )
        else:
            # If there's no highway layer then we have a standard
            # LSTM. The 4 comes from fusing input, forget, memory, output
            # gates/inputs.
            self.input_linearity = torch.nn.Linear(
                self.embed_dim, 4 * self.lstm_dim, bias=self.use_bias
            )
            self.state_linearity = torch.nn.Linear(self.lstm_dim, 4 * self.lstm_dim, bias=True)
        self.reset_parameters()

    def reset_parameters(self):
        # Use sensible default initializations for parameters.
        block_orthogonal(self.input_linearity.weight.data, [self.lstm_dim, self.embed_dim])
        block_orthogonal(self.state_linearity.weight.data, [self.lstm_dim, self.lstm_dim])

        self.state_linearity.bias.data.fill_(0.0)
        # Initialize forget gate biases to 1.0 as per An Empirical
        # Exploration of Recurrent Network Architectures, (Jozefowicz, 2015).
        self.state_linearity.bias.data[self.lstm_dim : 2 * self.lstm_dim].fill_(1.0)

    def forward(
        self,
        x: torch.Tensor,
        states=Tuple[torch.Tensor, torch.Tensor],
        variational_dropout_mask: Optional[torch.BoolTensor] = None,
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        !!! Warning
            DO NOT USE THIS LAYER DIRECTLY, instead use the AugmentedLSTM class

        # Parameters

        x : `torch.Tensor`
            Input tensor of shape (bsize x input_dim).
        states : `Tuple[torch.Tensor, torch.Tensor]`
            Tuple of tensors containing
            the hidden state and the cell state of each element in
            the batch. Each of these tensors have a dimension of
            (bsize x nhid). Defaults to `None`.

        # Returns

        `Tuple[torch.Tensor, torch.Tensor]`
            Returned states. Shape of each state is (bsize x nhid).

        """
        hidden_state, memory_state = states

        # In Pytext this was done as the last step of the cell.
        # But the original AugmentedLSTM from AllenNLP this was done before the processing
        if variational_dropout_mask is not None and self.training:
            hidden_state = hidden_state * variational_dropout_mask

        projected_input = self.input_linearity(x)
        projected_state = self.state_linearity(hidden_state)

        input_gate = forget_gate = memory_init = output_gate = highway_gate = None
        if self.use_highway:
            fused_op = projected_input[:, : 5 * self.lstm_dim] + projected_state
            fused_chunked = torch.chunk(fused_op, 5, 1)
            (input_gate, forget_gate, memory_init, output_gate, highway_gate) = fused_chunked
            highway_gate = torch.sigmoid(highway_gate)
        else:
            fused_op = projected_input + projected_state
            input_gate, forget_gate, memory_init, output_gate = torch.chunk(fused_op, 4, 1)
        input_gate = torch.sigmoid(input_gate)
        forget_gate = torch.sigmoid(forget_gate)
        memory_init = torch.tanh(memory_init)
        output_gate = torch.sigmoid(output_gate)
        memory = input_gate * memory_init + forget_gate * memory_state
        timestep_output: torch.Tensor = output_gate * torch.tanh(memory)

        if self.use_highway:
            highway_input_projection = projected_input[
                :, self._highway_inp_proj_start : self._highway_inp_proj_end
            ]
            timestep_output = (
                highway_gate * timestep_output
                + (1 - highway_gate) * highway_input_projection  # type: ignore
            )

        return timestep_output, memory


@Registry.register('augumented_lstm')
class AugmentedLstm(Module, FromParameters):
    """
    `AugmentedLstm` implements a one-layer single directional
    AugmentedLSTM layer. AugmentedLSTM is an LSTM which optionally
    appends an optional highway network to the output layer. Furthermore the
    dropout controls the level of variational dropout done.

    # Parameters

    input_size : `int`
        The number of expected features in the input.
    hidden_size : `int`
        Number of features in the hidden state of the LSTM.
        Defaults to 32.
    go_forward : `bool`
        Whether to compute features left to right (forward)
        or right to left (backward).
    recurrent_dropout_probability : `float`
        Variational dropout probability to use. Defaults to 0.0.
    use_highway : `bool`
        If `True` we append a highway network to the outputs of the LSTM.
    use_input_projection_bias : `bool`
        If `True` we use a bias in our LSTM calculations, otherwise we don't.

    # Attributes

    cell : `AugmentedLSTMCell`
        `AugmentedLSTMCell` that is applied at every timestep.

    """

    @register_arguments
    def __init__(
        self,
        input_size: int,
        hidden_size: int,
        go_forward: bool = True,
        recurrent_dropout_probability: float = 0.0,
        use_highway: bool = True,
        use_input_projection_bias: bool = True,
    ):
        super().__init__()

        self.embed_dim = input_size
        self.lstm_dim = hidden_size

        self.go_forward = go_forward
        self.use_highway = use_highway
        self.recurrent_dropout_probability = recurrent_dropout_probability

        self.cell = AugmentedLSTMCell(
            self.embed_dim, self.lstm_dim, self.use_highway, use_input_projection_bias
        )

    def forward(
        self, inputs: PackedSequence, states: Optional[Tuple[torch.Tensor, torch.Tensor]] = None
    ) -> Tuple[PackedSequence, Tuple[torch.Tensor, torch.Tensor]]:
        """
        Warning: Would be better to use the BiAugmentedLstm class in a regular model

        Given an input batch of sequential data such as word embeddings, produces a single layer unidirectional
        AugmentedLSTM representation of the sequential input and new state tensors.

        # Parameters

        inputs : `PackedSequence`
            `bsize` sequences of shape `(len, input_dim)` each, in PackedSequence format
        states : `Tuple[torch.Tensor, torch.Tensor]`
            Tuple of tensors containing the initial hidden state and
            the cell state of each element in the batch. Each of these tensors have a dimension of
            (1 x bsize x nhid). Defaults to `None`.

        # Returns

        `Tuple[PackedSequence, Tuple[torch.Tensor, torch.Tensor]]`
            AugmentedLSTM representation of input and the state of the LSTM `t = seq_len`.
            Shape of representation is (bsize x seq_len x representation_dim).
            Shape of each state is (1 x bsize x nhid).

        """
        if not isinstance(inputs, PackedSequence):
            raise ConfigurationError("inputs must be PackedSequence but got %s" % (type(inputs)))

        sequence_tensor, batch_lengths = pad_packed_sequence(inputs, batch_first=True)
        batch_size = sequence_tensor.size()[0]
        total_timesteps = sequence_tensor.size()[1]
        output_accumulator = sequence_tensor.new_zeros(batch_size, total_timesteps, self.lstm_dim)
        if states is None:
            full_batch_previous_memory = sequence_tensor.new_zeros(batch_size, self.lstm_dim)
            full_batch_previous_state = sequence_tensor.data.new_zeros(batch_size, self.lstm_dim)
        else:
            full_batch_previous_state = states[0].squeeze(0)
            full_batch_previous_memory = states[1].squeeze(0)
        current_length_index = batch_size - 1 if self.go_forward else 0
        if self.recurrent_dropout_probability > 0.0:
            dropout_mask = get_dropout_mask(
                self.recurrent_dropout_probability, full_batch_previous_memory
            )
        else:
            dropout_mask = None

        for timestep in range(total_timesteps):
            index = timestep if self.go_forward else total_timesteps - timestep - 1

            if self.go_forward:
                while batch_lengths[current_length_index] <= index:
                    current_length_index -= 1
            # If we're going backwards, we are _picking up_ more indices.
            else:
                # First conditional: Are we already at the maximum
                # number of elements in the batch?
                # Second conditional: Does the next shortest
                # sequence beyond the current batch
                # index require computation use this timestep?
                while (
                    current_length_index < (len(batch_lengths) - 1)
                    and batch_lengths[current_length_index + 1] > index
                ):
                    current_length_index += 1

            previous_memory = full_batch_previous_memory[0 : current_length_index + 1].clone()
            previous_state = full_batch_previous_state[0 : current_length_index + 1].clone()
            timestep_input = sequence_tensor[0 : current_length_index + 1, index]
            timestep_output, memory = self.cell(
                timestep_input,
                (previous_state, previous_memory),
                dropout_mask[0 : current_length_index + 1] if dropout_mask is not None else None,
            )
            full_batch_previous_memory = full_batch_previous_memory.data.clone()
            full_batch_previous_state = full_batch_previous_state.data.clone()
            full_batch_previous_memory[0 : current_length_index + 1] = memory
            full_batch_previous_state[0 : current_length_index + 1] = timestep_output
            output_accumulator[0 : current_length_index + 1, index, :] = timestep_output

        output_accumulator = pack_padded_sequence(
            output_accumulator, batch_lengths, batch_first=True
        )

        # Mimic the pytorch API by returning state in the following shape:
        # (num_layers * num_directions, batch_size, lstm_dim). As this
        # LSTM cannot be stacked, the first dimension here is just 1.
        final_state = (
            full_batch_previous_state.unsqueeze(0),
            full_batch_previous_memory.unsqueeze(0),
        )
        return output_accumulator, final_state
