import unittest

from combo.data import LamboTokenizer


class LamboTokenizerTest(unittest.TestCase):

    def setUp(self) -> None:
        self.lambo_tokenizer = LamboTokenizer()

    def test_tokenize_sentence(self):
        sentences = self.lambo_tokenizer.tokenize('Hello cats. I love you')
        self.assertListEqual([t.text for t in sentences[0] + sentences[1]],
                             ['Hello', 'cats', '.', 'I', 'love', 'you'])

    def test_segment_text(self):
        tokens = self.lambo_tokenizer.segment('Hello cats. I love you.\n\nHi.')
        self.assertListEqual(tokens,
                             [['Hello', 'cats', '.'], ['I', 'love', 'you', '.'], ['Hi', '.']])

    def test_segment_text_with_turns(self):
        tokens = self.lambo_tokenizer.segment('Hello cats. I love you.\n\nHi.', turns=True)
        self.assertListEqual(tokens,
                             [['Hello', 'cats', '.', 'I', 'love', 'you', '.'], ['Hi', '.']])

    def test_segment_text_with_multiwords(self):
        tokens = self.lambo_tokenizer.segment('I don\'t want a pizza.', split_subwords=True)
        self.assertListEqual(tokens,
                             [['I', 'do', 'n\'t', 'want', 'a', 'pizza', '.']])

    def test_segment_text_with_multiwords_without_splitting(self):
        tokens = self.lambo_tokenizer.tokenize('I don\'t want a pizza.', split_subwords=False)
        self.assertListEqual([t.text for t in tokens[0]],
                             ['I', 'don\'t', 'want', 'a', 'pizza', '.'])
        self.assertListEqual([t.subwords for t in tokens[0]],
                             [[], ['do', 'n\'t'], [], [], [], []])

    def test_segment_text_with_multiwords_with_splitting(self):
        tokens = self.lambo_tokenizer.tokenize('I don\'t want a pizza.', split_subwords=True)
        self.assertListEqual([t.text for t in tokens[0]],
                             ['I', 'do', 'n\'t', 'want', 'a', 'pizza', '.'])
        self.assertListEqual([t.multiword for t in tokens[0]],
                             [None, ('don\'t', (2, 3)), ('don\'t', (2, 3)), None, None, None, None])

