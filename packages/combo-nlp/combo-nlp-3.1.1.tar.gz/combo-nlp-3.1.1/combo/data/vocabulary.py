import codecs
import glob
import json
import logging
import os
import re
from collections import defaultdict
from typing import Dict, Optional, Iterable, Set, List, Union

from filelock import FileLock
from transformers import PreTrainedTokenizer

from combo.common import Tqdm
from combo.config import FromParameters, Registry
from combo.config.from_parameters import register_arguments
from combo.utils import ConfigurationError
from combo.utils.file_utils import cached_path

logger = logging.Logger(__name__)

DEFAULT_NON_PADDED_NAMESPACES = ("*tags", "*labels")
DEFAULT_PADDING_TOKEN = "@@PADDING@@"
DEFAULT_OOV_TOKEN = "@@UNKNOWN@@"
NAMESPACE_PADDING_FILE = "non_padded_namespaces.txt"
DEFAULT_NAMESPACE = "tokens"
_NEW_LINE_REGEX = re.compile(r"\n|\r\n")


def match_namespace(pattern: str, namespace: str):
    if not isinstance(pattern, str):
        raise ValueError("Pattern and _namespace must be string types, got %s and %s." %
                         (type(pattern), type(namespace)))
    if pattern == namespace:
        return True
    if len(pattern) > 2 and pattern[0] == '*' and namespace.endswith(pattern[1:]):
        return True
    return False


def _read_pretrained_tokens(embeddings_file_uri: str) -> List[str]:
    # Moving this import to the top breaks everything (cycling import, I guess)
    from combo.modules.token_embedders.embeddings_text_file import EmbeddingsTextFile

    logger.info("Reading pretrained tokens from: %s", embeddings_file_uri)
    tokens: List[str] = []
    with EmbeddingsTextFile(embeddings_file_uri) as embeddings_file:
        for line_number, line in enumerate(Tqdm.tqdm(embeddings_file), start=1):
            token_end = line.find(" ")
            if token_end >= 0:
                token = line[:token_end]
                tokens.append(token)
            else:
                line_begin = line[:20] + "..." if len(line) > 20 else line
                logger.warning("Skipping line number %d: %s", line_number, line_begin)
    return tokens


class NamespaceVocabulary:
    def __init__(self,
                 padding_token: Optional[str] = None,
                 oov_token: Optional[str] = None):
        if padding_token and oov_token:
            self._itos = {0: padding_token, 1: oov_token}
            self._stoi = {padding_token: 0, oov_token: 1}
        elif not padding_token and not oov_token:
            self._itos = {}
            self._stoi = {}
        else:
            raise ValueError('Padding token and OOV token must be either both None or both provided')

    def append_token(self, token: str):
        # TODO: Should I check if tokens are duplicated here?
        vocab_size = len(self._itos)
        self._itos[vocab_size] = token
        self._stoi[token] = vocab_size

    def append_tokens(self, tokens: Iterable[str]):
        next_index = len(self._itos)
        for ind, token in enumerate(tokens):
            self._itos[next_index + ind] = token
            self._stoi[token] = next_index + ind

    def insert_token(self, token: str, index: int):
        self._itos[index] = token
        self._stoi[token] = index

    def get_itos(self) -> Dict[int, str]:
        return self._itos

    def get_stoi(self) -> Dict[str, int]:
        return self._stoi


class _NamespaceDependentDefaultDict(defaultdict[str, NamespaceVocabulary]):
    def __init__(self,
                 non_padded_namespaces: Iterable[str],
                 padding_token: str,
                 oov_token: str):
        self._non_padded_namespaces = set(non_padded_namespaces)
        self._padding_token = padding_token
        self._oov_token = oov_token
        super().__init__()

    def add_non_padded_namespaces(self, non_padded_namespaces: Set[str]):
        self._non_padded_namespaces.update(non_padded_namespaces)

    def __missing__(self, namespace: str):
        # Non-padded _namespace
        if any([match_namespace(npn, namespace) for npn in self._non_padded_namespaces]):
            value = NamespaceVocabulary()
        else:
            value = NamespaceVocabulary(self._padding_token, self._oov_token)
        dict.__setitem__(self, namespace, value)
        return value


