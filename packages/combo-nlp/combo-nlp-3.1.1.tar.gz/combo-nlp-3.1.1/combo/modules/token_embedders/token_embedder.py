from typing import Optional, NamedTuple

import h5py
import torch
from overrides import overrides
from torchtext.vocab import Vectors, GloVe, FastText, CharNGram

from combo import nn
from combo.config import FromParameters, Registry
from combo.config.from_parameters import register_arguments
from combo.data import Vocabulary
from combo.nn.utils import tiny_value_of_dtype, uncombine_initial_dims, combine_initial_dims
from combo.modules.module import Module
from combo.utils import ConfigurationError
from combo.models.time_distributed import TimeDistributed


class TokenEmbedder(Module, FromParameters):
    def __init__(self):
        super(TokenEmbedder, self).__init__()

    def get_output_dim(self) -> int:
        raise NotImplementedError()

    def forward(self,
                x: torch.Tensor,
                char_mask: Optional[torch.BoolTensor] = None) -> torch.Tensor:
        raise NotImplementedError()


@Registry.register("embedding")
class Embedding(TokenEmbedder):
    """
    A more featureful embedding module than the default in Pytorch.  Adds the ability to:

        1. embed higher-order inputs
        2. pre-specify the weight matrix
        3. use a non-trainable embedding
        4. project the resultant embeddings to some other dimension (which only makes sense with
           non-trainable embeddings).

    Note that if you are using our data API and are trying to embed a
    [`TextField`](../../data/fields/text_field.md), you should use a
    [`TextFieldEmbedder`](../text_field_embedders/text_field_embedder.md) instead of using this directly.

    Registered as a `TokenEmbedder` with name "embedding".

    # Parameters

    num_embeddings : `int`
        Size of the dictionary of embeddings (vocabulary size).
    embedding_dim : `int`
        The size of each embedding vector.
    projection_dim : `int`, optional (default=`None`)
        If given, we add a projection layer after the embedding layer.  This really only makes
        sense if `trainable` is `False`.
    weight : `torch.FloatTensor`, optional (default=`None`)
        A pre-initialised weight matrix for the embedding lookup, allowing the use of
        pretrained vectors.
    padding_index : `int`, optional (default=`None`)
        If given, pads the output with zeros whenever it encounters the index.
    trainable : `bool`, optional (default=`True`)
        Whether or not to optimize the embedding parameters.
    max_norm : `float`, optional (default=`None`)
        If given, will renormalize the embeddings to always have a norm lesser than this
    norm_type : `float`, optional (default=`2`)
        The p of the p-norm to compute for the max_norm option
    scale_grad_by_freq : `bool`, optional (default=`False`)
        If given, this will scale gradients by the frequency of the words in the mini-batch.
    sparse : `bool`, optional (default=`False`)
        Whether or not the Pytorch backend should use a sparse representation of the embedding weight.
    vocab_namespace : `str`, optional (default=`None`)
        In case of fine-tuning/transfer learning, the model's embedding matrix needs to be
        extended according to the size of extended-vocabulary. To be able to know how much to
        extend the embedding-matrix, it's necessary to know which vocab_namspace was used to
        construct it in the original training. We store vocab_namespace used during the original
        training as an attribute, so that it can be retrieved during fine-tuning.
    pretrained_file : `str`, optional (default=`None`)
        Path to a file of word vectors to initialize the embedding matrix. It can be the
        path to a local file or a URL of a (cached) remote file. Two formats are supported:
            * hdf5 file - containing an embedding matrix in the form of a torch.Tensor;
            * text file - an utf-8 encoded text file with space separated fields.
    vocabulary : `Vocabulary`, optional (default = `None`)
        Used to construct an embedding from a pretrained file.

        In a typical AllenNLP configuration file, this parameter does not get an entry under the
        "embedding", it gets specified as a top-level parameter, then is passed in to this module
        separately.

    # Returns

    An Embedding module.
    """

    @register_arguments
    def __init__(
            self,
            embedding_dim: int,
            num_embeddings: int = None,
            projection_dim: int = None,
            weight: torch.FloatTensor = None,
            padding_index: int = None,
            trainable: bool = True,
            max_norm: float = None,
            norm_type: float = 2.0,
            scale_grad_by_freq: bool = False,
            sparse: bool = False,
            vocab_namespace: str = "tokens",
            pretrained_file: str = None,
            vocabulary: Vocabulary = None,
    ) -> None:
        super().__init__()

        if num_embeddings is None and vocabulary is None:
            raise ConfigurationError(
                "Embedding must be constructed with either num_embeddings or a vocabulary."
            )

        _vocab_namespace: Optional[str] = vocab_namespace
        if num_embeddings is None:
            num_embeddings = vocabulary.get_vocab_size(_vocab_namespace)  # type: ignore
        else:
            # If num_embeddings is present, set default namespace to None so that extend_vocab
            # call doesn't misinterpret that some namespace was originally used.
            _vocab_namespace = None  # type: ignore

        self.num_embeddings = num_embeddings
        self.padding_index = padding_index
        self.max_norm = max_norm
        self.norm_type = norm_type
        self.scale_grad_by_freq = scale_grad_by_freq
        self.sparse = sparse
        self._vocab_namespace = _vocab_namespace
        self._pretrained_file = pretrained_file

        self.output_dim = projection_dim or embedding_dim

        if weight is not None and pretrained_file:
            raise ConfigurationError(
                "Embedding was constructed with both a weight and a pretrained file."
            )

        elif pretrained_file is not None:

            if vocabulary is None:
                raise ConfigurationError(
                    "To construct an Embedding from a pretrained file, you must also pass a vocabulary."
                )

            # If we're loading a saved model, we don't want to actually read a pre-trained
            # embedding file - the embeddings will just be in our saved weights, and we might not
            # have the original embedding file anymore, anyway.

            # TODO: having to pass tokens here is SUPER gross, but otherwise this breaks the
            # extend_vocab method, which relies on the value of vocab_namespace being None
            # to infer at what stage the embedding has been constructed. Phew.
            weight = _read_pretrained_embeddings_file(
                pretrained_file, embedding_dim, vocabulary, vocab_namespace
            )
            self.weight = torch.nn.Parameter(weight, requires_grad=trainable)

        elif weight is not None:
            self.weight = torch.nn.Parameter(weight, requires_grad=trainable)

        else:
            weight = torch.FloatTensor(num_embeddings, embedding_dim)
            self.weight = torch.nn.Parameter(weight, requires_grad=trainable)
            torch.nn.init.xavier_uniform_(self.weight)

        # Whatever way we have constructed the embedding, it should be consistent with
        # num_embeddings and embedding_dim.
        if self.weight.size() != (num_embeddings, embedding_dim):
            raise ConfigurationError(
                "A weight matrix was passed with contradictory embedding shapes."
            )

        if self.padding_index is not None:
            self.weight.data[self.padding_index].fill_(0)

        if projection_dim:
            self._projection = torch.nn.Linear(embedding_dim, projection_dim)
        else:
            self._projection = None

    def get_output_dim(self) -> int:
        return self.output_dim

    def forward(self, tokens: torch.Tensor) -> torch.Tensor:
        # tokens may have extra dimensions (batch_size, d1, ..., dn, sequence_length),
        # but embedding expects (batch_size, sequence_length), so pass tokens to
        # util.combine_initial_dims (which is a no-op if there are no extra dimensions).
        # Remember the original size.
        original_size = tokens.size()
        tokens = combine_initial_dims(tokens)

        embedded = embedding(
            tokens,
            self.weight,
            padding_idx=self.padding_index,
            max_norm=self.max_norm,
            norm_type=self.norm_type,
            scale_grad_by_freq=self.scale_grad_by_freq,
            sparse=self.sparse,
        )

        # Now (if necessary) add back in the extra dimensions.
        embedded = uncombine_initial_dims(embedded, original_size)

        if self._projection:
            projection = self._projection
            for _ in range(embedded.dim() - 2):
                projection = TimeDistributed(projection)
            embedded = projection(embedded)
        return embedded

    def extend_vocab(
            self,
            extended_vocab: Vocabulary,
            vocab_namespace: str = None,
            extension_pretrained_file: str = None,
            model_path: str = None,
    ):
        """
        Extends the embedding matrix according to the extended vocabulary.
        If extension_pretrained_file is available, it will be used for initializing the new words
        embeddings in the extended vocabulary; otherwise we will check if _pretrained_file attribute
        is already available. If none is available, they will be initialized with xavier uniform.

        # Parameters

        extended_vocab : `Vocabulary`
            Vocabulary extended from original vocabulary used to construct
            this `Embedding`.
        vocab_namespace : `str`, (optional, default=`None`)
            In case you know what vocab_namespace should be used for extension, you
            can pass it. If not passed, it will check if vocab_namespace used at the
            time of `Embedding` construction is available. If so, this namespace
            will be used or else extend_vocab will be a no-op.
        extension_pretrained_file : `str`, (optional, default=`None`)
            A file containing pretrained embeddings can be specified here. It can be
            the path to a local file or an URL of a (cached) remote file. Check format
            details in `from_params` of `Embedding` class.
        model_path : `str`, (optional, default=`None`)
            Path traversing the model attributes upto this embedding module.
            Eg. "_text_field_embedder.token_embedder_tokens". This is only useful
            to give a helpful error message when extend_vocab is implicitly called
            by train or any other command.
        """
        # Caveat: For allennlp v0.8.1 and below, we weren't storing vocab_namespace as an attribute,
        # knowing which is necessary at time of embedding vocabulary extension. So old archive models are
        # currently unextendable.

        vocab_namespace = vocab_namespace or self._vocab_namespace
        if not vocab_namespace:
            # It's not safe to default to "tokens" or any other namespace.
            logger.info(
                "Loading a model trained before embedding extension was implemented; "
                "pass an explicit vocabulary namespace if you want to extend the vocabulary."
            )
            return

        extended_num_embeddings = extended_vocab.get_vocab_size(vocab_namespace)
        if extended_num_embeddings == self.num_embeddings:
            # It's already been extended. No need to initialize / read pretrained file in first place (no-op)
            return

        if extended_num_embeddings < self.num_embeddings:
            raise ConfigurationError(
                f"Size of namespace, {vocab_namespace} for extended_vocab is smaller than "
                f"embedding. You likely passed incorrect vocabulary or namespace for extension."
            )

        # Case 1: user passed extension_pretrained_file and it's available.
        if extension_pretrained_file and is_url_or_existing_file(extension_pretrained_file):
            # Don't have to do anything here, this is the happy case.
            pass
        # Case 2: user passed extension_pretrained_file and it's not available
        elif extension_pretrained_file:
            raise ConfigurationError(
                f"You passed pretrained embedding file {extension_pretrained_file} "
                f"for model_path {model_path} but it's not available."
            )
        # Case 3: user didn't pass extension_pretrained_file, but pretrained_file attribute was
        # saved during training and is available.
        elif is_url_or_existing_file(self._pretrained_file):
            extension_pretrained_file = self._pretrained_file
        # Case 4: no file is available, hope that pretrained embeddings weren't used in the first place and warn
        elif self._pretrained_file is not None:
            # Warn here instead of an exception to allow a fine-tuning even without the original pretrained_file
            logger.warning(
                f"Embedding at model_path, {model_path} cannot locate the pretrained_file. "
                f"Originally pretrained_file was at '{self._pretrained_file}'."
            )
        else:
            # When loading a model from archive there is no way to distinguish between whether a pretrained-file
            # was or wasn't used during the original training. So we leave an info here.
            logger.info(
                "If you are fine-tuning and want to use a pretrained_file for "
                "embedding extension, please pass the mapping by --embedding-sources argument."
            )

        embedding_dim = self.weight.data.shape[-1]
        if not extension_pretrained_file:
            extra_num_embeddings = extended_num_embeddings - self.num_embeddings
            extra_weight = torch.FloatTensor(extra_num_embeddings, embedding_dim)
            torch.nn.init.xavier_uniform_(extra_weight)
        else:
            # It's easiest to just reload the embeddings for the entire vocabulary,
            # then only keep the ones we need.
            whole_weight = _read_pretrained_embeddings_file(
                extension_pretrained_file, embedding_dim, extended_vocab, vocab_namespace
            )
            extra_weight = whole_weight[self.num_embeddings:, :]

        device = self.weight.data.device
        extended_weight = torch.cat([self.weight.data, extra_weight.to(device)], dim=0)
        self.weight = torch.nn.Parameter(extended_weight, requires_grad=self.weight.requires_grad)
        self.num_embeddings = extended_num_embeddings


