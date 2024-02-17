import collections
import dataclasses
import json
from dataclasses import dataclass, field
from typing import List, Dict, Any

import conllu
from conllu.models import Metadata
from overrides import overrides

from combo.data.tokenizers import Token


@dataclass
class Sentence:
    tokens: List[Token] = field(default_factory=list)
    sentence_embedding: List[float] = field(default_factory=list, repr=False)
    relation_distribution: List[float] = field(default_factory=list, repr=False)
    relation_label_distribution: List[float] = field(default_factory=list, repr=False)
    metadata: Dict[str, Any] = field(default_factory=collections.OrderedDict)

    def to_json(self):
        return json.dumps({
            "tokens": [dataclasses.asdict(t) for t in self.tokens],
            "sentence_embedding": self.sentence_embedding,
            "relation_distribution": self.relation_distribution,
            "relation_label_distribution": self.relation_label_distribution,
            "metadata": self.metadata
        })

    def __len__(self):
        return len(self.tokens)


class _TokenList(conllu.models.TokenList):

    @overrides
    def __repr__(self):
        return 'TokenList<' + ', '.join(token['text'] for token in self) + '>'


def sentence2conllu(sentence: Sentence, keep_semrel: bool = True) -> conllu.models.TokenList:
    tokens = []
    used_multiwords = set()
    for token in sentence.tokens:
        if token.multiword and token.multiword not in used_multiwords:
            tokens.append(collections.OrderedDict(Token(idx=token.multiword[1], text=token.multiword[0]).as_dict(keep_semrel)))
            used_multiwords.add(token.multiword)
        token_dict = collections.OrderedDict(token.as_dict(keep_semrel))
        tokens.append(token_dict)
    # Range tokens must be tuple not list, this is conllu library requirement
    for t in tokens:
        if type(t["idx"]) == list:
            t["idx"] = tuple(t["idx"])
        if t["deps"]:
            for dep in t["deps"]:
                if len(dep) > 1 and type(dep[1]) == list:
                    dep[1] = tuple(dep[1])
    return _TokenList(tokens=tokens,
                      metadata=sentence.metadata if sentence.metadata is None else Metadata())

def serialize_field(field: Any) -> str:
    if field is None:
        return '_'

    if isinstance(field, dict):
        if field == {}:
            return '_'

        fields = []
        for key, value in field.items():
            if value is None:
                value = "_"
            if value == "":
                fields.append(key)
                continue

            fields.append('='.join((key, value)))

        return '|'.join(fields)

    if isinstance(field, tuple):
        return "-".join([serialize_field(item) for item in field])

    if isinstance(field, list):
        if len(field[0]) != 2:
            raise ValueError("Can't serialize '{}', invalid format".format(field))
        return "|".join([serialize_field(value) + ":" + str(key) for key, value in field])

    return "{}".format(field)

def serialize_token_list(tokenlist: conllu.models.TokenList) -> str:
    KEYS_ORDER = ['idx', 'text', 'lemma', 'upostag', 'xpostag', 'feats', 'head', 'deprel', 'deps']
    lines = []

    if tokenlist.metadata:
        for key, value in tokenlist.metadata.items():
            if value:
                line = f"# {key} = {value}"
            else:
                line = f"# {key}"
            lines.append(line)

    for token_data in tokenlist:
        line = '\t'.join(serialize_field(token_data[k]) for k in KEYS_ORDER)
        serialized_misc = serialize_field(token_data['misc'])
        serialized_entity_type = serialize_field(token_data['entity_type'])
        if serialized_misc == '_' and serialized_entity_type == '_':
            serialized_last_column = '_'
        elif serialized_misc == '_':
            serialized_last_column = serialized_entity_type
        elif serialized_entity_type == '_':
            serialized_last_column = serialized_misc
        else:
            serialized_last_column = serialized_entity_type + ' | ' + serialized_misc

        line += '\t' + serialized_last_column
        lines.append(line)

    return '\n'.join(lines) + "\n\n"

def tokens2conllu(tokens: List[str]) -> conllu.models.TokenList:
    return _TokenList(
        [collections.OrderedDict({"id": idx, "token": token}) for
         idx, token
         in enumerate(tokens, start=1)],
        metadata=collections.OrderedDict()
    )


def conllu2sentence(tokens: List[Token],
                    sentence_embedding=None, embeddings=None,
                    metadata=None,
                    relation_distribution=None,
                    relation_label_distribution=None) -> Sentence:
    embeddings = embeddings or {}
    if relation_distribution is None:
        relation_distribution = []
    if relation_label_distribution is None:
        relation_label_distribution = []
    if sentence_embedding is None:
        sentence_embedding = []
    if embeddings:
        for token in tokens:
            token.embeddings = embeddings[token["idx"]]
    return Sentence(
        tokens=tokens,
        sentence_embedding=sentence_embedding,
        relation_distribution=relation_distribution,
        relation_label_distribution=relation_label_distribution,
        metadata=metadata
    )
