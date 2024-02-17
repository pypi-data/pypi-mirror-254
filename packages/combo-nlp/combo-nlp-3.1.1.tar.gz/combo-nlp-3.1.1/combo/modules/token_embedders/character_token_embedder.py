"""
Adapted from COMBO
Author: Mateusz Klimaszewski
https://gitlab.clarin-pl.eu/syntactic-tools/combo/-/blob/master/combo/models/embeddings.py
"""
from overrides import overrides

from combo.config import Registry
from combo.config.from_parameters import register_arguments
from combo.data import Vocabulary
from combo.models.dilated_cnn import DilatedCnnEncoder
from combo.modules.token_embedders import TokenEmbedder

from typing import Optional
import torch
import torch.nn as nn
from combo import modules


# @token_embedders.TokenEmbedder.register("char_embeddings")
@Registry.register("char_embeddings_token_embedder")
class CharacterBasedWordEmbedder(TokenEmbedder):
    """Character-based word embeddings."""

    @register_arguments
    def __init__(self,
                 embedding_dim: int,
                 vocabulary: Vocabulary,
                 dilated_cnn_encoder: DilatedCnnEncoder,
                 vocab_namespace: str = "token_characters"):
        assert vocab_namespace in vocabulary.get_namespaces()
        super().__init__()
        self.char_embed = nn.Embedding(
            num_embeddings=vocabulary.get_vocab_size(vocab_namespace),
            embedding_dim=embedding_dim,
        )
        self.dilated_cnn_encoder = modules.TimeDistributed(dilated_cnn_encoder)
        self.output_dim = embedding_dim

    def forward(self,
                x: torch.Tensor,
                char_mask: Optional[torch.BoolTensor] = None) -> torch.Tensor:
        if char_mask is None:
            char_mask = x.new_ones(x.size())

        x = self.char_embed(x)
        x = x * char_mask.unsqueeze(-1).float()
        x = self.dilated_cnn_encoder(x.transpose(2, 3))
        return torch.max(x, dim=-1)[0]

    @overrides
    def get_output_dim(self) -> int:
        return self.output_dim
