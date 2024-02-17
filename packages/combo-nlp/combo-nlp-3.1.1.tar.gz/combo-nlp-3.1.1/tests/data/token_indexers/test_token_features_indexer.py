import unittest
import os
import importlib.resources

from combo.data.tokenizers import Token
from combo.data.token_indexers import TokenFeatsIndexer
from combo.data.vocabulary import Vocabulary

test_file_path_str = str(importlib.resources.files('tests').joinpath('test_fixtures'))

class TokenFeatsIndexerTest(unittest.TestCase):

    def setUp(self):
        self.vocabulary = Vocabulary.from_files(
            os.path.join(test_file_path_str, 'train_vocabulary'),
            oov_token='_',
            padding_token='__PAD__'
        )
        self.token_feats_indexer = TokenFeatsIndexer()

    def test_get_index_to_token(self):
        token = Token(idx=0, text='a', feats={'Mood': 'Ind'})
        counter = {'feats_labels': {'Mood=Ind': 0}}
        self.token_feats_indexer.count_vocab_items(token, counter)
        self.assertEqual(counter['feats_labels']['Mood=Ind'], 1)

    def test_tokens_to_indices(self):
        self.assertEqual(
            self.token_feats_indexer.tokens_to_indices(
                [Token(idx=0, text='a', feats={'Mood': 'Ind'})], self.vocabulary),
            {'tokens': [[11]+[0]*173]})

    def test_get_padding_lengths(self):
        self.assertEqual(
            self.token_feats_indexer.get_padding_lengths({'tokens': [[11]+[0]*173]}),
            {'tokens': 1}
        )

    def test_get_nondefault_padding_lengths(self):
        token_feats_indexer_w_padding = TokenFeatsIndexer(token_min_padding_length=4)
        self.assertEqual(
            token_feats_indexer_w_padding.get_padding_lengths({'tokens': [[11]+[0]*173]}),
            {'tokens': 4}
        )

    def test_tokens_to_indices_as_padded_tensor(self):
        token_feats_indexer_w_padding = TokenFeatsIndexer(token_min_padding_length=4)
        token = Token(idx=0, text='a', feats={'Mood': 'Ind'})
        indices_dict = token_feats_indexer_w_padding.tokens_to_indices([token], self.vocabulary)
        padded_dict = list(token_feats_indexer_w_padding.as_padded_tensor_dict(
            indices_dict,
            token_feats_indexer_w_padding.get_padding_lengths(indices_dict)
        )['tokens'].numpy()[0])
        self.assertListEqual(padded_dict, [11]+[0]*173)
