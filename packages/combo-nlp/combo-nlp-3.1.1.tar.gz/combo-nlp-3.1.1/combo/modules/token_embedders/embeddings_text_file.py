"""
Adapted from AllenNLP
https://github.com/allenai/allennlp/blob/main/allennlp/modules/token_embedders/embedding.py
"""
import io
import itertools
import logging
import re
import tarfile
import zipfile
from typing import Any, Iterator, Tuple, NamedTuple, Optional, BinaryIO, Sequence

from combo.utils.typing import cast
from combo.utils.file_utils import cached_path, get_file_extension

logger = logging.getLogger(__name__)


class EmbeddingsFileURI(NamedTuple):
    main_file_uri: str
    path_inside_archive: Optional[str] = None


def format_embeddings_file_uri(
    main_file_path_or_url: str, path_inside_archive: Optional[str] = None
) -> str:
    if path_inside_archive:
        return "({})#{}".format(main_file_path_or_url, path_inside_archive)
    return main_file_path_or_url


def parse_embeddings_file_uri(uri: str) -> "EmbeddingsFileURI":
    match = re.fullmatch(r"\((.*)\)#(.*)", uri)
    if match:
        fields = cast(Tuple[str, str], match.groups())
        return EmbeddingsFileURI(*fields)
    else:
        return EmbeddingsFileURI(uri, None)


class EmbeddingsTextFile(Iterator[str]):
    """
    Utility class for opening embeddings text files. Handles various compression formats,
    as well as context management.

    # Parameters

    file_uri : `str`
        It can be:

        * a file system path or a URL of an eventually compressed text file or a zip/tar archive
          containing a single file.
        * URI of the type `(archive_path_or_url)#file_path_inside_archive` if the text file
          is contained in a multi-file archive.

    encoding : `str`
    cache_dir : `str`
    """

    DEFAULT_ENCODING = "utf-8"

    def __init__(
            self, file_uri: str, encoding: str = DEFAULT_ENCODING, cache_dir: str = None
    ) -> None:

        self.uri = file_uri
        self._encoding = encoding
        self._cache_dir = cache_dir
        self._archive_handle: Any = None  # only if the file is inside an archive

        main_file_uri, path_inside_archive = parse_embeddings_file_uri(file_uri)
        main_file_local_path = cached_path(main_file_uri, cache_dir=cache_dir)

        if zipfile.is_zipfile(main_file_local_path):  # ZIP archive
            self._open_inside_zip(main_file_uri, path_inside_archive)

        elif tarfile.is_tarfile(main_file_local_path):  # TAR archive
            self._open_inside_tar(main_file_uri, path_inside_archive)

        else:  # all the other supported formats, including uncompressed files
            if path_inside_archive:
                raise ValueError("Unsupported archive format: %s" + main_file_uri)

            # All the python packages for compressed files share the same interface of io.open
            extension = get_file_extension(main_file_uri)

            # Some systems don't have support for all of these libraries, so we import them only
            # when necessary.
            package = None
            if extension in [".txt", ".vec"]:
                package = io
            elif extension == ".gz":
                import gzip

                package = gzip
            elif extension == ".bz2":
                import bz2

                package = bz2
            elif extension == ".xz":
                import lzma

                package = lzma

            if package is None:
                logger.warning(
                    'The embeddings file has an unknown file extension "%s". '
                    "We will assume the file is an (uncompressed) text file",
                    extension,
                )
                package = io

            self._handle = package.open(  # type: ignore
                main_file_local_path, "rt", encoding=encoding
            )

        # To use this with tqdm we'd like to know the number of tokens. It's possible that the
        # first line of the embeddings file contains this: if it does, we want to start iteration
        # from the 2nd line, otherwise we want to start from the 1st.
        # Unfortunately, once we read the first line, we cannot move back the file iterator
        # because the underlying file may be "not seekable"; we use itertools.chain instead.
        first_line = next(self._handle)  # this moves the iterator forward
        self.num_tokens = EmbeddingsTextFile._get_num_tokens_from_first_line(first_line)
        if self.num_tokens:
            # the first line is a header line: start iterating from the 2nd line
            self._iterator = self._handle
        else:
            # the first line is not a header line: start iterating from the 1st line
            self._iterator = itertools.chain([first_line], self._handle)

    def _open_inside_zip(self, archive_path: str, member_path: Optional[str] = None) -> None:
        cached_archive_path = cached_path(archive_path, cache_dir=self._cache_dir)
        archive = zipfile.ZipFile(cached_archive_path, "r")
        if member_path is None:
            members_list = archive.namelist()
            member_path = self._get_the_only_file_in_the_archive(members_list, archive_path)
        member_path = cast(str, member_path)
        member_file = cast(BinaryIO, archive.open(member_path, "r"))
        self._handle = io.TextIOWrapper(member_file, encoding=self._encoding)
        self._archive_handle = archive

    def _open_inside_tar(self, archive_path: str, member_path: Optional[str] = None) -> None:
        cached_archive_path = cached_path(archive_path, cache_dir=self._cache_dir)
        archive = tarfile.open(cached_archive_path, "r")
        if member_path is None:
            members_list = archive.getnames()
            member_path = self._get_the_only_file_in_the_archive(members_list, archive_path)
        member_path = cast(str, member_path)
        member = archive.getmember(member_path)  # raises exception if not present
        member_file = cast(BinaryIO, archive.extractfile(member))
        self._handle = io.TextIOWrapper(member_file, encoding=self._encoding)
        self._archive_handle = archive

    def read(self) -> str:
        return "".join(self._iterator)

    def readline(self) -> str:
        return next(self._iterator)

    def close(self) -> None:
        self._handle.close()
        if self._archive_handle:
            self._archive_handle.close()

    def __enter__(self) -> "EmbeddingsTextFile":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close()

    def __iter__(self) -> "EmbeddingsTextFile":
        return self

    def __next__(self) -> str:
        return next(self._iterator)

    def __len__(self) -> Optional[int]:
        if self.num_tokens:
            return self.num_tokens
        raise AttributeError(
            "an object of type EmbeddingsTextFile implements `__len__` only if the underlying "
            "text file declares the number of tokens (i.e. the number of lines following)"
            "in the first line. That is not the case of this particular instance."
        )

    @staticmethod
    def _get_the_only_file_in_the_archive(members_list: Sequence[str], archive_path: str) -> str:
        if len(members_list) > 1:
            raise ValueError(
                "The archive %s contains multiple files, so you must select "
                "one of the files inside providing a uri of the type: %s."
                % (
                    archive_path,
                    format_embeddings_file_uri("path_or_url_to_archive", "path_inside_archive"),
                )
            )
        return members_list[0]

    @staticmethod
    def _get_num_tokens_from_first_line(line: str) -> Optional[int]:
        """This function takes in input a string and if it contains 1 or 2 integers, it assumes the
        largest one it the number of tokens. Returns None if the line doesn't match that pattern."""
        fields = line.split(" ")
        if 1 <= len(fields) <= 2:
            try:
                int_fields = [int(x) for x in fields]
            except ValueError:
                return None
            else:
                num_tokens = max(int_fields)
                logger.info(
                    "Recognized a header line in the embedding file with number of tokens: %d",
                    num_tokens,
                )
                return num_tokens
        return None
