import torch
from torch.nn.utils.rnn import pad_packed_sequence

from combo.modules.encoder import _EncoderBase
from combo.config.from_parameters import FromParameters, register_arguments
from combo.utils import ConfigurationError


class Seq2SeqEncoder(_EncoderBase, FromParameters):
    """
    A `Seq2SeqEncoder` is a `Module` that takes as input a sequence of vectors and returns a
    modified sequence of vectors.  Input shape : `(batch_size, sequence_length, input_dim)`; output
    shape : `(batch_size, sequence_length, output_dim)`.

    We add two methods to the basic `Module` API: `get_input_dim()` and `get_output_dim()`.
    You might need this if you want to construct a `Linear` layer using the output of this encoder,
    or to raise sensible errors for mis-matching input dimensions.
    """

    @register_arguments
    def __init__(self, module: torch.nn.Module, stateful: bool = False) -> None:
        super().__init__(stateful)
        self._module = module
        try:
            if not self._module.batch_first:
                raise ConfigurationError("Our encoder semantics assumes batch is always first!")
        except AttributeError:
            pass

        try:
            self._is_bidirectional = self._module.bidirectional
        except AttributeError:
            self._is_bidirectional = False
        if self._is_bidirectional:
            self._num_directions = 2
        else:
            self._num_directions = 1

    def get_input_dim(self) -> int:
        return self._module.input_size

    def get_output_dim(self) -> int:
        return self._module.hidden_size * self._num_directions

    def is_bidirectional(self) -> bool:
        return self._is_bidirectional

    def forward(
        self, inputs: torch.Tensor, mask: torch.BoolTensor, hidden_state: torch.Tensor = None
    ) -> torch.Tensor:

        if self.stateful and mask is None:
            raise ValueError("Always pass a mask with stateful RNNs.")
        if self.stateful and hidden_state is not None:
            raise ValueError("Stateful RNNs provide their own initial hidden_state.")

        if mask is None:
            return self._module(inputs, hidden_state)[0]

        batch_size, total_sequence_length = mask.size()

        packed_sequence_output, final_states, restoration_indices = self.sort_and_run_forward(
            self._module, inputs, mask, hidden_state
        )

        unpacked_sequence_tensor, _ = pad_packed_sequence(packed_sequence_output, batch_first=True)

        num_valid = unpacked_sequence_tensor.size(0)
        # Some RNNs (GRUs) only return one state as a Tensor.  Others (LSTMs) return two.
        # If one state, use a single element list to handle in a consistent manner below.
        if not isinstance(final_states, (list, tuple)) and self.stateful:
            final_states = [final_states]

        # Add back invalid rows.
        if num_valid < batch_size:
            _, length, output_dim = unpacked_sequence_tensor.size()
            zeros = unpacked_sequence_tensor.new_zeros(batch_size - num_valid, length, output_dim)
            unpacked_sequence_tensor = torch.cat([unpacked_sequence_tensor, zeros], 0)

            # The states also need to have invalid rows added back.
            if self.stateful:
                new_states = []
                for state in final_states:
                    num_layers, _, state_dim = state.size()
                    zeros = state.new_zeros(num_layers, batch_size - num_valid, state_dim)
                    new_states.append(torch.cat([state, zeros], 1))
                final_states = new_states

        # It's possible to need to pass sequences which are padded to longer than the
        # max length of the sequence to a Seq2SeqEncoder. However, packing and unpacking
        # the sequences mean that the returned tensor won't include these dimensions, because
        # the RNN did not need to process them. We add them back on in the form of zeros here.
        sequence_length_difference = total_sequence_length - unpacked_sequence_tensor.size(1)
        if sequence_length_difference > 0:
            zeros = unpacked_sequence_tensor.new_zeros(
                batch_size, sequence_length_difference, unpacked_sequence_tensor.size(-1)
            )
            unpacked_sequence_tensor = torch.cat([unpacked_sequence_tensor, zeros], 1)

        if self.stateful:
            self._update_states(final_states, restoration_indices)

        # Restore the original indices and return the sequence.
        return unpacked_sequence_tensor.index_select(0, restoration_indices)
