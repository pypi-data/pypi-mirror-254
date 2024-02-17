import unittest
import os

from combo.data import UniversalDependenciesDatasetReader


class UniversalDependenciesDatasetReaderTest(unittest.TestCase):
    def test_read_all_tokens(self):
        t = UniversalDependenciesDatasetReader()
        tokens = [token for token in t.read(os.path.join(os.path.dirname(__file__), 'en_test.conllu'))]
        self.assertEqual(len(tokens), 5)

    def test_read_text(self):
        t = UniversalDependenciesDatasetReader()
        token = next(iter(t.read(os.path.join(os.path.dirname(__file__), 'en_test.conllu'))))
        self.assertListEqual([t.text for t in token['sentence'].tokens],
                             ['What', 'if', 'Google', 'Morphed', 'Into', 'GoogleOS', '?'])

    def test_read_deprel(self):
        t = UniversalDependenciesDatasetReader()
        token = next(iter(t.read(os.path.join(os.path.dirname(__file__), 'en_test.conllu'))))
        self.assertListEqual(token['deprel'].labels,
                             ['root', 'mark', 'nsubj', 'advcl', 'case', 'obl', 'punct'])

    def test_read_upostag(self):
        t = UniversalDependenciesDatasetReader()
        token = next(iter(t.read(os.path.join(os.path.dirname(__file__), 'en_test.conllu'))))
        self.assertListEqual(token['upostag'].labels,
                             ['PRON', 'SCONJ', 'PROPN', 'VERB', 'ADP', 'PROPN', 'PUNCT'])

