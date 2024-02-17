"""
Adapted from COMBO
Author: Mateusz Klimaszewski
"""
from typing import Dict, List, Optional, Union
import torch
from overrides import overrides

from combo import data
from combo.config import Registry
from combo.config.from_parameters import register_arguments
from combo.data.vocabulary import get_slices_if_not_provided
from combo.nn import base
from combo.nn.activations import Activation
from combo.nn.utils import masked_cross_entropy
from combo.predictors.predictor import Predictor
from combo.utils import ConfigurationError


@Registry.register('combo_morpho_from_vocab')
class MorphologicalFeatures(Predictor):
    """Morphological features predicting model."""

    @register_arguments
    def __init__(self,
                 vocabulary: data.Vocabulary,
                 vocab_namespace: str,
                 input_dim: int,
                 num_layers: int,
                 hidden_dims: List[int],
                 activations: List[Activation],  # change to Union[Activation, List[Activation]]
                 dropout: Union[float, List[float]] = 0.0,
                 ):
        super().__init__()
        if len(hidden_dims) + 1 != num_layers:
            raise ConfigurationError(
                f"len(hidden_dims) ({len(hidden_dims):d}) + 1 != num_layers ({num_layers:d})"
            )

        assert vocab_namespace in vocabulary.get_namespaces()

        slices = get_slices_if_not_provided(vocabulary)
        hidden_dims = hidden_dims + [vocabulary.get_vocab_size(vocab_namespace)]
        self.feedforward_network = base.FeedForward(
            input_dim=input_dim,
            num_layers=num_layers,
            hidden_dims=hidden_dims,
            activations=activations,
            dropout=dropout)
        self.slices = slices

    @overrides
    def forward(self,
                x: Union[torch.Tensor, List[torch.Tensor]],
                mask: Optional[torch.BoolTensor] = None,
                labels: Optional[Union[torch.Tensor, List[torch.Tensor]]] = None,
                sample_weights: Optional[Union[torch.Tensor, List[torch.Tensor]]] = None) -> Dict[str, torch.Tensor]:
        if mask is None:
            mask = x.new_ones(x.size()[:-1])

        x, feature_maps = self.feedforward_network(x)

        prediction = []
        for _, cat_indices in self.slices.items():
            prediction.append(x[:, :, cat_indices].argmax(dim=-1))

        output = {
            "prediction": torch.stack(prediction, dim=-1),
            "probability": x,
            "embedding": feature_maps[-1],
        }

        if labels is not None:
            if sample_weights is None:
                sample_weights = labels.new_ones([mask.size(0)])
            output["loss"] = self._loss(x, labels, mask, sample_weights)

        return output

    def _loss(self, pred: torch.Tensor, true: torch.Tensor, mask: torch.BoolTensor,
              sample_weights: torch.Tensor) -> torch.Tensor:
        assert pred.size() == true.size()
        BATCH_SIZE, _, MORPHOLOGICAL_FEATURES = pred.size()

        valid_positions = mask.sum()

        pred = pred.reshape(-1, MORPHOLOGICAL_FEATURES)
        true = true.reshape(-1, MORPHOLOGICAL_FEATURES)
        mask = mask.reshape(-1)
        loss = None
        loss_func = masked_cross_entropy
        for cat, cat_indices in self.slices.items():
            if cat not in ["__PAD__", "_"]:
                if loss is None:
                    loss = loss_func(pred[:, cat_indices],
                                     true[:, cat_indices].argmax(dim=1),
                                     mask)
                else:
                    loss += loss_func(pred[:, cat_indices],
                                      true[:, cat_indices].argmax(dim=1),
                                      mask)
        loss = loss.reshape(BATCH_SIZE, -1) * sample_weights.unsqueeze(-1)
        return loss.sum() / valid_positions
