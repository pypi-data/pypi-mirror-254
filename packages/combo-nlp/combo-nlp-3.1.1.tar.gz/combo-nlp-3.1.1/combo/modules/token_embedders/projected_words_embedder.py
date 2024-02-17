from typing import Optional

import torch
from overrides import overrides

from combo.config import Registry
from combo.config.from_parameters import register_arguments
from combo.data.vocabulary import Vocabulary
from combo.modules.token_embedders.token_embedder import Embedding


@Registry.register("projected_words_embedder")
class ProjectedWordEmbedder(Embedding):
    """Word embeddings."""
    @register_arguments
    def __init__(self,
                 embedding_dim: int,
                 num_embeddings: int = None,
                 weight: torch.FloatTensor = None,
                 padding_index: int = None,
                 trainable: bool = True,
                 max_norm: float = None,
                 norm_type: float = 2.0,
                 scale_grad_by_freq: bool = False,
                 sparse: bool = False,
                 vocab_namespace: str = "tokens",
                 pretrained_file: str = None,
                 vocabulary: Vocabulary = None,
                 projection_layer: Optional["Linear"] = None): # Change to Optional[Linear]
        super().__init__(
            embedding_dim=embedding_dim,
            num_embeddings=num_embeddings,
            weight=weight,
            padding_index=padding_index,
            trainable=trainable,
            max_norm=max_norm,
            norm_type=norm_type,
            scale_grad_by_freq=scale_grad_by_freq,
            sparse=sparse,
            vocab_namespace=vocab_namespace,
            pretrained_file=pretrained_file,
            vocabulary=vocabulary
        )
        self._projection = projection_layer
        self.output_dim = embedding_dim if projection_layer is None else projection_layer.out_features

    @overrides
    def get_output_dim(self) -> int:
        return self.output_dim
