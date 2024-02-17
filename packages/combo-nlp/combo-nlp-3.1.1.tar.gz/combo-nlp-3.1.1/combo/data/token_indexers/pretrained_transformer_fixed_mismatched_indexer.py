"""
Adapted from COMBO
Authors: Mateusz Klimaszewski, Lukasz Pszenny
"""
import warnings
from typing import Optional, Dict, Any

from overrides import overrides

from combo.config import Registry
from combo.config.from_parameters import register_arguments
from combo.data import Vocabulary
from combo.data.token_indexers import IndexedTokenList
from combo.data.token_indexers.pretrained_transformer_indexer import PretrainedTransformerIndexer
from combo.data.token_indexers.pretrained_transformer_mismatched_indexer import PretrainedTransformerMismatchedIndexer


@Registry.register('pretrained_transformer_mismatched_fixed_token_indexer')
class PretrainedTransformerFixedMismatchedIndexer(PretrainedTransformerMismatchedIndexer):
    @register_arguments
    def __init__(self, model_name: str, namespace: str = "tags", max_length: int = None,
                 tokenizer_kwargs: Optional[Dict[str, Any]] = None, **kwargs) -> None:
        # The matched version v.s. mismatched
        super().__init__(model_name, namespace, max_length, tokenizer_kwargs, **kwargs)
        self._matched_indexer = PretrainedTransformerIndexer(
            model_name,
            namespace=namespace,
            max_length=max_length,
            tokenizer_kwargs=tokenizer_kwargs,
            **kwargs,
        )
        self._allennlp_tokenizer = self._matched_indexer._allennlp_tokenizer
        self._tokenizer = self._matched_indexer._tokenizer
        self._num_added_start_tokens = self._matched_indexer._num_added_start_tokens
        self._num_added_end_tokens = self._matched_indexer._num_added_end_tokens
        self._max_length = max_length or self._tokenizer.max_len_single_sentence
        if self._max_length <= 0:
            raise ValueError('Maximum sentence length must be larger than 0.')

    @overrides
    def tokens_to_indices(self,
                          tokens,
                          vocabulary: Vocabulary) -> IndexedTokenList:
        """
        Method is overridden in order to raise an error while the number of tokens needed to embed a sentence exceeds the
        maximal input of a model.
        """
        self._matched_indexer._add_encoding_to_vocabulary_if_needed(vocabulary)

        wordpieces, offsets = self._allennlp_tokenizer.intra_word_tokenize(
            [t.ensure_text() for t in tokens])

        if len(wordpieces) > self._max_length:
            warnings.warn("Following sentence consists of more wordpiece tokens that the model can process:\n" +\
                             " ".join([str(x) for x in tokens[:10]]) + " ... \n" + \
                             f"Maximal input: {self._max_length}\n"+ \
                             f"Current input: {len(wordpieces)}")

            tokens_chunk_len = self._max_length
            start_ind = 0
            wordpieces = []
            offsets = []

            while start_ind < len(tokens):
                tokens_chunk = tokens[start_ind:min(start_ind+tokens_chunk_len, len(tokens))]
                _wordpieces, _offsets = self._allennlp_tokenizer.intra_word_tokenize([t.ensure_text() for t in tokens_chunk])
                wordpieces += _wordpieces
                offset_len = offsets[-1][1] if start_ind > 0 else 0
                offsets += [(o[0]+offset_len, o[1]+offset_len) for o in _offsets]
                start_ind += tokens_chunk_len

        offsets = [x if x is not None else (-1, -1) for x in offsets]

        output: IndexedTokenList = {
            "token_ids": [t.text_id for t in wordpieces],
            "mask": [True] * len(tokens),  # for original tokens (i.e. word-level)
            "type_ids": [t.type_id for t in wordpieces],
            "offsets": offsets,
            "wordpiece_mask": [True] * len(wordpieces),  # for wordpieces (i.e. subword-level)
        }

        return self._matched_indexer._postprocess_output(output)
