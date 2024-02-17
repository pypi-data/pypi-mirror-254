import json
import logging
import os
import pathlib
import tempfile
from itertools import chain
from typing import Dict, Optional, Any, Tuple

import torch
from absl import app, flags
import pytorch_lightning as pl
from pytorch_lightning.loggers import TensorBoardLogger
from tqdm import tqdm

from combo.training.trainable_combo import TrainableCombo
from combo.utils import checks, ComboLogger

from combo.config import resolve
from combo.default_model import default_ud_dataset_reader, default_data_loader, default_model
from combo.modules.archival import load_archive, archive
from combo.predict import COMBO
from combo.data import api
from combo.config import override_parameters
from combo.data import LamboTokenizer, Vocabulary, DatasetReader
from combo.data.dataset_loaders import DataLoader
from combo.modules.model import Model
from combo.utils import ConfigurationError
from combo.utils.matrices import extract_combo_matrices

logging.setLoggerClass(ComboLogger)
logger = logging.getLogger(__name__)
_FEATURES = ["token", "char", "upostag", "xpostag", "lemma", "feats"]
_TARGETS = ["deprel", "feats", "head", "lemma", "upostag", "xpostag", "semrel", "sent", "deps"]


def handle_error(error: Exception, prefix: str):
    msg = getattr(error, 'message', str(error))
    logger.error(msg, prefix)


FLAGS = flags.FLAGS
flags.DEFINE_enum(name="mode", default=None, enum_values=["train", "predict"],
                  help="Specify COMBO mode: train or predict")

# Common flags
flags.DEFINE_integer(name="n_cuda_devices", default=-1,
                     help="Number of devices to train on (default -1 auto mode - train on as many as possible)")
flags.DEFINE_string(name="output_file", default="output.log",
                    help="Predictions result file.")

# Training flags
flags.DEFINE_string(name="training_data_path", default="", help="Training data path(s)")
flags.DEFINE_alias(name="training_data", original_name="training_data_path")
flags.DEFINE_string(name="validation_data_path", default="", help="Validation data path(s)")
flags.DEFINE_alias(name="validation_data", original_name="validation_data_path")
flags.DEFINE_string(name="vocabulary_path", default=None,
                    help="Stored vocabulary files. If not provided in training mode, vocabulary is built from training files")
flags.DEFINE_integer(name="lemmatizer_embedding_dim", default=300,
                     help="Lemmatizer embeddings dim")
flags.DEFINE_integer(name="num_epochs", default=400,
                     help="Epochs num")
flags.DEFINE_integer(name="batch_size", default=256,
                     help="Batch size")
flags.DEFINE_integer(name="batches_per_epoch", default=16,
                     help="Number of batches per epoch")
flags.DEFINE_string(name="pretrained_transformer_name", default="bert-base-cased",
                    help="Pretrained transformer model name (see transformers from HuggingFace library for list of "
                         "available models) for transformers based embeddings.")
flags.DEFINE_list(name="features", default=["token", "char"],
                  help=f"Features used to train model (required 'token' and 'char'). Possible values: {_FEATURES}.")
flags.DEFINE_list(name="targets", default=["deprel", "feats", "head", "lemma", "upostag", "xpostag"],
                  help=f"Targets of the model (required `deprel` and `head`). Possible values: {_TARGETS}.")
flags.DEFINE_string(name="serialization_dir", default=None,
                    help="Model serialization directory (default - system temp dir).")
flags.DEFINE_boolean(name="tensorboard", default=False,
                     help="When provided model will log tensorboard metrics.")
flags.DEFINE_string(name="tensorboard_name", default="combo",
                    help="Name of the model in TensorBoard logs.")
flags.DEFINE_string(name="config_path", default="",
                    help="Config file path.")
flags.DEFINE_list(name="datasets_for_vocabulary", default=["train"],
                  help="")
flags.DEFINE_boolean(name="turns", default=False,
                     help="Segment into sentences on sentence break or on turn break.")
