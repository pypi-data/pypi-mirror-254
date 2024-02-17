import os
import unittest
from tempfile import TemporaryDirectory
import importlib.resources

from combo.combo_model import ComboModel
from combo.data.vocabulary import Vocabulary
from combo.default_model import default_model
from combo.modules import archive

TEMP_FILE_PATH = 'temp_serialization_dir'
test_file_path_str = str(importlib.resources.files('tests').joinpath('test_fixtures'))

def _test_vocabulary() -> Vocabulary:
    return Vocabulary.from_files(os.path.normpath(os.path.join(test_file_path_str, 'train_vocabulary')),
                                 oov_token='_', padding_token='__PAD__')


class ArchivalTest(unittest.TestCase):
    def test_serialize_model(self):
        vocabulary = _test_vocabulary()
        model = default_model('bert-base-cased', vocabulary)
        t = '.'
        with TemporaryDirectory(TEMP_FILE_PATH) as t:
            archive(model, t)
            loaded_model = ComboModel.from_archive(os.path.join(t, 'model.tar.gz'))
        self.assertDictEqual(loaded_model.serialize(['vocabulary']), model.serialize(['vocabulary']))