@Registry.register("base_vocabulary")
@Registry.register("from_files_vocabulary", "from_files")
@Registry.register("from_pretrained_transformer_vocabulary", "from_pretrained_transformer")
@Registry.register("from_data_loader_vocabulary", "from_data_loader")
@Registry.register("from_data_loader_extended_vocabulary", "from_data_loader_extended")
class Vocabulary(FromParameters):
    @register_arguments
    def __init__(self,
                 counter: Dict[str, Dict[str, int]] = None,
                 min_count: Dict[str, int] = None,
                 max_vocab_size: Union[int, Dict[str, int]] = None,
                 non_padded_namespaces: Iterable[str] = DEFAULT_NON_PADDED_NAMESPACES,
                 pretrained_files: Optional[Dict[str, str]] = None,
                 only_include_pretrained_words: bool = False,
                 tokens_to_add: Dict[str, List[str]] = None,
                 min_pretrained_embeddings: Dict[str, int] = None,
                 padding_token: Optional[str] = DEFAULT_PADDING_TOKEN,
                 oov_token: Optional[str] = DEFAULT_OOV_TOKEN,
                 serialization_dir: Optional[str] = None):
        self._padding_token = padding_token if padding_token is not None else DEFAULT_PADDING_TOKEN
        self._oov_token = oov_token if oov_token is not None else DEFAULT_OOV_TOKEN
        self._non_padded_namespaces = set(non_padded_namespaces)
        self._vocab = _NamespaceDependentDefaultDict(self._non_padded_namespaces,
                                                     self._padding_token,
                                                     self._oov_token)
        self._retained_counter: Optional[Dict[str, Dict[str, int]]] = None
        self._serialization_dir: Optional[str] = serialization_dir
        self._extend(
            counter,
            min_count,
            max_vocab_size,
            non_padded_namespaces,
            pretrained_files,
            only_include_pretrained_words,
            tokens_to_add,
            min_pretrained_embeddings
        )

    def _extend(self,
                counter: Dict[str, Dict[str, int]] = None,
                min_count: Dict[str, int] = None,
                max_vocab_size: Union[int, Dict[str, int]] = None,
                non_padded_namespaces: Iterable[str] = DEFAULT_NON_PADDED_NAMESPACES,
                pretrained_files: Optional[Dict[str, str]] = None,
                only_include_pretrained_words: bool = False,
                tokens_to_add: Dict[str, Dict[str, int]] = None,
                min_pretrained_embeddings: Dict[str, int] = None):
        if min_count is not None:
            for key in min_count:
                if counter is not None and key not in counter or counter is None:
                    raise ConfigurationError(
                        f"The key '{key}' is present in min_count but not in counter"
                    )
        if not isinstance(max_vocab_size, dict):
            int_max_vocab_size = max_vocab_size
            max_vocab_size = defaultdict(lambda: int_max_vocab_size)  # type: ignore

        min_count = min_count or {}
        pretrained_files = pretrained_files or {}
        min_pretrained_embeddings = min_pretrained_embeddings or {}
        non_padded_namespaces = set(non_padded_namespaces)
        counter = counter or {}
        tokens_to_add = tokens_to_add or {}
        self._retained_counter = counter
        # Make sure vocabulary extension is safe.
        current_namespaces = {*self._vocab}
        extension_namespaces = {*counter, *tokens_to_add}

        for namespace in current_namespaces & extension_namespaces:
            # if new namespace was already present
            # Either both should be padded or none should be.
            original_padded = not any(
                match_namespace(pattern, namespace) for pattern in self._non_padded_namespaces
            )
            extension_padded = not any(
                match_namespace(pattern, namespace) for pattern in non_padded_namespaces
            )
            if original_padded != extension_padded:
                raise ConfigurationError(
                    "Common namespace {} has conflicting ".format(namespace)
                    + "setting of padded = True/False. "
                    + "Hence extension cannot be done."
                )

        self._vocab.add_non_padded_namespaces(non_padded_namespaces)
        self._non_padded_namespaces.update(non_padded_namespaces)

        for namespace in counter:
            pretrained_set: Optional[Set] = None
            if namespace in pretrained_files:
                pretrained_list = _read_pretrained_tokens(pretrained_files[namespace])
                min_embeddings = min_pretrained_embeddings.get(namespace, 0)
                if min_embeddings > 0 or min_embeddings == -1:
                    tokens_old = tokens_to_add.get(namespace, [])
                    tokens_new = (
                        pretrained_list
                        if min_embeddings == -1
                        else pretrained_list[:min_embeddings]
                    )
                    tokens_to_add[namespace] = tokens_old + tokens_new
                pretrained_set = set(pretrained_list)
            token_counts = list(counter[namespace].items())
            token_counts.sort(key=lambda x: x[1], reverse=True)
            max_vocab: Optional[int]
            try:
                max_vocab = max_vocab_size[namespace]
            except KeyError:
                max_vocab = None
            if max_vocab:
                token_counts = token_counts[:max_vocab]
            for token, count in token_counts:
                if pretrained_set is not None:
                    if only_include_pretrained_words:
                        if token in pretrained_set and count >= min_count.get(namespace, 1):
                            self.add_token_to_namespace(token, namespace)
                    elif token in pretrained_set or count >= min_count.get(namespace, 1):
                        self.add_token_to_namespace(token, namespace)
                elif count >= min_count.get(namespace, 1):
                    self.add_token_to_namespace(token, namespace)

        for namespace, tokens in tokens_to_add.items():
            self._vocab[namespace].append_tokens(tokens)

    @classmethod
    def from_files(cls,
                   directory: Union[str, os.PathLike],
                   padding_token: Optional[str] = DEFAULT_PADDING_TOKEN,
                   oov_token: Optional[str] = DEFAULT_OOV_TOKEN) -> "Vocabulary":
        """
                Loads a `Vocabulary` that was serialized either using `save_to_files` or inside
                a model archive file.

                # Parameters

                directory : `str`
                    The directory or archive file containing the serialized vocabulary.
                """
        logger.info("Loading token dictionary from %s.", directory)
        padding_token = padding_token if padding_token is not None else DEFAULT_PADDING_TOKEN
        oov_token = oov_token if oov_token is not None else DEFAULT_OOV_TOKEN

        if not os.path.isdir(directory):
            base_directory = cached_path(directory, extract_archive=True)
            # For convenience we'll check for a 'vocabulary' subdirectory of the archive.
            # That way you can use model archives directly.
            vocab_subdir = os.path.join(base_directory, "vocabulary")
            if os.path.isdir(vocab_subdir):
                directory = vocab_subdir
            elif os.path.isdir(base_directory):
                directory = base_directory
            else:
                raise ConfigurationError(f"{directory} is neither a directory nor an archive")

        files = [file for file in glob.glob(os.path.join(directory, '*.txt'))]

        if len(files) == 0:
            logger.warning(f'Directory %s is empty' % directory)

        with FileLock(os.path.join(directory, ".lock")):
            with codecs.open(
                    os.path.join(directory, NAMESPACE_PADDING_FILE), "r", "utf-8"
            ) as namespace_file:
                non_padded_namespaces = [namespace_str.strip() for namespace_str in namespace_file]

            vocab = cls(
                non_padded_namespaces=non_padded_namespaces,
                padding_token=padding_token,
                oov_token=oov_token,
                serialization_dir=directory
            )

            for namespace_filename in os.listdir(directory):
                if namespace_filename == "slices.json":
                    continue
                if namespace_filename == NAMESPACE_PADDING_FILE:
                    continue
                if namespace_filename.startswith("."):
                    continue
                namespace = namespace_filename.replace(".txt", "")
                if any(match_namespace(pattern, namespace) for pattern in non_padded_namespaces):
                    is_padded = False
                else:
                    is_padded = True
                filename = os.path.join(directory, namespace_filename)
                vocab.set_from_file(filename, is_padded, namespace=namespace, oov_token=oov_token)

            with codecs.open(
                    os.path.join(directory, "slices.json"), "r", "utf-8"
            ) as slices_file:
                vocab.slices = json.load(slices_file)

        vocab.constructed_from = 'from_files'
        vocab.constructed_args = {
            "directory": directory.split("/")[-1],
            "padding_token": padding_token,
            "oov_token": oov_token
        }
        return vocab

    @classmethod
    def from_data_loader(
            cls,
            data_loader: "DataLoader",
            min_count: Dict[str, int] = None,
            max_vocab_size: Union[int, Dict[str, int]] = None,
            non_padded_namespaces: Iterable[str] = DEFAULT_NON_PADDED_NAMESPACES,
            pretrained_files: Optional[Dict[str, str]] = None,
            only_include_pretrained_words: bool = False,
            tokens_to_add: Dict[str, List[str]] = None,
            min_pretrained_embeddings: Dict[str, int] = None,
            padding_token: Optional[str] = DEFAULT_PADDING_TOKEN,
            oov_token: Optional[str] = DEFAULT_OOV_TOKEN,
            serialization_dir: Optional[str] = None
    ) -> "Vocabulary":
        vocab = cls.from_instances(
            instances=data_loader.iter_instances(),
            min_count=min_count,
            max_vocab_size=max_vocab_size,
            non_padded_namespaces=non_padded_namespaces,
            pretrained_files=pretrained_files,
            only_include_pretrained_words=only_include_pretrained_words,
            tokens_to_add=tokens_to_add,
            min_pretrained_embeddings=min_pretrained_embeddings,
            padding_token=padding_token,
            oov_token=oov_token,
            serialization_dir=serialization_dir
        )
        vocab.constructed_args = {
            "data_loader": data_loader,
            "min_count": min_count,
            "max_vocab_size": max_vocab_size,
            "non_padded_namespaces": non_padded_namespaces,
            "pretrained_files": pretrained_files,
            "only_include_pretrained_words": only_include_pretrained_words,
            "tokens_to_add": tokens_to_add,
            "min_pretrained_embeddings": min_pretrained_embeddings,
            "padding_token": padding_token,
            "oov_token": oov_token,
            "serialization_dir": serialization_dir
        }
        return vocab

    @classmethod
    def from_instances(
            cls,
            instances: Iterable["Instance"],
            min_count: Dict[str, int] = None,
            max_vocab_size: Union[int, Dict[str, int]] = None,
            non_padded_namespaces: Iterable[str] = DEFAULT_NON_PADDED_NAMESPACES,
            pretrained_files: Optional[Dict[str, str]] = None,
            only_include_pretrained_words: bool = False,
            tokens_to_add: Dict[str, List[str]] = None,
            min_pretrained_embeddings: Dict[str, int] = None,
            padding_token: Optional[str] = DEFAULT_PADDING_TOKEN,
            oov_token: Optional[str] = DEFAULT_OOV_TOKEN,
            serialization_dir: Optional[str] = None
    ) -> "Vocabulary":
        """
                Constructs a vocabulary given a collection of `Instances` and some parameters.
                We count all of the vocabulary items in the instances, then pass those counts
                and the other parameters, to :func:`__init__`.  See that method for a description
                of what the other parameters do.

                The `instances` parameter does not get an entry in a typical AllenNLP configuration file,
                but the other parameters do (if you want non-default parameters).
                """
        logger.info("Fitting token dictionary from dataset.")
        padding_token = padding_token if padding_token is not None else DEFAULT_PADDING_TOKEN
        oov_token = oov_token if oov_token is not None else DEFAULT_OOV_TOKEN
        namespace_token_counts: Dict[str, Dict[str, int]] = defaultdict(lambda: defaultdict(int))
        for instance in Tqdm.tqdm(instances, desc="building vocabulary"):
            instance.count_vocab_items(namespace_token_counts)

        vocab = cls(
            counter=namespace_token_counts,
            min_count=min_count,
            max_vocab_size=max_vocab_size,
            non_padded_namespaces=non_padded_namespaces,
            pretrained_files=pretrained_files,
            only_include_pretrained_words=only_include_pretrained_words,
            tokens_to_add=tokens_to_add,
            min_pretrained_embeddings=min_pretrained_embeddings,
            padding_token=padding_token,
            oov_token=oov_token,
            serialization_dir=serialization_dir
        )
        return vocab

    @classmethod
    def from_files_and_instances(
            cls,
            instances: Iterable["Instance"],
            directory: str,
            padding_token: Optional[str] = DEFAULT_PADDING_TOKEN,
            oov_token: Optional[str] = DEFAULT_OOV_TOKEN,
            min_count: Dict[str, int] = None,
            max_vocab_size: Union[int, Dict[str, int]] = None,
            non_padded_namespaces: Iterable[str] = DEFAULT_NON_PADDED_NAMESPACES,
            pretrained_files: Optional[Dict[str, str]] = None,
            only_include_pretrained_words: bool = False,
            tokens_to_add: Dict[str, List[str]] = None,
            min_pretrained_embeddings: Dict[str, int] = None,
            serialization_dir: Optional[str] = None
    ) -> "Vocabulary":
        """
        Extends an already generated vocabulary using a collection of instances.

        The `instances` parameter does not get an entry in a typical AllenNLP configuration file,
        but the other parameters do (if you want non-default parameters).  See `__init__` for a
        description of what the other parameters mean.
        """
        vocab = cls.from_files(directory, padding_token, oov_token)
        logger.info("Fitting token dictionary from dataset.")
        namespace_token_counts: Dict[str, Dict[str, int]] = defaultdict(lambda: defaultdict(int))
        for instance in Tqdm.tqdm(instances):
            instance.count_vocab_items(namespace_token_counts)
        vocab._extend(
            counter=namespace_token_counts,
            min_count=min_count,
            max_vocab_size=max_vocab_size,
            non_padded_namespaces=non_padded_namespaces,
            pretrained_files=pretrained_files,
            only_include_pretrained_words=only_include_pretrained_words,
            tokens_to_add=tokens_to_add,
            min_pretrained_embeddings=min_pretrained_embeddings
        )
        vocab.constructed_from = 'from_files_and_instances'
        return vocab

    @classmethod
    def from_pretrained_transformer_and_instances(
            cls,
            instances: Iterable["Instance"],
            transformers: Dict[str, str],
            min_count: Dict[str, int] = None,
            max_vocab_size: Union[int, Dict[str, int]] = None,
            non_padded_namespaces: Iterable[str] = DEFAULT_NON_PADDED_NAMESPACES,
            pretrained_files: Optional[Dict[str, str]] = None,
            only_include_pretrained_words: bool = False,
            tokens_to_add: Dict[str, List[str]] = None,
            min_pretrained_embeddings: Dict[str, int] = None,
            padding_token: Optional[str] = DEFAULT_PADDING_TOKEN,
            oov_token: Optional[str] = DEFAULT_OOV_TOKEN,
            serialization_dir: Optional[str] = None
    ) -> "Vocabulary":
        """
        Construct a vocabulary given a collection of `Instance`'s and some parameters. Then extends
        it with generated vocabularies from pretrained transformers.

        Vocabulary from instances is constructed by passing parameters to :func:`from_instances`,
        and then updated by including merging in vocabularies from
        :func:`from_pretrained_transformer`. See other methods for full descriptions for what the
        other parameters do.

        The `instances` parameters does not get an entry in a typical AllenNLP configuration file,
        other parameters do (if you want non-default parameters).

        # Parameters

        transformers : `Dict[str, str]`
            Dictionary mapping the vocabulary namespaces (keys) to a transformer model name (value).
            Namespaces not included will be ignored.

        # Examples

        You can use this constructor by modifying the following example within your training
        configuration.

        ```jsonnet
        {
            vocabulary: {
                type: 'from_pretrained_transformer_and_instances',
                transformers: {
                    'namespace1': 'bert-base-cased',
                    'namespace2': 'roberta-base',
                },
            }
        }
        ```
        """
        vocab = cls.from_instances(
            instances=instances,
            min_count=min_count,
            max_vocab_size=max_vocab_size,
            non_padded_namespaces=non_padded_namespaces,
            pretrained_files=pretrained_files,
            only_include_pretrained_words=only_include_pretrained_words,
            tokens_to_add=tokens_to_add,
            min_pretrained_embeddings=min_pretrained_embeddings,
            padding_token=padding_token,
            oov_token=oov_token,
            serialization_dir=serialization_dir
        )

        for namespace, model_name in transformers.items():
            transformer_vocab = cls.from_pretrained_transformer(
                model_name=model_name, namespace=namespace
            )
            vocab.extend_from_vocab(transformer_vocab)

        vocab.constructed_from = 'from_pretrained_transformer_and_instances'
        return vocab

    def save_to_files(self, directory: str) -> None:
        """
        Persist this Vocabulary to files, so it can be reloaded later.
        Each _namespace corresponds to one file.

        Adapred from https://github.com/allenai/allennlp/blob/main/allennlp/data/vocabulary.py
        # Parameters
        directory : `str`
            The directory where we save the serialized vocabulary.
        """
        os.makedirs(directory, exist_ok=True)
        if os.listdir(directory):
            logger.warning("Directory %s is not empty", directory)

        # We use a lock file to avoid race conditions where multiple processes
        # might be reading/writing from/to the same vocabulary files at once.
        with FileLock(os.path.join(directory, ".lock")):
            with codecs.open(
                    os.path.join(directory, NAMESPACE_PADDING_FILE), "w", "utf-8"
            ) as namespace_file:
                for namespace_str in self._non_padded_namespaces:
                    print(namespace_str, file=namespace_file)

            for namespace, vocab in self._vocab.items():
                # Each _namespace gets written to its own file, in index order.
                with codecs.open(
                        os.path.join(directory, namespace + ".txt"), "w", "utf-8"
                ) as token_file:
                    mapping = vocab.get_itos()
                    num_tokens = len(mapping)
                    start_index = 1 if mapping[0] == self._padding_token else 0
                    for i in range(start_index, num_tokens):
                        print(mapping[i].replace("\n", "@@NEWLINE@@"), file=token_file)

            with codecs.open(
                    os.path.join(directory, "slices.json"), "w", "utf-8"
            ) as slices_file:
                json.dump(get_slices_if_not_provided(self), slices_file)

    def is_padded(self, namespace: str) -> bool:
        namespace_itos = self._vocab[namespace].get_itos()
        return len(namespace_itos) > 0 and namespace_itos[0] == self._padding_token

    def add_token_to_namespace(self, token: str, namespace: str = DEFAULT_NAMESPACE):
        """
        Add the token if not present and return the index even if token was already in the _namespace.

        :param token: token to be added
        :param namespace: _namespace to add the token to
        :return: index of the token in the _namespace
        """

        if not isinstance(token, str):
            raise ValueError("Vocabulary tokens must be strings. Got %s with type %s" % (repr(token), type(token)))

        self._vocab[namespace].append_token(token)

    def add_tokens_to_namespace(self, tokens: List[str], namespace: str = DEFAULT_NAMESPACE):
        """
        Add the token if not present and return the index even if token was already in the _namespace.

        :param tokens: tokens to be added
        :param namespace: _namespace to add the token to
        :return: index of the token in the _namespace
        """

        if not isinstance(tokens, List):
            raise ValueError("Vocabulary tokens must be passed as a list of strings. Got tokens with type %s" % (
                type(tokens)))

        for token in tokens:
            self._vocab[namespace].append_token(token)

    def add_transformer_vocab(
            self, tokenizer: PreTrainedTokenizer, namespace: str = "tokens"
    ) -> None:
        """
        Copies tokens from a transformer tokenizer's vocabulary into the given namespace.
        """
        try:
            vocab_items = tokenizer.get_vocab().items()
        except NotImplementedError:
            vocab_items = (
                (tokenizer.convert_ids_to_tokens(idx), idx) for idx in range(tokenizer.vocab_size)
            )

        for word, idx in vocab_items:
            self._vocab[namespace].insert_token(token=word, index=idx)

        self._non_padded_namespaces.add(namespace)

    def extend_from_vocab(self, vocab: "Vocabulary") -> None:
        """
        Adds all vocabulary items from all namespaces in the given vocabulary to this vocabulary.
        Useful if you want to load a model and extends its vocabulary from new instances.

        We also add all non-padded namespaces from the given vocabulary to this vocabulary.
        """
        self._non_padded_namespaces.update(vocab._non_padded_namespaces)
        for namespace in vocab.get_namespaces():
            for token in vocab.get_token_to_index_vocabulary(namespace):
                self.add_token_to_namespace(token, namespace)

    def get_index_to_token_vocabulary(self, namespace: str = DEFAULT_NAMESPACE) -> Dict[int, str]:
        if not isinstance(namespace, str):
            raise ValueError(
                "Namespace must be passed as string. Received %s with type %s" % (repr(namespace), type(namespace)))

        return self._vocab[namespace].get_itos()

    def get_token_to_index_vocabulary(self, namespace: str = DEFAULT_NAMESPACE) -> Dict[str, int]:
        if not isinstance(namespace, str):
            raise ValueError(
                "Namespace must be passed as string. Received %s with type %s" % (repr(namespace), type(namespace)))

        return self._vocab[namespace].get_stoi()

    def get_token_index(self, token: str, namespace: str = DEFAULT_NAMESPACE) -> int:
        try:
            return self._vocab[namespace].get_stoi()[token]
        except KeyError:
            try:
                return self._vocab[namespace].get_stoi()[self._oov_token]
            except KeyError:
                raise KeyError("Namespace %s doesn't contain token %s or default OOV token %s" %
                               (namespace, repr(token), repr(self._oov_token)))

    def get_token_from_index(self, index: int, namespace: str = DEFAULT_NAMESPACE) -> str:
        return self._vocab[namespace].get_itos()[index]

    def get_vocab_size(self, namespace: str = DEFAULT_NAMESPACE) -> int:
        return len(self._vocab[namespace].get_itos())

    def get_namespaces(self) -> Set[str]:
        return set(self._vocab.keys())

    def set_from_file(self,
                      filename: str,
                      is_padded: bool = True,
                      oov_token: str = DEFAULT_OOV_TOKEN,
                      namespace: str = "tokens"):
        if is_padded:
            self._vocab[namespace].insert_token(self._padding_token, 0)
        with codecs.open(filename, "r", "utf-8") as input_file:
            lines = _NEW_LINE_REGEX.split(input_file.read())
            # Be flexible about having final newline or not
            if lines and lines[-1] == "":
                lines = lines[:-1]
            for i, line in enumerate(lines):
                index = i + 1 if is_padded else i
                token = line.replace("@@NEWLINE@@", "\n")
                if token == oov_token:
                    token = self._oov_token

                self._vocab[namespace].insert_token(token, index)
        if is_padded:
            assert self._oov_token in self._vocab[namespace].get_itos().values(), "OOV token not found!"

    @classmethod
    @register_arguments
    def from_pretrained_transformer(cls,
                                    model_name: str,
                                    namespace: str = "tokens",
                                    oov_token: Optional[str] = None,
                                    serialization_dir: Optional[str] = None) -> "Vocabulary":
        """
        Initialize a vocabulary from the vocabulary of a pretrained transformer model.
        If `oov_token` is not given, we will try to infer it from the transformer tokenizer.
        """
        from combo.common import cached_transformers

        tokenizer = cached_transformers.get_tokenizer(model_name)
        if oov_token is None:
            if hasattr(tokenizer, "_unk_token"):
                oov_token = tokenizer._unk_token
            elif hasattr(tokenizer, "special_tokens_map"):
                oov_token = tokenizer.special_tokens_map.get("unk_token")
        vocab = cls(non_padded_namespaces=[namespace], oov_token=oov_token, serialization_dir=serialization_dir)
        vocab.add_transformer_vocab(tokenizer, namespace)
        vocab.constructed_from = 'from_pretrained_transformer'
        return vocab

    @classmethod
    @register_arguments
    def from_data_loader_extended(
            cls,
            data_loader: "DataLoader",
            min_count: Dict[str, int] = None,
            max_vocab_size: Union[int, Dict[str, int]] = None,
            non_padded_namespaces: Iterable[str] = DEFAULT_NON_PADDED_NAMESPACES,
            pretrained_files: Optional[Dict[str, str]] = None,
            only_include_pretrained_words: bool = False,
            min_pretrained_embeddings: Dict[str, int] = None,
            padding_token: Optional[str] = DEFAULT_PADDING_TOKEN,
            oov_token: Optional[str] = DEFAULT_OOV_TOKEN,
            serialization_dir: Optional[str] = None
    ) -> "Vocabulary":

        vocab = cls.from_instances_extended(
            instances=data_loader.iter_instances(),
            min_count=min_count,
            max_vocab_size=max_vocab_size,
            non_padded_namespaces=non_padded_namespaces,
            pretrained_files=pretrained_files,
            only_include_pretrained_words=only_include_pretrained_words,
            min_pretrained_embeddings=min_pretrained_embeddings,
            padding_token=padding_token,
            oov_token=oov_token,
            serialization_dir=serialization_dir
        )
        vocab.constructed_from = 'from_data_loader_extended'
        return vocab

    @classmethod
    def from_instances_extended(
            cls,
            instances: Iterable["Instance"],
            min_count: Dict[str, int] = None,
            max_vocab_size: Union[int, Dict[str, int]] = None,
            non_padded_namespaces: Iterable[str] = DEFAULT_NON_PADDED_NAMESPACES,
            pretrained_files: Optional[Dict[str, str]] = None,
            only_include_pretrained_words: bool = False,
            min_pretrained_embeddings: Dict[str, int] = None,
            padding_token: Optional[str] = DEFAULT_PADDING_TOKEN,
            oov_token: Optional[str] = DEFAULT_OOV_TOKEN,
            serialization_dir: Optional[str] = None
    ) -> "Vocabulary":
        """
        Extension to manually fill gaps in missing 'feats_labels'.
        """
        # Load manually tokens from pretrained file (using different strategy
        # - only words add all embedding file, without checking if were seen
        # in any dataset.
        tokens_to_add = None
        if pretrained_files and "tokens" in pretrained_files:
            pretrained_set = set(_read_pretrained_tokens(pretrained_files["tokens"]))
            tokens_to_add = {"tokens": list(pretrained_set)}
            pretrained_files = None

        vocab = cls.from_instances(
            instances=instances,
            min_count=min_count,
            max_vocab_size=max_vocab_size,
            non_padded_namespaces=non_padded_namespaces,
            pretrained_files=pretrained_files,
            only_include_pretrained_words=only_include_pretrained_words,
            tokens_to_add=tokens_to_add,
            min_pretrained_embeddings=min_pretrained_embeddings,
            padding_token=padding_token,
            oov_token=oov_token,
            serialization_dir=serialization_dir
        )
        # Extending vocabulary with features that does not show up explicitly.
        # To know all features we need to read full dataset first.
        # Adding auxiliary '=None' feature for each category is needed
        # to perform classification.
        get_slices_if_not_provided(vocab)
        vocab.constructed_from = 'from_instances_extended'
        return vocab


def get_slices_if_not_provided(vocab: Vocabulary):
    if hasattr(vocab, "slices"):
        return vocab.slices

    if "feats_labels" in vocab.get_namespaces():
        idx2token = vocab.get_index_to_token_vocabulary("feats_labels")
        for _, v in dict(idx2token).items():
            if v not in ["_", "__PAD__"]:
                empty_value = v.split("=")[0] + "=None"
                vocab.add_token_to_namespace(empty_value, "feats_labels")

        slices = {}
        for idx, name in vocab.get_index_to_token_vocabulary("feats_labels").items():
            # There are 2 types features: with (Case=Acc) or without assigment (None).
            # Here we group their indices by name (before assigment sign).
            name = name.split("=")[0]
            if name in slices:
                slices[name].append(idx)
            else:
                slices[name] = [idx]
        vocab.slices = slices
        return vocab.slices