flags.DEFINE_boolean(name="split_subwords", default=False,
                     help="Split subwords (e.g. don\'t = do, n\'t) into separate tokens.")

# Finetune after training flags
flags.DEFINE_string(name="finetuning_training_data_path", default="",
                    help="Training data path(s)")
flags.DEFINE_string(name="finetuning_validation_data_path", default="",
                    help="Validation data path(s)")

# Test after training flags
flags.DEFINE_string(name="test_data_path", default=None,
                    help="Test path file.")
flags.DEFINE_alias(name="test_data", original_name="test_data_path")
flags.DEFINE_boolean(name="use_pure_config", default=False,
                     help="Ignore ext flags.")

# Prediction flags
flags.DEFINE_string(name="model_path", default=None,
                    help="Pretrained model path.")
flags.DEFINE_string(name="input_file", default=None,
                    help="File to predict path")
flags.DEFINE_boolean(name="conllu_format", default=True,
                     help="Prediction based on conllu format (instead of raw text).")
flags.DEFINE_boolean(name="finetuning", default=False,
                     help="Finetuning mode for training.")
flags.DEFINE_string(name="tokenizer_language", default="English",
                    help="Tokenizer language.")
flags.DEFINE_boolean(name="save_matrices", default=True,
                     help="Save relation distribution matrices.")
flags.DEFINE_enum(name="predictor_name", default="combo-lambo",
                  enum_values=["combo", "combo-spacy", "combo-lambo"],
                  help="Use predictor with whitespace, spacy or lambo (recommended) tokenizer.")


def build_vocabulary_from_instances(training_data_loader: DataLoader,
                                    validation_data_loader: Optional[DataLoader],
                                    logging_prefix: str) -> Vocabulary:
    logger.info('Building a vocabulary from instances.', prefix=logging_prefix)
    if "train" in FLAGS.datasets_for_vocabulary and "valid" in FLAGS.datasets_for_vocabulary:
        instances = chain(training_data_loader.iter_instances(),
                          validation_data_loader.iter_instances()) \
            if validation_data_loader \
            else training_data_loader.iter_instances()
    elif "train" in FLAGS.datasets_for_vocabulary:
        instances = training_data_loader.iter_instances()
    elif "valid" in FLAGS.datasets_for_vocabulary:
        instances = validation_data_loader.iter_instances()
    else:
        logger.error("train and valid are the only allowed values for --datasets_for_vocabulary!",
                     prefix=logging_prefix)
        raise ValueError("train and valid are the only allowed values for --datasets_for_vocabulary!")
    vocabulary = Vocabulary.from_instances_extended(
        instances,
        non_padded_namespaces=['head_labels'],
        only_include_pretrained_words=False,
        oov_token='_',
        padding_token='__PAD__'
    )
    return vocabulary


def get_defaults(dataset_reader: Optional[DatasetReader],
                 training_data_loader: Optional[DataLoader],
                 validation_data_loader: Optional[DataLoader],
                 vocabulary: Optional[Vocabulary],
                 training_data_path: str,
                 validation_data_path: str,
                 prefix: str) -> Tuple[DatasetReader, DataLoader, DataLoader, Vocabulary]:
    if not dataset_reader and (FLAGS.test_data_path
                               or not training_data_loader
                               or (FLAGS.validation_data_path and not validation_data_loader)):
        # Dataset reader is required to read training data and/or for training (and validation) data loader
        dataset_reader = default_ud_dataset_reader(FLAGS.pretrained_transformer_name,
                                                   tokenizer=LamboTokenizer(FLAGS.tokenizer_language,
                                                                            default_turns=FLAGS.turns,
                                                                            default_split_subwords=FLAGS.split_subwords)
                                                   )

    if not training_data_loader:
        training_data_loader = default_data_loader(dataset_reader, training_data_path)
    else:
        if training_data_path:
            training_data_loader.data_path = training_data_path
        else:
            logger.warning(f'No training data path provided - using the path from configuration: ' +
                           str(training_data_loader.data_path), prefix=prefix)

    if FLAGS.validation_data_path and not validation_data_loader:
        validation_data_loader = default_data_loader(dataset_reader, validation_data_path)
    elif FLAGS.validation_data_path and validation_data_loader:
        if validation_data_path:
            validation_data_loader.data_path = validation_data_path
        else:
            logger.warning(f'No validation data path provided - using the path from configuration: ' +
                           str(validation_data_loader.data_path), prefix=prefix)

    if not vocabulary:
        vocabulary = build_vocabulary_from_instances(training_data_loader, validation_data_loader, prefix)

    return dataset_reader, training_data_loader, validation_data_loader, vocabulary


