"""Sampler tests."""
import unittest

from combo.data import TokenCountBatchSampler, Instance
from combo.data.fields.text_field import TextField
from combo.data.tokenizers import Token


class TokenCountBatchSamplerTest(unittest.TestCase):

    def setUp(self) -> None:
        self.dataset = []
        self.sentences = ["First sentence makes full batch.", "Short", "This ends first batch"]
        for sentence in self.sentences:
            tokens = [Token(t)
                      for t in sentence.split()]
            text_field = TextField(tokens, {})
            self.dataset.append(Instance({"sentence": text_field}))

    def test_batches(self):
        # given
        sampler = TokenCountBatchSampler(self.dataset, word_batch_size=2, shuffle_dataset=False)

        # when
        length = len(sampler)
        values = list(sampler)

        # then
        self.assertEqual(2, length)
        # sort by lengths + word_batch_size makes 1, 2 first batch
        self.assertListEqual([[1, 2], [0]], values)
