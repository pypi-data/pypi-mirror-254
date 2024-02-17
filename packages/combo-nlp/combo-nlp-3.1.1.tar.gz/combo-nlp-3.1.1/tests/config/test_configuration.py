import unittest
import os
import importlib.resources

from combo.config import Registry
from combo.config.from_parameters import override_parameters
from combo.data import WhitespaceTokenizer, UniversalDependenciesDatasetReader, Vocabulary
from combo.data.token_indexers.token_characters_indexer import TokenCharactersIndexer

test_file_path_str = str(importlib.resources.files('tests').joinpath('test_fixtures'))
VOCABULARY_DIR = os.path.normpath(os.path.join(test_file_path_str, 'small_vocabulary'))


class ConfigurationTest(unittest.TestCase):

    def test_dataset_reader_from_registry(self):
        dr_type, constructor = Registry.resolve('conllu_dataset_reader')
        dataset_reader = dr_type.from_parameters()
        self.assertEqual(type(dataset_reader), UniversalDependenciesDatasetReader)

    def test_dataset_reader_from_registry_with_parameters(self):
        parameters = {'token_indexers': {'char': {'type': 'token_characters_indexer'}},
                      'use_sem': True}
        dr_type, constructor = Registry.resolve('conllu_dataset_reader')
        dataset_reader = dr_type.from_parameters(parameters, constructor)
        self.assertEqual(type(dataset_reader), UniversalDependenciesDatasetReader)
        self.assertEqual(type(dataset_reader.token_indexers['char']), TokenCharactersIndexer)
        self.assertEqual(dataset_reader.use_sem, True)

    def test_dataset_reader_from_registry_with_token_indexer_parameters(self):
        parameters = {'token_indexers': {'char': {'type': 'token_characters_indexer',
                                                  'parameters': {
                                                      'namespace': 'custom_namespace',
                                                      'tokenizer': {
                                                          'type': 'whitespace_tokenizer'
                                                      }
                                                  }}}}
        dr_type, constructor = Registry.resolve('conllu_dataset_reader')
        dataset_reader = dr_type.from_parameters(parameters)
        self.assertEqual(type(dataset_reader), UniversalDependenciesDatasetReader)
        self.assertEqual(dataset_reader.token_indexers['char']._namespace, 'custom_namespace')
        self.assertEqual(type(dataset_reader.token_indexers['char']._character_tokenizer), WhitespaceTokenizer)

    def test_vocabulary_from_files(self):
        parameters = {'type': 'from_files_vocabulary',
                      'parameters': {
                          'directory': VOCABULARY_DIR
                      }}
        vocab_type, constructor = Registry.resolve(parameters['type'])
        vocab = vocab_type.from_parameters(parameters['parameters'], constructor)
        self.assertEqual(type(vocab), Vocabulary)
        self.assertEqual(vocab.constructed_from, 'from_files')
        self.assertSetEqual(vocab.get_namespaces(), {'animals'})

    def test_serialize(self):
        vocab = Vocabulary({'counter': {'test': 0}}, max_vocab_size=10)
        self.assertDictEqual(vocab.serialize(),
                             {
                                 'type': 'base_vocabulary',
                                 'parameters': {
                                     'counter': {'counter': {'test': 0}},
                                     'max_vocab_size': 10
                                 }
                             })

    def test_serialize_non_base_constructor(self):
        vocab = Vocabulary.from_files(VOCABULARY_DIR)
        self.assertDictEqual(vocab.serialize(),
                             {
                                 'type': 'from_files_vocabulary',
                                 'parameters': {
                                     'directory': 'small_vocabulary',
                                     'oov_token': '@@UNKNOWN@@',
                                     'padding_token': '@@PADDING@@'
                                 }
                             })

    def test_serialize_and_load_non_base_constructor(self):
        vocab = Vocabulary.from_files(VOCABULARY_DIR)
        serialized_vocab = vocab.serialize()
        serialized_vocab['parameters']['directory'] = VOCABULARY_DIR
        clz, constructor = Registry.resolve(serialized_vocab['type'])
        reconstructed_vocab = clz.from_parameters(serialized_vocab['parameters'], constructor)
        self.assertEqual(type(reconstructed_vocab), Vocabulary)
        self.assertEqual(reconstructed_vocab.constructed_from, 'from_files')
        self.assertSetEqual(reconstructed_vocab.get_namespaces(), {'animals'})


    def test_override_parameters(self):
        parameters = {
            'type': 'base_vocabulary',
            'parameters': {
                'counter': {'counter': {'test': 0}},
                'max_vocab_size': 10
            }
        }

        to_override = {'parameters': {'max_vocab_size': 15}}

        self.assertDictEqual({
            'type': 'base_vocabulary',
            'parameters': {
                'counter': {'counter': {'test': 0}},
                'max_vocab_size': 15
            }
        }, override_parameters(parameters, to_override))

    def test_override_nested_parameters(self):
        parameters = {
            'type': 'base_vocabulary',
            'parameters': {
                'counter': {'counter': {'test': 0}, 'another_property': 0},
                'another_counter': {'counter': {'test': 0}, 'another_property': 0}
            }
        }

        to_override = {'parameters': {'another_counter': {'counter': {'test': 1}}}}

        self.assertDictEqual({
            'type': 'base_vocabulary',
            'parameters': {
                'counter': {'counter': {'test': 0}, 'another_property': 0},
                'another_counter': {'counter': {'test': 1}, 'another_property': 0}
            }
        }, override_parameters(parameters, to_override))

    def test_override_parameters_no_change(self):
        parameters = {
            'type': 'base_vocabulary',
            'parameters': {
                'counter': {'counter': {'test': 0}},
                'max_vocab_size': 10
            }
        }

        to_override = {}

        self.assertDictEqual({
            'type': 'base_vocabulary',
            'parameters': {
                'counter': {'counter': {'test': 0}},
                'max_vocab_size': 10
            }
        }, override_parameters(parameters, to_override))
