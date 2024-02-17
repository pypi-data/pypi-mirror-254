import unittest
import os

from combo.data.dataset_readers import TextClassificationJSONReader
from combo.data.fields import LabelField, ListField


class TextClassificationJSONReaderTest(unittest.TestCase):
    def test_read_two_tokens(self):
        reader = TextClassificationJSONReader()
        tokens = [token for token in reader.read(os.path.join(os.path.dirname(__file__), 'text_classification_json_reader.json'))]
        self.assertEqual(len(tokens), 2)

    def test_read_two_examples_fields_without_sentence_splitting(self):
        reader = TextClassificationJSONReader()
        tokens = [token for token in reader.read(os.path.join(os.path.dirname(__file__), 'text_classification_json_reader.json'))]
        self.assertEqual(len(tokens[0].fields.items()), 2)
        self.assertIsInstance(tokens[0].fields.get('label'), LabelField)
        self.assertEqual(tokens[0].fields.get('label').label, 'label1')
        self.assertEqual(len(tokens[1].fields.items()), 2)
        self.assertIsInstance(tokens[1].fields.get('label'), LabelField)
        self.assertEqual(tokens[1].fields.get('label').label, 'label2')

    def test_read_two_examples_tokens_with_sentence_splitting(self):
        reader = TextClassificationJSONReader()
        tokens = [token for token in reader.read(os.path.join(os.path.dirname(__file__), 'text_classification_json_reader.json'))]
        self.assertEqual(len(tokens[0].fields.items()), 2)
        self.assertIsInstance(tokens[0].fields.get('tokens'), ListField)
        self.assertEqual(len(tokens[0].fields.get('tokens').field_list), 2)
        self.assertEqual(len(tokens[1].fields.items()), 2)
        self.assertIsInstance(tokens[1].fields.get('tokens'), ListField)
        self.assertEqual(len(tokens[1].fields.get('tokens').field_list), 1)
