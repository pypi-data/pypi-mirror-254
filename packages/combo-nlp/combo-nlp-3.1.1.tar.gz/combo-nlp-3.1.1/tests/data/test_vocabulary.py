import unittest

from combo.data.vocabulary import match_namespace, Vocabulary


class VocabularyTest(unittest.TestCase):

    def test_match_namespace(self):
        self.assertTrue(match_namespace('*labels', 'test_labels'))

    def test_dont_match_namespace(self):
        self.assertFalse(match_namespace('*labels', 'test_something'))

    def test_default_non_padded_namespace(self):
        v = Vocabulary()
        self.assertFalse(v.is_padded('test_labels'))

    def test_empty_padded_namespace_is_padded(self):
        padded_namespaces = ['padded_example']
        non_padded_namespaces = ['non_padded_example']
        v = Vocabulary(non_padded_namespaces=non_padded_namespaces)
        self.assertTrue(v.is_padded('padded_example'))

    def test_empty_non_padded_namespace_is_not_padded(self):
        padded_namespaces = ['padded_example']
        non_padded_namespaces = ['non_padded_example']
        v = Vocabulary(non_padded_namespaces=non_padded_namespaces)
        self.assertFalse(v.is_padded('non_padded_example'))

    def test_add_token_to_padded_namespace_correct_vocab_size(self):
        padded_namespaces = ['padded_example']
        non_padded_namespaces = ['non_padded_example']
        v = Vocabulary(non_padded_namespaces=non_padded_namespaces)
        v.add_token_to_namespace('test_token', 'padded_example')
        self.assertEqual(v.get_vocab_size('padded_example'), 3)

    def test_add_token_to_padded_namespace_correct_token_index(self):
        padded_namespaces = ['padded_example']
        non_padded_namespaces = ['non_padded_example']
        v = Vocabulary(non_padded_namespaces=non_padded_namespaces)
        v.add_token_to_namespace('test_token', 'padded_example')
        self.assertEqual(v.get_token_index('test_token', 'padded_example'), 2)

    def test_add_token_to_padded_namespace_correct_token_for_index(self):
        padded_namespaces = ['padded_example']
        non_padded_namespaces = ['non_padded_example']
        v = Vocabulary(non_padded_namespaces=non_padded_namespaces)
        v.add_token_to_namespace('test_token', 'padded_example')
        self.assertEqual(v.get_token_from_index(2, 'padded_example'), 'test_token')

    def test_add_tokens_to_padded_namespace_correct_vocab_size(self):
        padded_namespaces = ['padded_example']
        non_padded_namespaces = ['non_padded_example']
        v = Vocabulary(non_padded_namespaces=non_padded_namespaces)
        v.add_tokens_to_namespace(['test_token1', 'test_token2'], 'padded_example')
        self.assertEqual(v.get_vocab_size('padded_example'), 4)

    def test_add_tokens_to_padded_namespace_correct_token_index(self):
        padded_namespaces = ['padded_example']
        non_padded_namespaces = ['non_padded_example']
        v = Vocabulary(non_padded_namespaces=non_padded_namespaces)
        v.add_tokens_to_namespace(['test_token1', 'test_token2'], 'padded_example')
        self.assertEqual(v.get_token_index('test_token1', 'padded_example'), 2)
        self.assertEqual(v.get_token_index('test_token2', 'padded_example'), 3)

    def test_add_tokens_to_padded_namespace_correct_token_for_index(self):
        padded_namespaces = ['padded_example']
        non_padded_namespaces = ['non_padded_example']
        v = Vocabulary(non_padded_namespaces=non_padded_namespaces)
        v.add_tokens_to_namespace(['test_token1', 'test_token2'], 'padded_example')
        self.assertEqual(v.get_token_from_index(2, 'padded_example'), 'test_token1')
        self.assertEqual(v.get_token_from_index(3, 'padded_example'), 'test_token2')


    def test_add_tokens_to_padded_namespace_correct_index_to_token_dict(self):
        padded_namespaces = ['padded_example']
        non_padded_namespaces = ['non_padded_example']
        v = Vocabulary(non_padded_namespaces=non_padded_namespaces)
        v.add_tokens_to_namespace(['test_token1', 'test_token2'], 'padded_example')
        self.assertEqual(v.get_index_to_token_vocabulary('padded_example'),
                         {0: '@@PADDING@@',
                          1: '@@UNKNOWN@@',
                          2: 'test_token1',
                          3: 'test_token2'})

    def test_add_tokens_to_padded_namespace_correct_token_to_index_dict(self):
        padded_namespaces = ['padded_example']
        non_padded_namespaces = ['non_padded_example']
        v = Vocabulary(non_padded_namespaces=non_padded_namespaces)
        v.add_tokens_to_namespace(['test_token1', 'test_token2'], 'padded_example')
        self.assertEqual(v.get_token_to_index_vocabulary('padded_example'),
                         {'@@PADDING@@': 0,
                          '@@UNKNOWN@@': 1,
                          'test_token1': 2,
                          'test_token2': 3})

    def test_add_token_to_non_padded_namespace_correct_vocab_size(self):
        padded_namespaces = ['padded_example']
        non_padded_namespaces = ['non_padded_example']
        v = Vocabulary(non_padded_namespaces=non_padded_namespaces)
        v.add_token_to_namespace('test_token', 'non_padded_example')
        self.assertEqual(v.get_vocab_size('non_padded_example'), 1)

    def test_add_token_to_non_padded_namespace_correct_token_index(self):
        padded_namespaces = ['padded_example']
        non_padded_namespaces = ['non_padded_example']
        v = Vocabulary(non_padded_namespaces=non_padded_namespaces)
        v.add_token_to_namespace('test_token', 'non_padded_example')
        self.assertEqual(v.get_token_index('test_token', 'non_padded_example'), 0)

    def test_add_token_to_non_padded_namespace_correct_token_for_index(self):
        padded_namespaces = ['padded_example']
        non_padded_namespaces = ['non_padded_example']
        v = Vocabulary(non_padded_namespaces=non_padded_namespaces)
        v.add_token_to_namespace('test_token', 'non_padded_example')
        self.assertEqual(v.get_token_from_index(0, 'non_padded_example'), 'test_token')

    def test_add_tokens_to_non_padded_namespace_correct_vocab_size(self):
        padded_namespaces = ['padded_example']
        non_padded_namespaces = ['non_padded_example']
        v = Vocabulary(non_padded_namespaces=non_padded_namespaces)
        v.add_tokens_to_namespace(['test_token1', 'test_token2'], 'non_padded_example')
        self.assertEqual(v.get_vocab_size('non_padded_example'), 2)

    def test_add_tokens_to_non_padded_namespace_correct_token_index(self):
        padded_namespaces = ['padded_example']
        non_padded_namespaces = ['non_padded_example']
        v = Vocabulary(non_padded_namespaces=non_padded_namespaces)
        v.add_tokens_to_namespace(['test_token1', 'test_token2'], 'non_padded_example')
        self.assertEqual(v.get_token_index('test_token1', 'non_padded_example'), 0)
        self.assertEqual(v.get_token_index('test_token2', 'non_padded_example'), 1)

    def test_add_tokens_to_non_padded_namespace_correct_token_for_index(self):
        padded_namespaces = ['padded_example']
        non_padded_namespaces = ['non_padded_example']
        v = Vocabulary(non_padded_namespaces=non_padded_namespaces)
        v.add_tokens_to_namespace(['test_token1', 'test_token2'], 'non_padded_example')
        self.assertEqual(v.get_token_from_index(0, 'non_padded_example'), 'test_token1')
        self.assertEqual(v.get_token_from_index(1, 'non_padded_example'), 'test_token2')

    def test_add_tokens_to_non_padded_namespace_correct_index_to_token_dict(self):
        padded_namespaces = ['padded_example']
        non_padded_namespaces = ['non_padded_example']
        v = Vocabulary(non_padded_namespaces=non_padded_namespaces)
        v.add_tokens_to_namespace(['test_token1', 'test_token2'], 'non_padded_example')
        self.assertEqual(v.get_index_to_token_vocabulary('non_padded_example'),
                         {0: 'test_token1',
                          1: 'test_token2'})

    def test_add_tokens_to_non_padded_namespace_correct_token_to_index_dict(self):
        padded_namespaces = ['padded_example']
        non_padded_namespaces = ['non_padded_example']
        v = Vocabulary(non_padded_namespaces=non_padded_namespaces)
        v.add_tokens_to_namespace(['test_token1', 'test_token2'], 'non_padded_example')
        self.assertEqual(v.get_token_to_index_vocabulary('non_padded_example'),
                         {'test_token1': 0,
                          'test_token2': 1})


if __name__ == '__main__':
    unittest.main()
