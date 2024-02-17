import unittest
import os
import importlib.resources

from combo.data.tokenizers import Token
from combo.data.token_indexers import PretrainedTransformerFixedMismatchedIndexer
from combo.data.vocabulary import Vocabulary

test_file_path_str = str(importlib.resources.files('tests').joinpath('test_fixtures'))

class TokenFeatsIndexerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.indexer = PretrainedTransformerFixedMismatchedIndexer("allegro/herbert-base-cased")
        self.short_indexer = PretrainedTransformerFixedMismatchedIndexer("allegro/herbert-base-cased",
                                                                         max_length=3)
        self.vocabulary = Vocabulary.from_files(
            os.path.join(test_file_path_str, 'train_vocabulary'),
            oov_token='_',
            padding_token='__PAD__'
        )

    def test_offsets(self):
        output1 = self.indexer.tokens_to_indices([
            Token('Hello'), Token(','), Token('my'), Token('friend'), Token('!'),
            Token('What'), Token('a'), Token('nice'), Token('day'), Token('!')
        ], self.vocabulary)
        output2 = self.short_indexer.tokens_to_indices([
            Token('Hello'), Token(','), Token('my'), Token('friend'), Token('!'),
            Token('What'), Token('a'), Token('nice'), Token('day'), Token('!')
        ], self.vocabulary)
        self.assertListEqual(output1['offsets'], output2['offsets'])