def _read_pretrained_embeddings_file(
        file_uri: str, embedding_dim: int, vocab: Vocabulary, namespace: str = "tokens"
) -> torch.FloatTensor:
    """
    Returns and embedding matrix for the given vocabulary using the pretrained embeddings
    contained in the given file. Embeddings for tokens not found in the pretrained embedding file
    are randomly initialized using a normal distribution with mean and standard deviation equal to
    those of the pretrained embeddings.

    We support two file formats:

        * text format - utf-8 encoded text file with space separated fields: [word] [dim 1] [dim 2] ...
          The text file can eventually be compressed, and even resides in an archive with multiple files.
          If the file resides in an archive with other files, then `embeddings_filename` must
          be a URI "(archive_uri)#file_path_inside_the_archive"

        * hdf5 format - hdf5 file containing an embedding matrix in the form of a torch.Tensor.

    If the filename ends with '.hdf5' or '.h5' then we load from hdf5, otherwise we assume
    text format.

    # Parameters

    file_uri : `str`, required.
        It can be:

        * a file system path or a URL of an eventually compressed text file or a zip/tar archive
          containing a single file.

        * URI of the type `(archive_path_or_url)#file_path_inside_archive` if the text file
          is contained in a multi-file archive.

    vocabulary : `Vocabulary`, required.
        A Vocabulary object.
    namespace : `str`, (optional, default=`"tokens"`)
        The namespace of the vocabulary to find pretrained embeddings for.
    trainable : `bool`, (optional, default=`True`)
        Whether or not the embedding parameters should be optimized.

    # Returns

    A weight matrix with embeddings initialized from the read file.  The matrix has shape
    `(vocabulary.get_vocab_size(namespace), embedding_dim)`, where the indices of words appearing in
    the pretrained embedding file are initialized to the pretrained embedding value.
    """
    file_ext = get_file_extension(file_uri)
    if file_ext in [".h5", ".hdf5"]:
        return _read_embeddings_from_hdf5(file_uri, embedding_dim, vocab, namespace)

    return _read_embeddings_from_text_file(file_uri, embedding_dim, vocab, namespace)