def _read_property_from_config(property_key: str,
                               params: Dict[str, Any],
                               logging_prefix: str,
                               pass_down_parameters: Dict[str, Any] = None) -> Optional[Any]:
    property = None
    pass_down_parameters = pass_down_parameters or {}
    if property_key in params:
        logger.info(f'Reading {property_key.replace("_", " ")} from parameters.', prefix=logging_prefix)
        try:
            property = resolve(params[property_key], pass_down_parameters=pass_down_parameters)
        except Exception as e:
            handle_error(e, logging_prefix)
    return property


def read_dataset_reader_from_config(params: Dict[str, Any],
                                    logging_prefix: str,
                                    pass_down_parameters: Dict[str, Any] = None) -> Optional[DataLoader]:
    return _read_property_from_config('dataset_reader', params, logging_prefix, pass_down_parameters)


def read_data_loader_from_config(params: Dict[str, Any],
                                 logging_prefix: str,
                                 validation: bool = False,
                                 pass_down_parameters: Dict[str, Any] = None) -> Optional[DataLoader]:
    key = 'validation_data_loader' if validation else 'data_loader'
    return _read_property_from_config(key, params, logging_prefix, pass_down_parameters)


def read_vocabulary_from_config(params: Dict[str, Any],
                                logging_prefix: str,
                                pass_down_parameters: Dict[str, Any] = None) -> Optional[Vocabulary]:
    vocabulary = None
    pass_down_parameters = pass_down_parameters or {}
    if "vocabulary" in params:
        logger.info('Reading vocabulary from saved directory.', prefix=logging_prefix)
        if 'directory' in params['vocabulary']['parameters']:
            params['vocabulary']['parameters']['directory'] = os.path.join('/'.join(FLAGS.config_path.split('/')[:-1]),
                                                                           params['vocabulary']['parameters'][
                                                                               'directory'])
        try:
            vocabulary = resolve(params['vocabulary'], pass_down_parameters)
        except Exception as e:
            handle_error(e, logging_prefix)
    return vocabulary


