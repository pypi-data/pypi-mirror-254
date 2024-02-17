"""
Adapted from AllenNLP
https://github.com/allenai/allennlp/blob/main/allennlp/data/data_loaders/simple_data_loader.py
"""

import math
import random
from typing import Optional, List, Iterator, Callable

import torch

from combo.common.util import lazy_groups_of
from combo.common.tqdm import Tqdm
from combo.config import Registry
from combo.data.dataset_loaders.data_collator import DefaultDataCollator
from combo.data.dataset_readers import DatasetReader
from combo.data.instance import Instance
from combo.data.vocabulary import Vocabulary
import combo.nn.utils as nn_util

from combo.data.dataset_loaders.dataset_loader import DataLoader, TensorDict


@Registry.register("simple_data_loader")
@Registry.register("simple_data_loader_from_dataset_reader", "from_dataset_reader")
class SimpleDataLoader(DataLoader):
    """
    A very simple `DataLoader` that is mostly used for testing.
    """
    def __init__(
        self,
        instances: List[Instance],
        batch_size: int,
        *,
        shuffle: bool = False,
        batches_per_epoch: Optional[int] = None,
        vocabulary: Optional[Vocabulary] = None,
        collate_fn: Optional[Callable[[List[Instance]], TensorDict]] = DefaultDataCollator()
    ) -> None:
        self.instances = instances
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.batches_per_epoch = batches_per_epoch
        self.vocab = vocabulary
        self.cuda_device: Optional[torch.device] = None
        self._batch_generator: Optional[Iterator[TensorDict]] = None
        self.collate_fn = collate_fn

    def __len__(self) -> int:
        if self.batches_per_epoch is not None:
            return self.batches_per_epoch
        return math.ceil(len(self.instances) / self.batch_size)

    def __iter__(self) -> Iterator[TensorDict]:
        if self.batches_per_epoch is None:
            yield from self._iter_batches()
        else:
            if self._batch_generator is None:
                self._batch_generator = self._iter_batches()
            for i in range(self.batches_per_epoch):
                try:
                    yield next(self._batch_generator)
                except StopIteration:  # data_generator is exhausted
                    self._batch_generator = self._iter_batches()  # so refresh it
                    yield next(self._batch_generator)

    def _iter_batches(self) -> Iterator[TensorDict]:
        if self.shuffle:
            random.shuffle(self.instances)
        for batch in lazy_groups_of(self.iter_instances(), self.batch_size):
            tensor_dict = self.collate_fn(batch)
            if self.cuda_device is not None:
                tensor_dict = nn_util.move_to_device(tensor_dict, self.cuda_device)
            yield tensor_dict

    def iter_instances(self) -> Iterator[Instance]:
        for instance in self.instances:
            if self.vocab is not None:
                instance.index_fields(self.vocab)
            yield instance

    def index_with(self, vocab: Vocabulary) -> None:
        self.vocab = vocab
        for instance in self.instances:
            instance.index_fields(self.vocab)

    def set_target_device(self, device: torch.device) -> None:
        self.cuda_device = device

    @classmethod
    def from_dataset_reader(
        cls,
        reader: DatasetReader,
        data_path: str,
        batch_size: int,
        shuffle: bool = False,
        batches_per_epoch: Optional[int] = None,
        quiet: bool = False,
        collate_fn: Optional[Callable[[List[Instance]], TensorDict]] = DefaultDataCollator()
    ) -> "SimpleDataLoader":
        instance_iter = reader.read(data_path)
        if not quiet:
            instance_iter = Tqdm.tqdm(instance_iter, desc="loading instances")
        instances = list(instance_iter)
        new_obj = cls(instances, batch_size, shuffle=shuffle, batches_per_epoch=batches_per_epoch, collate_fn=collate_fn)
        new_obj.constructed_args = {
            'reader': reader,
            'data_path': data_path,
            'batch_size': batch_size,
            'shuffle': shuffle,
            'batches_per_epoch': batches_per_epoch,
            'quiet': quiet
        }
        new_obj.constructed_from = 'from_dataset_reader'
        return new_obj
