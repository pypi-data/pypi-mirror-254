import unittest
import os
import importlib.resources

from combo.data.tokenizers import Token
from combo.data.token_indexers import TokenCharactersIndexer
from combo.data.vocabulary import Vocabulary

test_file_path_str = str(importlib.resources.files('tests').joinpath('test_fixtures'))

class TokenCharactersIndexerTest(unittest.TestCase):

    def setUp(self):
        self.vocabulary = Vocabulary.from_files(
            os.path.normpath(os.path.join(test_file_path_str, 'train_vocabulary')),
            oov_token='_',
            padding_token='__PAD__'
        )
        self.token_characters_indexer = TokenCharactersIndexer()

    def test_get_index_to_token(self):
        token = Token(idx=0, text='a')
        counter = {'token_characters': {'a': 0}}
        self.token_characters_indexer.count_vocab_items(token, counter)
        self.assertEqual(counter['token_characters']['a'], 1)

    def test_tokens_to_indices(self):
        self.assertEqual(
            self.token_characters_indexer.tokens_to_indices(
                [Token('za')], self.vocabulary),
            {'token_characters': [[8, 4]]})

    def test_get_padding_lengths(self):
        self.assertEqual(
            self.token_characters_indexer.get_padding_lengths({'token_characters': [[11, 4]]}),
            {'num_token_characters': 2, 'token_characters': 1}
        )

    def test_get_nondefault_padding_lengths(self):
        token_characters_indexer_w_padding = TokenCharactersIndexer(min_padding_length=4)
        self.assertEqual(
            token_characters_indexer_w_padding.get_padding_lengths({'token_characters': [[11, 4]]}),
            {'num_token_characters': 4, 'token_characters': 1}
        )

    def test_tokens_to_indices_as_padded_tensor(self):
        token_characters_indexer_w_padding = TokenCharactersIndexer(min_padding_length=4)
        indices_dict = token_characters_indexer_w_padding.tokens_to_indices([Token('wa')], self.vocabulary)
        padded_dict = list(token_characters_indexer_w_padding.as_padded_tensor_dict(
            indices_dict,
            token_characters_indexer_w_padding.get_padding_lengths(indices_dict)
        )['token_characters'].numpy()[0])
        self.assertListEqual(padded_dict,[11, 4, 0, 0])