def read_model_from_config(logging_prefix: str) -> Optional[
    Tuple[Model, DatasetReader, DataLoader, DataLoader, Vocabulary]]:
    try:
        checks.file_exists(FLAGS.config_path)
    except ConfigurationError as e:
        handle_error(e, logging_prefix)
        return

    if FLAGS.serialization_dir is None:
        logger.error(f'--serialization_dir was not passed as an argument!')
        print(f'--serialization_dir was not passed as an argument!')
        return

    with open(FLAGS.config_path, 'r') as f:
        params = json.load(f)

    if not FLAGS.use_pure_config:
        params = override_parameters(params, _get_ext_vars(finetuning=False))
        if 'feats' not in FLAGS.targets and 'morphological_feat' in params['model']['parameters']:
            del params['model']['parameters']['morphological_feat']

    pass_down_parameters = {}
    model_name = params.get("model_name")
    if model_name:
        pass_down_parameters = {"model_name": model_name}

    dataset_reader = read_dataset_reader_from_config(params, logging_prefix, pass_down_parameters)
    training_data_loader = read_data_loader_from_config(params, logging_prefix,
                                                        validation=False, pass_down_parameters=pass_down_parameters)
    if (
            not FLAGS.validation_data_path or not FLAGS.finetuning_validation_data_path) and 'validation_data_loader' in params:
        logger.warning('Validation data loader is in parameters, but no validation data path was provided!')
        validation_data_loader = None
    else:
        validation_data_loader = read_data_loader_from_config(params, logging_prefix,
                                                              validation=True,
                                                              pass_down_parameters=pass_down_parameters)
    vocabulary = read_vocabulary_from_config(params, logging_prefix, pass_down_parameters)

    dataset_reader, training_data_loader, validation_data_loader, vocabulary = get_defaults(
        dataset_reader,
        training_data_loader,
        validation_data_loader,
        vocabulary,
        FLAGS.training_data_path if not FLAGS.finetuning else FLAGS.finetuning_training_data_path,
        FLAGS.validation_data_path if not FLAGS.finetuning else FLAGS.finetuning_validation_data_path,
        logging_prefix
    )

    pass_down_parameters = {'vocabulary': vocabulary}
    if not FLAGS.use_pure_config:
        pass_down_parameters['model_name'] = FLAGS.pretrained_transformer_name

    logger.info('Resolving the model from parameters.', prefix=logging_prefix)
    model = resolve(params['model'], pass_down_parameters=pass_down_parameters)

    return model, dataset_reader, training_data_loader, validation_data_loader, vocabulary


