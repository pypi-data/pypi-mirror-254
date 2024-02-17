"""Features indexer.
Adapted from COMBO.
Author: Mateusz Klimaszewski
"""
import collections
from typing import List, Dict

import torch
from overrides import overrides

from combo.config import Registry
from combo.config.from_parameters import register_arguments
from combo.data.tokenizers.tokenizer import Token
from combo.data.token_indexers.token_indexer import TokenIndexer, IndexedTokenList
from combo.utils import pad_sequence_to_length


@Registry.register('feats_indexer')
class TokenFeatsIndexer(TokenIndexer):
    @register_arguments
    def __init__(
            self,
            namespace: str = "feats_labels",
            feature_name: str = "feats",
            token_min_padding_length: int = 0,
    ) -> None:
        super().__init__(token_min_padding_length)
        self.namespace = namespace
        self._feature_name = feature_name

    @overrides
    def count_vocab_items(self, token: Token, counter: Dict[str, Dict[str, int]]):
        feats = self._feat_values(token)
        for feat in feats:
            counter[self.namespace][feat] += 1

    @overrides
    def tokens_to_indices(self, tokens: List[Token], vocabulary) -> IndexedTokenList:
        indices: List[List[int]] = []
        vocab_size = vocabulary.get_vocab_size(self.namespace)
        for token in tokens:
            token_indices = []
            feats = self._feat_values(token)
            for feat in feats:
                token_indices.append(vocabulary.get_token_index(feat, self.namespace))
            indices.append(pad_sequence_to_length(token_indices, vocab_size))
        return {"tokens": indices}

    @overrides
    def get_empty_token_list(self) -> IndexedTokenList:
        return {"tokens": [[]]}

    def _feat_values(self, token):
        feats = getattr(token, self._feature_name)
        if feats is None:
            feats = collections.OrderedDict()
        features = []
        for feat, value in feats.items():
            if feat in ["_", "__ROOT__"]:
                pass
            else:
                # Handle case where feature is binary (doesn't have associated value)
                if value:
                    features.append(feat + "=" + value)
                else:
                    features.append(feat)
        return features

    @overrides
    def as_padded_tensor_dict(
            self, tokens: IndexedTokenList, padding_lengths: Dict[str, int]
    ) -> Dict[str, torch.Tensor]:
        tensor_dict = {}
        for key, val in tokens.items():
            vocab_size = len(val[0])
            tensor = torch.tensor(pad_sequence_to_length(val,
                                                         padding_lengths[key],
                                                         default_value=lambda: [0] * vocab_size,
                                                         )
                                  )
            tensor_dict[key] = tensor
        return tensor_dict

