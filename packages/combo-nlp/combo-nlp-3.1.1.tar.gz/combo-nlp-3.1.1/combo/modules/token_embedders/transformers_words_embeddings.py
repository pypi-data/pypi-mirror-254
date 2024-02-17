"""
Adapted from COMBO
Author: Mateusz Klimaszewski
"""
from typing import Any, Dict, Optional

import torch
from overrides import overrides

from combo.config import Registry
from combo.config.from_parameters import register_arguments
from combo.modules.token_embedders.pretrained_transformer_mismatched_embedder import \
    PretrainedTransformerMismatchedEmbedder
from combo.nn import base
from combo.nn.activations import Activation


@Registry.register("transformers_word_embedder")
class TransformersWordEmbedder(PretrainedTransformerMismatchedEmbedder):
    """
    Transformers word embeddings as last hidden state + optional projection layers.

    Tested with Bert (but should work for other models as well).
    """

    authorized_missing_keys = [r"position_ids$"]

    @register_arguments
    def __init__(self,
                 model_name: str,
                 projection_dim: int = 0,
                 projection_activation: Optional[Activation] = lambda x: x,
                 projection_dropout_rate: Optional[float] = 0.0,
                 freeze_transformer: bool = True,
                 last_layer_only: bool = True,
                 tokenizer_kwargs: Optional[Dict[str, Any]] = None,
                 transformer_kwargs: Optional[Dict[str, Any]] = None):
        super().__init__(model_name,
                         train_parameters=not freeze_transformer,
                         last_layer_only=last_layer_only,
                         tokenizer_kwargs=tokenizer_kwargs,
                         transformer_kwargs=transformer_kwargs)
        if projection_dim:
            self.projection_layer = base.Linear(in_features=super().get_output_dim(),
                                                out_features=projection_dim,
                                                dropout_rate=projection_dropout_rate,
                                                activation=projection_activation)
            self.output_dim = projection_dim
        else:
            self.projection_layer = None
            self.output_dim = super().get_output_dim()

    #@overrides
    def forward(
            self,
            token_ids: torch.LongTensor,
            mask: torch.BoolTensor,
            offsets: torch.LongTensor,
            wordpiece_mask: torch.BoolTensor,
            type_ids: Optional[torch.LongTensor] = None,
            segment_concat_mask: Optional[torch.BoolTensor] = None,
    ) -> torch.Tensor:  # type: ignore
        x = super().forward(token_ids, mask, offsets, wordpiece_mask, type_ids, segment_concat_mask)
        if self.projection_layer:
            x = self.projection_layer(x)
        return x

    @overrides
    def get_output_dim(self) -> int:
        return self.output_dim
