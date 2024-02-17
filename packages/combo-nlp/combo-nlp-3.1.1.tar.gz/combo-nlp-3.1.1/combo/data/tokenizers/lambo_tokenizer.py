from typing import Iterator, List, Optional

from lambo.segmenter.lambo import Lambo

from combo.config import Registry
from combo.config.from_parameters import register_arguments
from combo.data.tokenizers.token import Token
from combo.data.tokenizers.tokenizer import Tokenizer

SPLIT_LEVELS = ["TURN", "SENTENCE", "NONE"]
DEFAULT_SPLIT_LEVEL = "SENTENCE"

IDX = 0


def _token_idx() -> Iterator[int]:
    global IDX
    IDX += 1
    yield IDX


def _reset_idx():
    global IDX
    IDX = 0


def _sentence_tokens(token: Token,
                     split_subwords: Optional[bool] = None) -> List[Token]:
    if split_subwords and len(token.subwords) > 0:
        subword_idxs = [next(_token_idx()) for _ in range(len(token.subwords))]
        multiword = (token.text, (subword_idxs[0], subword_idxs[1]))
        tokens = [Token(idx=s_idx, text=subword, multiword=multiword) for (s_idx, subword)
                  in zip(subword_idxs, token.subwords)]
        return tokens
    else:
        return [Token(idx=next(_token_idx()), text=token.text, subwords=token.subwords)]


@Registry.register('lambo_tokenizer')
class LamboTokenizer(Tokenizer):
    @register_arguments
    def __init__(
            self,
            language: str = "English",
            default_split_level: str = DEFAULT_SPLIT_LEVEL,
            default_split_subwords: bool = True
    ):
        self._language = language
        self.__tokenizer = Lambo.get(language)
        self.__default_split_level = default_split_level.upper()

        self.__default_split_subwords = default_split_subwords

    def tokenize(self,
                 text: str,
                 split_level: Optional[str] = None,
                 split_subwords: Optional[bool] = None,
                 multiwords: Optional[bool] = None) -> List[List[Token]]:
        """
        Simple tokenization - ignoring the sentence splits
        :param text:
        :param split_level: split on turns, sentences, or no splitting (return one list of tokens)
        :param split_subwords: split subwords into separate tokens (e.g. can't into ca, n't)
        :return:
        """
        _reset_idx()
        document = self.__tokenizer.segment(text)
        tokens = []

        split_level = split_level if split_level is not None else self.__default_split_level
        split_subwords = split_subwords if split_subwords is not None else self.__default_split_subwords

        if split_level.upper() == "TURN":
            for turn in document.turns:
                sentence_tokens = []
                for sentence in turn.sentences:
                    for token in sentence.tokens:
                        sentence_tokens.extend(_sentence_tokens(token, split_subwords))
                tokens.append(sentence_tokens)
        elif split_level.upper() == "SENTENCE":
            for turn in document.turns:
                for sentence in turn.sentences:
                    sentence_tokens = []
                    for token in sentence.tokens:
                        sentence_tokens.extend(_sentence_tokens(token, split_subwords))
                    tokens.append(sentence_tokens)
        else:
            for turn in document.turns:
                for sentence in turn.sentences:
                    for token in sentence.tokens:
                        tokens.extend(_sentence_tokens(token, split_subwords))
            tokens = [tokens]

        return tokens

    def segment(self,
                text: str,
                turns: Optional[bool] = None,
                split_subwords: Optional[bool] = None) -> List[List[str]]:
        """
        Full segmentation - segment into sentences and return a list of strings.
        :param text:
        :param turns: segment into sentences by splitting on sentences or on turns. Default: sentences.
        :param split_subwords: split subwords into separate tokens (e.g. can't into ca, n't)
        :return:
        """

        turns = turns if turns is not None else self.__default_split_level.upper() == "TURNS"
        split_subwords = split_subwords if split_subwords is not None else self.__default_split_subwords

        document = self.__tokenizer.segment(text)
        sentences = []
        sentence_tokens = []

        for turn in document.turns:
            if turns:
                sentence_tokens = []
            for sentence in turn.sentences:
                if not turns:
                    sentence_tokens = []
                for token in sentence.tokens:
                    if len(token.subwords) > 0 and split_subwords:
                        sentence_tokens.extend([s for s in token.subwords])
                    else:
                        sentence_tokens.append(token.text)
                if not turns:
                    sentences.append(sentence_tokens)
            if turns:
                sentences.append(sentence_tokens)

        return sentences
