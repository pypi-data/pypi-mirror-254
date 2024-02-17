"""
Partially adapted from AllenNLP
https://github.com/allenai/allennlp/blob/main/allennlp/data/dataset_readers/text_classification_json.py
"""

import json
from typing import Dict, Iterable, Optional, Union, List

from overrides import overrides

from combo.data.dataset_readers.dataset_reader import DatasetReader, DatasetReaderInput
from combo.data.dataset_readers.utils import MalformedFileException
from combo.data import Instance, Tokenizer, TokenIndexer
from combo.data.fields import Field, ListField
from combo.data.fields.label_field import LabelField
from combo.data.fields.text_field import TextField
from combo.config import Registry
from combo.config.from_parameters import register_arguments
from combo.utils import ConfigurationError


def _is_sentence_segmenter(sentence_segmenter: Optional[Tokenizer]) -> bool:
    split_sentences_method = getattr(sentence_segmenter, "split_sentences", None)
    return callable(split_sentences_method)


@Registry.register('text_classification_json_dataset_reader')
class TextClassificationJSONReader(DatasetReader):
    @register_arguments
    def __init__(self,
                 tokenizer: Optional[Tokenizer] = None,
                 token_indexers: Optional[Dict[str, TokenIndexer]] = None,
                 max_sequence_length: Optional[int] = None,
                 skip_label_indexing: bool = False,
                 text_key: str = "text",
                 label_key: str = "label") -> None:
        super().__init__(tokenizer, token_indexers)
        self.__max_sequence_length = max_sequence_length
        self.__skip_label_indexing = skip_label_indexing
        self.__text_key = text_key
        self.__label_key = label_key

    @property
    def max_sequence_length(self) -> Optional[int]:
        return self.__max_sequence_length

    @max_sequence_length.setter
    def max_sequence_length(self, value: Optional[int]):
        self.__max_sequence_length = value

    @property
    def skip_label_indexing(self) -> bool:
        return self.__skip_label_indexing

    @skip_label_indexing.setter
    def skip_label_indexing(self, value: bool):
        self.__skip_label_indexing = value

    @property
    def text_key(self) -> str:
        return self.__text_key

    @text_key.setter
    def text_key(self, value: str):
        self.__text_key = value

    @property
    def label_key(self) -> str:
        return self.__label_key

    @label_key.setter
    def label_key(self, value: str):
        self.__label_key = value

    @overrides
    def _read(self, file_path: DatasetReaderInput) -> Iterable[Instance]:
        # if self.file_path is None:
        #     raise ValueError('File path is None')
        with open(file_path, "r") as data_file:
            for line in data_file.readlines():
                if not line:
                    continue
                items = json.loads(line)
                text = items.get(self.text_key)
                if text is None:
                    raise MalformedFileException(f'No item with {self.text_key} (text) label')
                label = items.get(self.label_key)
                if label is not None:
                    if self.skip_label_indexing:
                        try:
                            label = int(label)
                        except ValueError:
                            raise MalformedFileException("Labels must be integers if skip_label_indexing is True.")
                    else:
                        label = str(label)
                yield self.text_to_instance(text, label)


    def text_to_instance(self,
                         text: str,
                         label: Optional[Union[str, int]] = None) -> Instance:
        """

        :param text: the text to classify
        :param label: the label for the text
        :return: Instance containing the following fields:
            - tokens ('TextField')
            - label ('LabelField')
        """
        fields: Dict[str, Field] = {}
        sentences: List[Field] = []

        # TODO: some subclass for sentence segmenter for tokenizers?
        sentence_splits = self.tokenizer.tokenize(text)
        for word_tokens in sentence_splits:
            if self.max_sequence_length is not None:
                word_tokens = self._truncate(word_tokens)
            sentences.append(TextField(word_tokens))
        fields["tokens"] = ListField(sentences)

        if label is not None:
            fields["label"] = LabelField(label,
                                         skip_indexing=self.skip_label_indexing)
        return Instance(fields)

    def _truncate(self, tokens):
        """
        truncate a set of tokens using the provided sequence length
        """
        if len(tokens) > self.max_sequence_length:
            tokens = tokens[: self.max_sequence_length]
        return tokens

    def __call__(self, file_path: str):
        self.file_path = file_path
        return self

    @overrides
    def apply_token_indexers(self, instance: Instance) -> None:
        if isinstance(instance.fields["tokens"], ListField):
            for text_field in instance.fields["tokens"]:  # type: ignore
                text_field._token_indexers = self.token_indexers
        else:
            instance.fields["tokens"]._token_indexers = self.token_indexers  # type: ignore