def run(_):
    if FLAGS.mode == 'train':
        model, dataset_reader, training_data_loader, validation_data_loader, vocabulary = None, None, None, None, None

        if not FLAGS.finetuning:
            prefix = 'Training'
            logger.info('Setting up the model for training', prefix=prefix)

            if FLAGS.config_path:
                logger.info(f'Reading parameters from configuration path {FLAGS.config_path}', prefix=prefix)
                model, dataset_reader, training_data_loader, validation_data_loader, vocabulary = read_model_from_config(
                    prefix)
            else:
                dataset_reader, training_data_loader, validation_data_loader, vocabulary = get_defaults(
                    dataset_reader,
                    training_data_loader,
                    validation_data_loader,
                    vocabulary,
                    FLAGS.training_data_path,
                    FLAGS.validation_data_path,
                    prefix
                )
                model = default_model(FLAGS.pretrained_transformer_name, vocabulary)

            if FLAGS.use_pure_config and model is None:
                logger.error('Error in configuration - model could not be read from parameters. ' +
                             'Correct the configuration or use --nopure_config ' +
                             'to use default models.')
                return

            try:
                pathlib.Path(FLAGS.serialization_dir).mkdir(parents=True, exist_ok=True)
            except FileExistsError:
                pass
            serialization_dir = tempfile.mkdtemp(prefix='combo', dir=FLAGS.serialization_dir)

        else:
            prefix = 'Finetuning'

            try:
                checks.file_exists(FLAGS.finetuning_training_data_path)
                if FLAGS.finetuning_validation_data_path:
                    checks.file_exists(FLAGS.finetuning_validation_data_path)
            except ConfigurationError as e:
                handle_error(e, prefix)

            logger.info('Loading the model for finetuning', prefix=prefix)
            model, _, training_data_loader, validation_data_loader, dataset_reader = load_archive(FLAGS.model_path)

            if model is None:
                logger.error(f'Model could not be loaded from archive {str(FLAGS.model_path)}. Exiting', prefix=prefix)
                return

            vocabulary = model.vocab

            try:
                pathlib.Path(FLAGS.serialization_dir).mkdir(parents=True, exist_ok=True)
            except FileExistsError:
                pass
            serialization_dir = tempfile.mkdtemp(prefix='combo', suffix='-finetuning', dir=FLAGS.serialization_dir)

            dataset_reader, training_data_loader, validation_data_loader, vocabulary = get_defaults(
                dataset_reader,
                training_data_loader,
                validation_data_loader,
                vocabulary,
                FLAGS.finetuning_training_data_path,
                FLAGS.finetuning_validation_data_path,
                prefix
            )

        logger.info('Indexing training data loader', prefix=prefix)
        training_data_loader.index_with(model.vocab)

        if validation_data_loader:
            logger.info('Indexing validation data loader', prefix=prefix)
            validation_data_loader.index_with(model.vocab)

        nlp = TrainableCombo(model,
                             torch.optim.Adam,
                             optimizer_kwargs={'betas': [0.9, 0.9], 'lr': 0.002},
                             validation_metrics=['EM'])

        n_cuda_devices = "auto" if FLAGS.n_cuda_devices == -1 else FLAGS.n_cuda_devices

        tensorboard_logger = TensorBoardLogger(os.path.join(serialization_dir, 'tensorboard_logs'),
                                               name=FLAGS.tensorboard_name) if FLAGS.tensorboard else None

        trainer = pl.Trainer(max_epochs=FLAGS.num_epochs,
                             default_root_dir=serialization_dir,
                             gradient_clip_val=5,
                             devices=n_cuda_devices,
                             logger=tensorboard_logger)
        trainer.fit(model=nlp, train_dataloaders=training_data_loader, val_dataloaders=validation_data_loader)

        logger.info(f'Archiving the model in {serialization_dir}', prefix=prefix)
        archive(model, serialization_dir, training_data_loader, validation_data_loader, dataset_reader)
        logger.info(f"Model stored in: {serialization_dir}", prefix=prefix)

    elif FLAGS.mode == 'predict':
        prefix = 'Predicting'
        logger.info('Loading the model', prefix=prefix)
        model, config, _, _, dataset_reader = load_archive(FLAGS.model_path)

        if config.get("tokenizer_language") is None:
            logger.warning("Tokenizer language was not found in archive's configuration file - " +
                           "using the --tokenizer_language parameter (default: English)")
        tokenizer_language = config.get("tokenizer_language", FLAGS.tokenizer_language)

        if not dataset_reader:
            logger.info("No dataset reader in the configuration or archive file - using a default UD dataset reader",
                        prefix=prefix)
            dataset_reader = default_ud_dataset_reader(FLAGS.pretrained_transformer_name,
                                                       tokenizer=LamboTokenizer(tokenizer_language,
                                                                                default_turns=FLAGS.turns,
                                                                                default_split_subwords=FLAGS.split_subwords)
                                                       )

        predictor = COMBO(model, dataset_reader)

        if FLAGS.input_file == '-':
            print("Interactive mode.")
            sentence = input("Sentence: ")
            prediction = [p.tokens for p in predictor(sentence)]
            # Flatten the prediction
            flattened_prediction = []
            for p in prediction:
                flattened_prediction.extend(p)
            print("{:15} {:15} {:10} {:10} {:10}".format('TOKEN', 'LEMMA', 'UPOS', 'HEAD', 'DEPREL'))
            for token in flattened_prediction:
                print("{:15} {:15} {:10} {:10} {:10}".format(token.text, token.lemma, token.upostag, token.head,
                                                             token.deprel))
        elif FLAGS.output_file:
            try:
                checks.file_exists(FLAGS.input_file)
            except ConfigurationError as e:
                handle_error(e, prefix)

            pathlib.Path(FLAGS.output_file).touch(exist_ok=True)

            logger.info("Predicting examples from file", prefix=prefix)

            predictions = []
            if FLAGS.conllu_format:
                test_trees = dataset_reader.read(FLAGS.input_file)
                with open(FLAGS.output_file, "w") as file:
                    for tree in tqdm(test_trees):
                        prediction = predictor.predict_instance(tree)
                        file.writelines(api.serialize_token_list(api.sentence2conllu(prediction,
                                                                                     keep_semrel=dataset_reader.use_sem)))
                        predictions.append(prediction)

            else:
                tokenizer = LamboTokenizer(tokenizer_language)
                with open(FLAGS.input_file, "r", encoding='utf-8') as file:
                    input_sentences = tokenizer.segment(file.read(),
                                                        turns=FLAGS.turns,
                                                        split_subwords=FLAGS.split_subwords)
                predictions = predictor.predict(input_sentences)
                with open(FLAGS.output_file, "w") as file:
                    for prediction in tqdm(predictions):
                        file.writelines(api.serialize_token_list(api.sentence2conllu(prediction,
                                                                                     keep_semrel=dataset_reader.use_sem)))

            if FLAGS.save_matrices:
                logger.info("Saving matrices", prefix=prefix)
                if FLAGS.serialization_dir is None or pathlib.Path(FLAGS.serialization_dir).exists():
                    logger.warning('Serialization path was not passed as an argument - skipping matrix extraction.')
                    return
                extract_combo_matrices(predictions,
                                       pathlib.Path(FLAGS.serialization_dir),
                                       pathlib.Path(FLAGS.input_file),
                                       logger,
                                       prefix)

        else:
            msg = 'No output file for input file {input_file} specified.'.format(input_file=FLAGS.input_file)
            logger.info(msg, prefix=prefix)
            print(msg)


