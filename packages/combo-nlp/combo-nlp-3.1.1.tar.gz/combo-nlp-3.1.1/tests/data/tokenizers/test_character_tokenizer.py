import unittest

from combo.data import CharacterTokenizer


class CharacterTokenizerText(unittest.TestCase):

    def setUp(self) -> None:
        self.character_tokenizer = CharacterTokenizer()

    def test_tokenize_sentence(self):
        tokens = self.character_tokenizer.tokenize('I love you!')
        self.assertListEqual([t.text for t in tokens],
                             ['I', ' ', 'l', 'o', 'v', 'e', ' ', 'y', 'o', 'u', '!'])

    def test_tokenize_sentence_with_start_tokens(self):
        tokenizer_w_start_tokens = CharacterTokenizer(start_tokens=['@'])
        tokens = tokenizer_w_start_tokens.tokenize('Hi! Hello.')
        self.assertListEqual([t.text for t in tokens],
                             ['@', 'H', 'i', '!', ' ', 'H', 'e', 'l', 'l', 'o', '.'])
        self.assertEqual(tokens[0].idx, 0)
        self.assertTrue([t.idx > 0 for t in tokens if t.idx is not None])

    def test_tokenize_sentence_with_end_tokens(self):
        tokenizer_w_end_tokens = CharacterTokenizer(end_tokens=['#'])
        tokens = tokenizer_w_end_tokens.tokenize('Hi! Hello.')
        self.assertListEqual([t.text for t in tokens],
                             ['H', 'i', '!', ' ', 'H', 'e', 'l', 'l', 'o', '.', '#'])
        self.assertEqual(tokens[-1].idx, 0)
        self.assertTrue([t.idx > 0 for t in tokens if t.idx is not None])

    def test_tokenize_empty_sentence(self):
        tokens = self.character_tokenizer.tokenize('')
        self.assertEqual(len(tokens), 0)
