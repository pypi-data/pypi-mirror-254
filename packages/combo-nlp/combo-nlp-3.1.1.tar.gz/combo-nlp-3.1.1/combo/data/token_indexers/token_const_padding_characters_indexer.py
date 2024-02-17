"""
Custom character token indexer.
Adapted from COMBO.
Author: Mateusz Klimaszewski
"""
import itertools
from typing import List, Dict

import torch
from overrides import overrides

from combo.config import Registry
from combo.config.from_parameters import register_arguments
from combo.data.token_indexers import IndexedTokenList
from combo.data.token_indexers.token_characters_indexer import TokenCharactersIndexer
from combo.data.tokenizers import CharacterTokenizer
from combo.utils import pad_sequence_to_length


@Registry.register('characters_const_padding_token_indexer')
class TokenConstPaddingCharactersIndexer(TokenCharactersIndexer):
    """Wrapper around allennlp token indexer with const padding."""

    @register_arguments
    def __init__(self,
                 namespace: str = "token_characters",
                 tokenizer: CharacterTokenizer = CharacterTokenizer(),
                 start_tokens: List[str] = None,
                 end_tokens: List[str] = None,
                 min_padding_length: int = 0,
                 token_min_padding_length: int = 0):
        super().__init__(namespace, tokenizer, start_tokens, end_tokens, min_padding_length,
                         token_min_padding_length)

    @overrides
    def get_padding_lengths(self, indexed_tokens: IndexedTokenList) -> Dict[str, int]:
        padding_lengths = {"token_characters": len(indexed_tokens["token_characters"]),
                           "num_token_characters": self._min_padding_length}
        return padding_lengths

    @overrides
    def as_padded_tensor_dict(
            self, tokens: IndexedTokenList, padding_lengths: Dict[str, int]
    ) -> Dict[str, torch.Tensor]:
        # Pad the tokens.
        padded_tokens = pad_sequence_to_length(
            tokens["token_characters"],
            padding_lengths["token_characters"],
            default_value=lambda: [],
        )

        # Pad the characters within the tokens.
        desired_token_length = padding_lengths["num_token_characters"]
        longest_token: List[int] = max(tokens["token_characters"], key=len, default=[])  # type: ignore
        padding_value = 0
        if desired_token_length > len(longest_token):
            # Since we want to pad to greater than the longest token, we add a
            # "dummy token" so we can take advantage of the fast implementation of itertools.zip_longest.
            padded_tokens.append([padding_value] * desired_token_length)
        # pad the list of lists to the longest sublist, appending 0's
        padded_tokens = list(zip(*itertools.zip_longest(*padded_tokens, fillvalue=padding_value)))
        if desired_token_length > len(longest_token):
            # Removes the "dummy token".
            padded_tokens.pop()
        # Truncates all the tokens to the desired length, and return the result.
        return {
            "token_characters": torch.LongTensor(
                [list(token[:desired_token_length]) for token in padded_tokens]
            )
        }
