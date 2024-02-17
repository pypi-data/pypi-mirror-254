from combo.config import Registry
from combo.config.from_parameters import register_arguments
from combo.data import Vocabulary
from combo.nn.utils import masked_cross_entropy
from combo.nn.base import FeedForward
from combo.predictors import Predictor
import torch
from typing import Dict, List, Optional, Union

from combo.utils import ConfigurationError


@Registry.register("feedforward_predictor")
@Registry.register("feedforward_predictor_from_vocab", constructor_method="from_vocab")
class FeedForwardPredictor(Predictor):
    """Feedforward predictor. Should be used on top of Seq2Seq encoder."""

    @register_arguments
    def __init__(self, feedforward_network: "FeedForward"):
        super().__init__()
        self.feedforward_network = feedforward_network

    def forward(self,
                x: Union[torch.Tensor, List[torch.Tensor]],
                mask: Optional[torch.BoolTensor] = None,
                labels: Optional[Union[torch.Tensor, List[torch.Tensor]]] = None,
                sample_weights: Optional[Union[torch.Tensor, List[torch.Tensor]]] = None) -> Dict[str, torch.Tensor]:
        if mask is None:
            mask = x.new_ones(x.size()[:-1])

        x, feature_maps = self.feedforward_network(x)
        output = {
            "prediction": x.argmax(-1),
            "probability": x,
            "embedding": feature_maps[-1],
        }

        if labels is not None:
            if sample_weights is None:
                sample_weights = labels.new_ones([mask.size(0)])
            output["loss"] = self._loss(x, labels, mask, sample_weights)

        return output

    def _loss(self,
              pred: torch.Tensor,
              true: torch.Tensor,
              mask: torch.BoolTensor,
              sample_weights: torch.Tensor) -> torch.Tensor:
        BATCH_SIZE, _, CLASSES = pred.size()
        valid_positions = mask.sum()
        pred = pred.reshape(-1, CLASSES)
        true = true.reshape(-1)
        mask = mask.reshape(-1)
        loss = masked_cross_entropy(pred, true, mask)
        loss = loss.reshape(BATCH_SIZE, -1) * sample_weights.unsqueeze(-1)
        return loss.sum() / valid_positions

    @classmethod
    def from_vocab(cls,
                   vocabulary: Vocabulary,
                   vocab_namespace: str,
                   input_dim: int,
                   num_layers: int,
                   hidden_dims: List[int],
                   activations: Union["Activation", List["Activation"]],
                   dropout: Union[float, List[float]] = 0.0,
                   ):
        if len(hidden_dims) + 1 != num_layers:
            raise ConfigurationError(
                f"len(hidden_dims) ({len(hidden_dims):d}) + 1 != num_layers ({num_layers:d})"
            )

        assert vocab_namespace in vocabulary.get_namespaces(), \
            f"There is not {vocab_namespace} in created vocabs, check if this field has any values to predict!"
        hidden_dims_w_vocab_added = hidden_dims + [vocabulary.get_vocab_size(vocab_namespace)]

        ff_p = cls(FeedForward(
            input_dim=input_dim,
            num_layers=num_layers,
            hidden_dims=hidden_dims_w_vocab_added,
            activations=activations,
            dropout=dropout))

        ff_p.constructed_from = "from_vocab"
        ff_p.constructed_args = {
            "vocab_namespace": vocab_namespace,
            "input_dim": input_dim,
            "num_layers": num_layers,
            "hidden_dims": hidden_dims,
            "activations": activations,
            "dropout": dropout
        }
        return ff_p
