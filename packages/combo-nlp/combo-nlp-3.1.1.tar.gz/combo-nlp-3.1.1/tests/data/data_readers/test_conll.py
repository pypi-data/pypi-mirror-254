import unittest
import os

from combo.data import ConllDatasetReader


class ConllDatasetReaderTest(unittest.TestCase):
    def test_read_all_tokens(self):
        reader = ConllDatasetReader(coding_scheme='IOB2')
        tokens = [token for token in reader.read(os.path.join(os.path.dirname(__file__), 'conll_test_file.txt'))]
        self.assertEqual(len(tokens), 6)

    def test_tokenize_correct_tokens(self):
        reader = ConllDatasetReader(coding_scheme='IOB2')
        token = next(iter(reader.read(os.path.join(os.path.dirname(__file__), 'conll_test_file.txt'))))
        self.assertListEqual([str(t) for t in token['tokens'].tokens],
                             ['SOCCER', '-', 'JAPAN', 'GET', 'LUCKY', 'WIN', ',',
                              'CHINA', 'IN', 'SURPRISE', 'DEFEAT', '.'])

    def test_tokenize_correct_tags(self):
        reader = ConllDatasetReader(coding_scheme='IOB2')
        token = next(iter(reader.read(os.path.join(os.path.dirname(__file__), 'conll_test_file.txt'))))
        self.assertListEqual(token['tags'].labels,
                             ['O', 'O', 'B-LOC', 'O', 'O', 'O', 'O',
                              'B-PER', 'O', 'O', 'O', 'O'])
