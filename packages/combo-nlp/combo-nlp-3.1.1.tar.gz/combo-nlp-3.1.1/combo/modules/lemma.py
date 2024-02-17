from typing import Optional, Dict, List, Union

import torch
import torch.nn as nn
from overrides import overrides

from combo import data
from combo.config import Registry
from combo.config.from_parameters import register_arguments
from combo.models import dilated_cnn
from combo.nn import base
from combo.nn.activations import Activation
from combo.nn.utils import masked_cross_entropy
from combo.utils import ConfigurationError
from combo.models.time_distributed import TimeDistributed
from combo.predictors import Predictor


@Registry.register('combo_lemma_predictor_from_vocab')
class LemmatizerModel(Predictor):
    """Lemmatizer model."""

    @register_arguments
    def __init__(self,
                 vocabulary: data.Vocabulary,
                 char_vocab_namespace: str,
                 lemma_vocab_namespace: str,
                 embedding_dim: int,
                 input_projection_layer: base.Linear,
                 filters: List[int],
                 kernel_size: List[int],
                 stride: List[int],
                 padding: List[int],
                 dilation: List[int],
                 activations: List[Activation],
                 ):
        assert char_vocab_namespace in vocabulary.get_namespaces()
        assert lemma_vocab_namespace in vocabulary.get_namespaces()
        super().__init__()

        if len(filters) + 1 != len(kernel_size):
            raise ConfigurationError(
                f"len(filters) ({len(filters):d}) + 1 != kernel_size ({len(kernel_size):d})"
            )
        filters = filters + [vocabulary.get_vocab_size(lemma_vocab_namespace)]

        dilated_cnn_encoder = dilated_cnn.DilatedCnnEncoder(
            input_dim=embedding_dim + input_projection_layer.get_output_dim(),
            filters=filters,
            kernel_size=kernel_size,
            stride=stride,
            padding=padding,
            dilation=dilation,
            activations=activations,
        )
        self.char_embed = nn.Embedding(
            num_embeddings=vocabulary.get_vocab_size(char_vocab_namespace),
            embedding_dim=embedding_dim,
        )
        self.dilated_cnn_encoder = TimeDistributed(dilated_cnn_encoder)
        self.input_projection_layer = input_projection_layer

    @overrides
    def forward(self,
                x: Union[torch.Tensor, List[torch.Tensor]],
                mask: Optional[torch.BoolTensor] = None,
                labels: Optional[Union[torch.Tensor, List[torch.Tensor]]] = None,
                sample_weights: Optional[Union[torch.Tensor, List[torch.Tensor]]] = None) -> Dict[str, torch.Tensor]:
        encoder_emb, chars = x

        encoder_emb = self.input_projection_layer(encoder_emb)
        char_embeddings = self.char_embed(chars)

        BATCH_SIZE, _, MAX_WORD_LENGTH, CHAR_EMB = char_embeddings.size()
        encoder_emb = encoder_emb.unsqueeze(2).repeat(1, 1, MAX_WORD_LENGTH, 1)

        x = torch.cat((char_embeddings, encoder_emb), dim=-1).transpose(2, 3)
        x = self.dilated_cnn_encoder(x).transpose(2, 3)
        output = {
            "prediction": x.argmax(-1),
            "probability": x
        }

        if labels is not None:
            if mask is None:
                mask = encoder_emb.new_ones(encoder_emb.size()[:-2])
            if sample_weights is None:
                sample_weights = labels.new_ones(BATCH_SIZE)
            mask = mask.unsqueeze(2).repeat(1, 1, MAX_WORD_LENGTH).bool()
            output["loss"] = self._loss(x, labels, mask, sample_weights)

        return output

    @staticmethod
    def _loss(pred: torch.Tensor, true: torch.Tensor, mask: torch.BoolTensor,
              sample_weights: torch.Tensor) -> torch.Tensor:
        BATCH_SIZE, SENTENCE_LENGTH, MAX_WORD_LENGTH, CHAR_CLASSES = pred.size()
        pred = pred.reshape(-1, CHAR_CLASSES)

        true = true.reshape(-1)
        mask = true.gt(0)
        loss = masked_cross_entropy(pred, true, mask)
        loss = loss.reshape(BATCH_SIZE, -1) * sample_weights.unsqueeze(-1)
        valid_positions = mask.sum()
        return loss.sum() / valid_positions
