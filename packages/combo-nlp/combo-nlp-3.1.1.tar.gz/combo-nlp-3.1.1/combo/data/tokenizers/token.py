"""
Adapted from AllenNLP
https://github.com/allenai/allennlp/blob/main/allennlp/data/tokenizers/token_class.py
"""
from typing import Any, Dict, List, Optional, Tuple, Union
import logging
from dataclasses import dataclass, field
import conllu

logger = logging.getLogger(__name__)


def _assert_none_or_type(value: Any, type_to_check: type) -> bool:
    return value is None or isinstance(value, type_to_check)


@dataclass(init=False, repr=False)
class Token:
    __slots__ = [
        "text",
        "idx",
        "lemma",
        "upostag",
        "xpostag",
        "entity_type",
        "feats",
        "head",
        "deprel",
        "deps",
        "misc",
        "subwords",
        "multiword",
        "semrel",
        "embeddings",
        "text_id",
        "type_id"
    ]

    text: Optional[str]
    idx: Optional[Union[int, Tuple]]
    lemma: Optional[str]
    upostag: Optional[str]  # Coarse-grained part of speech? pos_?
    xpostag: Optional[str]  # Fine-grained part of speech? tag_ ?
    entity_type: Optional[str]
    feats: Optional[str]
    head: Optional[int]
    deprel: Optional[str]  # dep_ ?
    deps: Optional[str]
    misc: Optional[str]
    subwords: Optional[List[str]]
    multiword: Optional[Tuple[str, Tuple[int, int]]]
    semrel: Optional[str]
    embeddings: Dict[str, List[float]]
    text_id: Optional[int]
    type_id: Optional[int]

    def __init__(self,
                 text: str = None,
                 idx: Union[int, Tuple] = None,
                 lemma: str = None,
                 upostag: str = None,
                 xpostag: str = None,
                 entity_type: str = None,
                 feats: Optional[Dict[str, str]] = None,
                 head: int = None,
                 deprel: str = None,
                 deps: str = None,
                 misc: str = None,
                 subwords: List[str] = None,
                 multiword: Tuple[str, Tuple[int, int]] = None,
                 semrel: str = None,
                 embeddings: Dict[str, List[float]] = None,
                 text_id: int = None,
                 type_id: int = None,) -> None:
        _assert_none_or_type(text, str)

        self.text = text
        self.idx = idx
        self.lemma = lemma
        self.upostag = upostag
        self.xpostag = xpostag
        self.entity_type = entity_type
        self.feats = feats
        self.head = head
        self.deprel = deprel
        self.deps = deps
        self.misc = misc
        self.subwords = subwords if subwords else []
        self.multiword = multiword
        self.semrel = semrel

        if embeddings is None:
            # what?
            self.embeddings = field(default_factory=list, repr=False)
        else:
            self.embeddings = embeddings

        self.text_id = text_id
        self.type_id = type_id

    def as_dict(self, semrel: bool = True) -> Dict[str, Any]:
        repr = {}
        repr_keys = [
            'text', 'idx', 'lemma', 'upostag', 'xpostag', 'entity_type', 'feats',
            'head', 'deprel', 'deps', 'misc'
        ]
        for rk in repr_keys:
            repr[rk] = self.__getattribute__(rk)

        if semrel:
            repr['semrel'] = self.semrel

        return repr

    def __str__(self):
        return str(self.text)

    def __repr__(self):
        return self.__str__()

    def ensure_text(self) -> str:
        """
        Return the `text` field, raising an exception if it's `None`.
        """
        if self.text is None:
            raise ValueError("Unexpected null text for token")
        else:
            return self.text

    def get(self, key, default=None):
        if hasattr(self, key):
            return getattr(self, key)
        else:
            return default

    def __getitem__(self, key):
        return getattr(self, key)

    def __show__(self):
        return (
            f"{self.text} "
            f"(idx: {self.idx}) "
            f"(lemma: {self.lemma}) "
            f"(upostag: {self.upostag}) "
            f"(xpostag: {self.xpostag}) "
            f"(entity_type: {self.entity_type}) "
            f"(feats: {self.feats}) "
            f"(head: {self.head}) "
            f"(deprel: {self.deprel}) "
            f"(deps: {self.deps}) "
            f"(misc: {self.misc}) "
            f"(subwords: {','.join(self.subwords)})"
            f"(semrel: {self.semrel}) "
            f"(embeddings: {self.embeddings}) "
            f"(text_id: {self.text_id}) "
            f"(type_id: {self.type_id}) "
        )

    @classmethod
    def from_conllu_token(cls,
                          conllu_token: conllu.models.Token):
        return cls(text=conllu_token.get("token"),
                   idx=conllu_token.get("id"),
                   lemma=conllu_token.get("lemma"),
                   upostag=conllu_token.get("upos"),
                   xpostag=conllu_token.get("xpos"),
                   feats=conllu_token.get("feats"),
                   head=conllu_token.get("head"),
                   deprel=conllu_token.get("deprel"),
                   deps=conllu_token.get("deps"),
                   misc=conllu_token.get("misc"))