def _read_embeddings_from_text_file(
        file_uri: str, embedding_dim: int, vocab: Vocabulary, namespace: str = "tokens"
) -> torch.FloatTensor:
    """
    Read pre-trained word vectors from an eventually compressed text file, possibly contained
    inside an archive with multiple files. The text file is assumed to be utf-8 encoded with
    space-separated fields: [word] [dim 1] [dim 2] ...

    Lines that contain more numerical tokens than `embedding_dim` raise a warning and are skipped.

    The remainder of the docstring is identical to `_read_pretrained_embeddings_file`.
    """
    tokens_to_keep = set(vocab.get_index_to_token_vocabulary(namespace).values())
    vocab_size = vocab.get_vocab_size(namespace)
    embeddings = {}

    # First we read the embeddings from the file, only keeping vectors for the words we need.
    logger.info("Reading pretrained embeddings from file")

    with EmbeddingsTextFile(file_uri) as embeddings_file:
        for line in Tqdm.tqdm(embeddings_file):
            token = line.split(" ", 1)[0]
            if token in tokens_to_keep:
                fields = line.rstrip().split(" ")
                if len(fields) - 1 != embedding_dim:
                    # Sometimes there are funny unicode parsing problems that lead to different
                    # fields lengths (e.g., a word with a unicode space character that splits
                    # into more than one column).  We skip those lines.  Note that if you have
                    # some kind of long header, this could result in all of your lines getting
                    # skipped.  It's hard to check for that here; you just have to look in the
                    # embedding_misses_file and at the model summary to make sure things look
                    # like they are supposed to.
                    logger.warning(
                        "Found line with wrong number of dimensions (expected: %d; actual: %d): %s",
                        embedding_dim,
                        len(fields) - 1,
                        line,
                    )
                    continue

                vector = numpy.asarray(fields[1:], dtype="float32")
                embeddings[token] = vector

    if not embeddings:
        raise ConfigurationError(
            "No embeddings of correct dimension found; you probably "
            "misspecified your embedding_dim parameter, or didn't "
            "pre-populate your Vocabulary"
        )

    all_embeddings = numpy.asarray(list(embeddings.values()))
    embeddings_mean = float(numpy.mean(all_embeddings))
    embeddings_std = float(numpy.std(all_embeddings))
    # Now we initialize the weight matrix for an embedding layer, starting with random vectors,
    # then filling in the word vectors we just read.
    logger.info("Initializing pre-trained embedding layer")
    embedding_matrix = torch.FloatTensor(vocab_size, embedding_dim).normal_(
        embeddings_mean, embeddings_std
    )
    num_tokens_found = 0
    index_to_token = vocab.get_index_to_token_vocabulary(namespace)
    for i in range(vocab_size):
        token = index_to_token[i]

        # If we don't have a pre-trained vector for this word, we'll just leave this row alone,
        # so the word has a random initialization.
        if token in embeddings:
            embedding_matrix[i] = torch.FloatTensor(embeddings[token])
            num_tokens_found += 1
        else:
            logger.debug(
                "Token %s was not found in the embedding file. Initialising randomly.", token
            )

    logger.info(
        "Pretrained embeddings were found for %d out of %d tokens", num_tokens_found, vocab_size
    )

    return embedding_matrix


