"""
Adapted from AllenNLP
https://github.com/allenai/allennlp/blob/main/allennlp/data/dataset_readers/dataset_reader.py
"""
import logging
from os import PathLike
from typing import Iterable, Iterator, Optional, Union, Dict, List

from overrides import overrides
from torch.utils.data import IterableDataset

from combo.config import FromParameters, Registry
from combo.config.from_parameters import register_arguments
from combo.data import LamboTokenizer, SingleIdTokenIndexer
from combo.data.instance import Instance
from combo.data.token_indexers import TokenIndexer
from combo.data.tokenizers import Tokenizer

logger = logging.getLogger(__name__)


PathOrStr = Union[PathLike, str]
DatasetReaderInput = Union[PathOrStr, List[PathOrStr], Dict[str, PathOrStr]]


@Registry.register('base_dataset_reader')
class DatasetReader(IterableDataset, FromParameters):
    """
    A `DatasetReader` knows how to turn a file containing a dataset into a collection
    of `Instance`s.
    """
    @register_arguments
    def __init__(self,
                 tokenizer: Optional[Tokenizer] = None,
                 token_indexers: Optional[Dict[str, TokenIndexer]] = None) -> None:
        super(DatasetReader).__init__()
        # self.__file_path = None
        self.__tokenizer = tokenizer or LamboTokenizer()
        self.__token_indexers = token_indexers or {"tokens": SingleIdTokenIndexer()}

    @property
    def tokenizer(self) -> Optional[Tokenizer]:
        return self.__tokenizer

    @tokenizer.setter
    def tokenizer(self, value):
        self.__tokenizer = value

    @property
    def token_indexers(self) -> Optional[Dict[str, TokenIndexer]]:
        return self.__token_indexers

    @token_indexers.setter
    def token_indexers(self, token_indexers: Dict[str, TokenIndexer]):
        self.__token_indexers = token_indexers

    @overrides
    def __getitem__(self, item, **kwargs) -> Instance:
        raise NotImplementedError

    @overrides
    def __iter__(self) -> Iterator[Instance]:
        """
        Returns an iterator of instances that can be read from the file path.
        """
        # TODO: add multiprocessing
        for instance in self._read():
            self.apply_token_indexers(instance)
            yield instance

    def _read(self, file_path: DatasetReaderInput) -> Iterable[Instance]:
        raise NotImplementedError

    def read(self, file_path: DatasetReaderInput) -> Iterator[Instance]:
        """
        Returns an iterator of instances that can be read from the file path.
        """
        for instance in self._read(file_path):  # type: ignore
            self.apply_token_indexers(instance)
            yield instance

    def apply_token_indexers(self, instance: Instance) -> None:
        pass

    def text_to_instance(self, *inputs) -> Instance:
        """
        Does whatever tokenization or processing is necessary to go from textual input to an
        `Instance`.  The primary intended use for this is with a
        :class:`~allennlp.predictors.predictor.Predictor`, which gets text input as a JSON
        object and needs to process it to be input to a model.

        The intent here is to share code between :func:`_read` and what happens at
        model serving time, or any other time you want to make a prediction from new data.  We need
        to process the data in the same way it was done at training time.  Allowing the
        `DatasetReader` to process new text lets us accomplish this, as we can just call
        `DatasetReader.text_to_instance` when serving predictions.

        The input type here is rather vaguely specified, unfortunately.  The `Predictor` will
        have to make some assumptions about the kind of `DatasetReader` that it's using, in order
        to pass it the right information.
        """
        raise NotImplementedError