def _get_ext_vars(finetuning: bool = False) -> Dict:
    if FLAGS.use_pure_config:
        return {}

    to_override = {
        "model_name": FLAGS.pretrained_transformer_name,
        "model": {
            "parameters": {
                "lemmatizer": {
                    "parameters": {
                        "embedding_dim": FLAGS.lemmatizer_embedding_dim
                    }
                },
                "serialization_dir": FLAGS.serialization_dir
            }
        },
        "data_loader": {
            "parameters": {
                "data_path": FLAGS.training_data_path if not finetuning else FLAGS.finetuning_training_data_path,
                "batch_size": FLAGS.batch_size,
                "batches_per_epoch": FLAGS.batches_per_epoch,
                "reader": {
                    "parameters": {
                        "features": FLAGS.features,
                        "targets": FLAGS.targets,
                        "tokenizer": {
                            "parameters": {
                                "language": FLAGS.tokenizer_language
                            }
                        }
                    }
                }
            }
        },
        "validation_data_loader": {
            "parameters": {
                "data_path": FLAGS.validation_data_path if not finetuning else FLAGS.finetuning_validation_data_path,
                "batch_size": FLAGS.batch_size,
                "batches_per_epoch": FLAGS.batches_per_epoch,
                "reader": {
                    "parameters": {
                        "features": FLAGS.features,
                        "targets": FLAGS.targets,
                        "tokenizer": {
                            "parameters": {
                                "language": FLAGS.tokenizer_language
                            }
                        }
                    }
                }
            }
        },
        "dataset_reader": {
            "parameters": {
                "features": FLAGS.features,
                "targets": FLAGS.targets,
                "tokenizer": {
                    "parameters": {
                        "language": FLAGS.tokenizer_language
                    }
                }
            }
        }
    }

    if FLAGS.vocabulary_path:
        to_override["vocabulary"] = {
            "type": "from_files_vocabulary",
            "parameters": {
                "directory": FLAGS.vocabulary_path,
                "padding_token": "__PAD__",
                "oov_token": "_"
            }
        }
    return to_override


def main():
    """Parse flags."""
    flags.register_validator(
        "features",
        lambda values: all(
            value in _FEATURES for value in values),
        message="Flags --features contains unknown value(s)."
    )
    flags.register_validator(
        "mode",
        lambda value: value is not None,
        message="Flag --mode must be set with either `predict` or `train` value")
    flags.register_validator(
        "targets",
        lambda values: all(
            value in _TARGETS for value in values),
        message="Flag --targets contains unknown value(s)."
    )
    app.run(run)


if __name__ == "__main__":
    main()