def _read_embeddings_from_hdf5(
        embeddings_filename: str, embedding_dim: int, vocabulary: Vocabulary, namespace: str = "tokens"
) -> torch.FloatTensor:
    """
    Reads from a hdf5 formatted file. The embedding matrix is assumed to
    be keyed by 'embedding' and of size `(num_tokens, embedding_dim)`.
    """
    with h5py.File(embeddings_filename, "r") as fin:
        embeddings = fin["embedding"][...]

    if list(embeddings.shape) != [vocabulary.get_vocab_size(namespace), embedding_dim]:
        raise ConfigurationError(
            "Read shape {0} embeddings from the file, but expected {1}".format(
                list(embeddings.shape), [vocabulary.get_vocab_size(namespace), embedding_dim]
            )
        )

    return torch.FloatTensor(embeddings)


def format_embeddings_file_uri(
        main_file_path_or_url: str, path_inside_archive: Optional[str] = None
) -> str:
    if path_inside_archive:
        return "({})#{}".format(main_file_path_or_url, path_inside_archive)
    return main_file_path_or_url


class EmbeddingsFileURI(NamedTuple):
    main_file_uri: str
    path_inside_archive: Optional[str] = None


@Registry.register('base_token_embedder')
class TorchEmbedder(TokenEmbedder):
    @register_arguments
    def __init__(self,
                 num_TokenEmbedders: int,
                 TokenEmbedder_dim: int,
                 padding_idx: Optional[int] = None,
                 max_norm: Optional[float] = None,
                 norm_type: float = 2.,
                 scale_grad_by_freq: bool = False,
                 sparse: bool = False,
                 vocab_namespace: str = "tokens",
                 vocabulary: Vocabulary = None,
                 weight: Optional[torch.Tensor] = None,
                 trainable: bool = True,
                 projection_dim: Optional[int] = None):
        super(TorchEmbedder, self).__init__()
        self._TokenEmbedder_dim = TokenEmbedder_dim
        self._TokenEmbedder = nn.TokenEmbedder(num_TokenEmbedders=num_TokenEmbedders,
                                               TokenEmbedder_dim=TokenEmbedder_dim,
                                               padding_idx=padding_idx,
                                               max_norm=max_norm,
                                               norm_type=norm_type,
                                               scale_grad_by_freq=scale_grad_by_freq,
                                               sparse=sparse)
        self.__vocab_namespace = vocab_namespace
        self.__vocab = vocabulary

        if weight is not None:
            if weight.shape() != (num_TokenEmbedders, TokenEmbedder_dim):
                raise ConfigurationError(
                    "Weight matrix must be of shape (num_TokenEmbedders, TokenEmbedder_dim)." +
                    f"Got: ({weight.shape()})"
                )

            self.__weight = torch.nn.Parameter(weight, requires_grad=trainable)
        else:
            self.__weight = torch.nn.Parameter(torch.FloatTensor(num_TokenEmbedders, TokenEmbedder_dim),
                                               requires_grad=trainable)
            torch.nn.init.xavier_uniform_(self.__weight)

        if padding_idx is not None:
            self.__weight.data[padding_idx].fill_(0)

        if projection_dim:
            self._projection = torch.nn.Linear(TokenEmbedder_dim, projection_dim)
            self.output_dim = projection_dim
        else:
            self._projection = None
            self.output_dim = TokenEmbedder_dim

    @overrides
    def forward(self,
                x: torch.Tensor,
                char_mask: Optional[torch.BoolTensor] = None) -> torch.Tensor:
        embedded = self._TokenEmbedder(x)
        if self._projection:
            projection = self._projection
            for p in range(embedded.dim() - 2):
                projection = TimeDistributed(p)
            embedded = projection(embedded)
        return embedded


