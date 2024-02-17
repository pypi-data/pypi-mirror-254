import os
import shutil
import tempfile
from os import PathLike
from pathlib import Path
from typing import Any, Dict, Union, NamedTuple, Optional

import cached_path
import torch
import json
import tarfile
from io import BytesIO
from tempfile import TemporaryDirectory

from combo.config import resolve
from combo.data.dataset_loaders import DataLoader
from combo.data.dataset_readers import DatasetReader
from combo.modules.model import Model
from contextlib import contextmanager

import logging
from combo.utils import ComboLogger

logging.setLoggerClass(ComboLogger)
logger = logging.getLogger(__name__)


CACHE_ROOT = Path(os.getenv("COMBO_CACHE_ROOT", Path.home() / ".combo"))
CACHE_DIRECTORY = str(CACHE_ROOT / "cache")

PREFIX = 'Loading archive'

class Archive(NamedTuple):
    model: Model
    config: Optional[Dict[str, Any]]
    data_loader: Optional[DataLoader]
    validation_data_loader: Optional[DataLoader]
    dataset_reader: Optional[DatasetReader]


def add_to_tar(tar_file: tarfile.TarFile, out_stream: BytesIO, data: bytes, name: str):
    out_stream.write(data)
    out_stream.seek(0)
    info = tarfile.TarInfo(name)
    info.size = len(out_stream.getbuffer())
    tar_file.addfile(info, out_stream)


def archive(model: Model,
            serialization_dir: Union[PathLike, str],
            data_loader: Optional[DataLoader] = None,
            validation_data_loader: Optional[DataLoader] = None,
            dataset_reader: Optional[DatasetReader] = None) -> str:
    parameters = {'vocabulary': {
        'type': 'from_files_vocabulary',
        'parameters': {
            'directory': 'vocabulary',
            'padding_token': model.vocab._padding_token,
            'oov_token': model.vocab._oov_token
        }
    }, 'model': model.serialize(pass_down_parameter_names=['vocabulary', 'optimizer', 'scheduler', 'model_name'])}

    if data_loader:
        parameters['data_loader'] = data_loader.serialize()
    if validation_data_loader:
        parameters['validation_data_loader'] = validation_data_loader.serialize()
    if dataset_reader:
        parameters['dataset_reader'] = dataset_reader.serialize()

    parameters['training'] = {}

    if model.optimizer:
        parameters['training']['optimizer'] = model.optimizer.serialize()

    if model.scheduler:
        parameters['training']['scheduler'] = model.scheduler.serialize(pass_down_parameter_names=['optimizer'])

    if model.model_name:
        parameters['model_name'] = model.model_name

    with (TemporaryDirectory(os.path.join('tmp')) as t,
          BytesIO() as out_stream,
          tarfile.open(os.path.join(serialization_dir, 'model.tar.gz'), 'w|gz') as tar_file):
        add_to_tar(tar_file, out_stream, json.dumps(parameters).encode(), 'config.json')
        weights_path = os.path.join(t, 'weights.th')
        torch.save(model.state_dict(), weights_path)
        tar_file.add(weights_path, 'weights.th')
        vocabulary_path = os.path.join(t, 'vocabulary')
        model.vocab.save_to_files(vocabulary_path)
        tar_file.add(vocabulary_path, 'vocabulary', recursive=True)

    return serialization_dir


@contextmanager
def extracted_archive(resolved_archive_file, cleanup=True):
    tempdir = None
    try:
        tempdir = tempfile.mkdtemp(dir=CACHE_DIRECTORY)
        with tarfile.open(resolved_archive_file) as archive:
            subdir_and_files = [
                tarinfo for tarinfo in archive.getmembers()
                if (any([tarinfo.name.endswith(f) for f in ['config.json', 'weights.th']])
                    or 'vocabulary' in tarinfo.name)
            ]
            for f in subdir_and_files:
                if 'vocabulary' in f.name and not f.name.endswith('vocabulary'):
                    f.name = os.path.join('vocabulary', os.path.basename(f.name))
                else:
                    f.name = os.path.basename(f.name)
            archive.extractall(path=tempdir, members=subdir_and_files)
            yield tempdir
    finally:
        if tempdir is not None and cleanup:
            shutil.rmtree(tempdir, ignore_errors=True)


def load_archive(url_or_filename: Union[PathLike, str],
                 cache_dir: Union[PathLike, str] = None,
                 cuda_device: int = -1) -> Archive:

    rarchive_file = cached_path.cached_path(
            url_or_filename,
            cache_dir=cache_dir or CACHE_DIRECTORY,
        )

    with extracted_archive(rarchive_file) as archive_file:
        model = Model.load(archive_file, cuda_device=cuda_device)

        config_path = os.path.join(archive_file, 'config.json')
        with open(config_path, 'r') as f:
            config = json.load(f)

        data_loader, validation_data_loader, dataset_reader = None, None, None
        pass_down_parameters = {}
        if config.get("model_name"):
            pass_down_parameters = {"model_name": config.get("model_name")}


        if 'data_loader' in config:
            try:
                data_loader = resolve(config['data_loader'],
                                      pass_down_parameters=pass_down_parameters)
            except Exception as e:
                logger.warning(f'Error while loading Training Data Loader: {str(e)}. Setting Data Loader to None',
                               prefix=PREFIX)
        if 'validation_data_loader' in config:
            try:
                validation_data_loader = resolve(config['validation_data_loader'],
                                                 pass_down_parameters=pass_down_parameters)
            except Exception as e:
                logger.warning(f'Error while loading Validation Data Loader: {str(e)}. Setting Data Loader to None',
                               prefix=PREFIX)
        if 'dataset_reader' in config:
            try:
                dataset_reader = resolve(config['dataset_reader'],
                                         pass_down_parameters=pass_down_parameters)
            except Exception as e:
                logger.warning(f'Error while loading Dataset Reader: {str(e)}. Setting Dataset Reader to None',
                               prefix=PREFIX)

    return Archive(model=model,
                   config=config,
                   data_loader=data_loader,
                   validation_data_loader=validation_data_loader,
                   dataset_reader=dataset_reader)