@Registry.register('torchtext_vectors_embedder')
class _TorchtextVectorsEmbedder(TokenEmbedder):
    """
    Torchtext Vectors object wrapper
    """

    @register_arguments
    def __init__(self,
                 torchtext_embedder: Vectors,
                 lower_case_backup: bool = False):
        """
        :param torchtext_embedder: Torchtext Vectors object
        :param lower_case_backup: whether to look up the token in the
        lower case. Default: False.
        """
        super(_TorchtextVectorsEmbedder, self).__init__()
        self.__torchtext_embedder = torchtext_embedder
        self.__lower_case_backup = lower_case_backup

    @overrides
    def get_output_dim(self) -> int:
        return len(self.__torchtext_embedder)

    @overrides
    def forward(self,
                x: torch.Tensor,
                char_mask: Optional[torch.BoolTensor] = None) -> torch.Tensor:
        return self.__torchtext_embedder.get_vecs_by_tokens(x, self.__lower_case_backup)


@Registry.register('glove42b')
class GloVe42BEmbedder(_TorchtextVectorsEmbedder):
    @register_arguments
    def __init__(self, dim: int = 300):
        super(GloVe42BEmbedder, self).__init__(GloVe("42B", dim))


@Registry.register('glove840b')
class GloVe840BEmbedder(_TorchtextVectorsEmbedder):
    @register_arguments
    def __init__(self, dim: int = 300):
        super(GloVe840BEmbedder, self).__init__(GloVe("840B", dim))


@Registry.register('glove_twitter27b')
class GloVeTwitter27BEmbedder(_TorchtextVectorsEmbedder):
    @register_arguments
    def __init__(self, dim: int = 300):
        super(GloVeTwitter27BEmbedder, self).__init__(GloVe("twitter.27B", dim))


@Registry.register('glove6b')
class GloVe6BEmbedder(_TorchtextVectorsEmbedder):
    @register_arguments
    def __init__(self, dim: int = 300):
        super(GloVe6BEmbedder, self).__init__(GloVe("6B", dim))


@Registry.register('fast_text')
class FastTextEmbedder(_TorchtextVectorsEmbedder):
    @register_arguments
    def __init__(self, language: str = "en"):
        super(FastTextEmbedder, self).__init__(FastText(language))


@Registry.register('char_ngram')
class CharNGramEmbedder(_TorchtextVectorsEmbedder):
    @register_arguments
    def __init__(self):
        super(CharNGramEmbedder, self).__init__(CharNGram())


@Registry.register('feats_token_embedder')
class FeatsTokenEmbedder(TorchEmbedder):
    @register_arguments
    def __init__(self,
                 num_TokenEmbedders: int,
                 TokenEmbedder_dim: int,
                 padding_idx: Optional[int] = None,
                 max_norm: Optional[float] = None,
                 norm_type: float = 2.,
                 scale_grad_by_freq: bool = False,
                 sparse: bool = False,
                 vocab_namespace: str = "feats",
                 vocabulary: Vocabulary = None,
                 weight: Optional[torch.Tensor] = None,
                 trainable: bool = True):
        super(FeatsTokenEmbedder, self).__init__(num_TokenEmbedders,
                                                 TokenEmbedder_dim,
                                                 padding_idx,
                                                 max_norm,
                                                 norm_type,
                                                 scale_grad_by_freq,
                                                 sparse,
                                                 vocab_namespace,
                                                 vocabulary,
                                                 weight,
                                                 trainable)

    @overrides
    def forward(self,
                x: torch.Tensor,
                char_mask: Optional[torch.BoolTensor] = None) -> torch.Tensor:
        mask = x.gt(0)
        x = super().forward(x)
        return x.sum(dim=-2) / (
            (mask.sum(dim=-1) + tiny_value_of_dtype(torch.float)).unsqueeze(dim=-1)
        )
