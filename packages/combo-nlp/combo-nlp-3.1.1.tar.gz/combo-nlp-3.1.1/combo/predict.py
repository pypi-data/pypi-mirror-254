import logging
import os
import sys
from typing import List, Union, Dict, Any

import numpy as np
import torch
from overrides import overrides

from combo import data
from combo.common import util
from combo.config import Registry
from combo.config.from_parameters import register_arguments
from combo.data import Instance, conllu2sentence, sentence2conllu
from combo.data.dataset_loaders.dataset_loader import TensorDict
from combo.data.dataset_readers.dataset_reader import DatasetReader
from combo.data.instance import JsonDict
from combo.default_model import default_ud_dataset_reader
from combo.modules.archival import load_archive
from combo.predictors import PredictorModule
from combo.utils import download, graph
from combo.modules.model import Model
from combo.data import Token

logger = logging.getLogger(__name__)


@Registry.register('combo')
class COMBO(PredictorModule):
    @register_arguments
    def __init__(self,
                 model: Model,
                 dataset_reader: DatasetReader,
                 batch_size: int = 1024,
                 line_to_conllu: bool = True) -> None:
        super().__init__(model, dataset_reader)
        self.batch_size = batch_size
        self.vocab = model.vocab
        self.dataset_reader.generate_labels = False
        self.dataset_reader.lazy = True
        self.tokenizer = dataset_reader.tokenizer
        self.without_sentence_embedding = False
        self.line_to_conllu = line_to_conllu

    def __call__(self, sentence: Union[str, List[str], List[List[str]], List[data.Sentence]]):
        """Depending on the input uses (or ignores) tokenizer.
        When model isn't only text-based only List[data.Sentence] is possible input.

        * str - tokenizer is used
        * List[str] - tokenizer is used for each string (treated as list of raw sentences)
        * List[List[str]] - tokenizer isn't used (treated as list of tokenized sentences)
        * List[data.Sentence] - tokenizer isn't used (treated as list of tokenized sentences)

        :param sentence: sentence(s) representation
        :return: Sentence or List[Sentence] depending on the input
        """
        try:
            return self.predict(sentence)
        except Exception as e:
            logger.error(e)
            logger.error('Exiting.')
            sys.exit(1)

    def forward(self, inputs: TensorDict, training: bool = False) -> Dict[str, torch.Tensor]:
        return self.batch_outputs(inputs, training)

    def training_step(self, batch: TensorDict) -> Dict[str, torch.Tensor]:
        self._model.train()
        output = self.forward(batch)
        output['loss'].backward()
        return output

    def configure_optimizers(self) -> Any:
        pass

    def predict(self,
                sentence: Union[str, List[str], List[List[str]], List[data.Sentence]],
                **kwargs):
        if isinstance(sentence, str):
            sentence = self.dataset_reader.tokenizer.tokenize(sentence, **kwargs)

        if isinstance(sentence, list):
            if len(sentence) == 0:
                return []
            example = sentence[0]
            sentences = sentence
            if isinstance(example, Token) or (isinstance(example, list) and isinstance(example[0], Token)):
                result = []
                sentences = [self._to_input_json(s) for s in sentences]
                for sentences_batch in util.lazy_groups_of(sentences, self.batch_size):
                    sentences_batch = self.predict_batch_json(sentences_batch)
                    result.extend(sentences_batch)
                return result
            elif isinstance(example, data.Sentence):
                result = []
                sentences = [self._to_input_instance(s) for s in sentences]
                for sentences_batch in util.lazy_groups_of(sentences, self.batch_size):
                    sentences_batch = self.predict_batch_instance(sentences_batch)
                    result.extend(sentences_batch)
                return result
            else:
                raise ValueError("List must have either sentences as str, List[str] or Sentence object.")
        else:
            raise ValueError("Input must be either string or list of strings.")

    @overrides
    def predict_batch_instance(self, instances: List[Instance]) -> List[data.Sentence]:
        sentences = []
        predictions = super().predict_batch_instance(instances)
        for prediction, instance in zip(predictions, instances):
            (tree, sentence_embedding, embeddings,
             relation_distribution, relation_label_distribution) = self._predictions_as_tree(prediction, instance)
            sentence = conllu2sentence(
                tree, sentence_embedding, embeddings,
                relation_distribution=relation_distribution,
                relation_label_distribution=relation_label_distribution
            )
            sentences.append(sentence)
        return sentences

    @overrides
    def predict_batch_json(self, inputs: List[JsonDict]) -> List[data.Sentence]:
        instances = self._batch_json_to_instances(inputs)
        sentences = self.predict_batch_instance(instances)
        return sentences

    @overrides
    def predict_instance(self, instance: Instance, serialize: bool = True) -> data.Sentence:
        predictions = super().predict_instance(instance)
        (tree, sentence_embedding, embeddings,
         relation_distribution, relation_label_distribution) = self._predictions_as_tree(predictions, instance)
        return conllu2sentence(
            tree, sentence_embedding, embeddings,
            relation_distribution=relation_distribution,
            relation_label_distribution=relation_label_distribution
        )

    @overrides
    def predict_json(self, inputs: JsonDict) -> data.Sentence:
        instance = self._json_to_instance(inputs)
        return self.predict_instance(instance)

    @overrides
    def _json_to_instance(self, json_dict) -> Instance:
        sentence = json_dict["sentence"]
        # TODO: tokenize EVERYTHING, even if a list is passed?
        if isinstance(sentence, str):
            tokens = [t.text for t in self.tokenizer.tokenize(json_dict["sentence"])]
        elif isinstance(sentence, list):
            tokens = sentence
        else:
            raise ValueError("Input must be either string or list of strings.")
        return self.dataset_reader.text_to_instance(tokens)

    @overrides
    def load_line(self, line: str) -> JsonDict:
        return self._to_input_json(line.replace("\n", "").strip())

    # outputs should be api.Sentence
    @overrides
    def dump_line(self, outputs: Any) -> str:
        # Check whether serialized (str) tree or token's list
        # Serialized tree has already separators between lines
        if self.without_sentence_embedding:
            outputs.sentence_embedding = []
        if self.line_to_conllu:
            return sentence2conllu(outputs, keep_semrel=getattr(self.dataset_reader, 'use_sem', False)).serialize()
        else:
            return outputs.to_json()

    @staticmethod
    def _to_input_json(sentence: str):
        return {"sentence": sentence}

    def _to_input_instance(self, sentence: data.Sentence) -> Instance:
        return self.dataset_reader.text_to_instance(sentence2conllu(sentence))

    def _predictions_as_tree(self, predictions: Dict[str, Any], instance: Instance):
        tree = instance.fields["metadata"]["input"]
        field_names = instance.fields["metadata"]["field_names"]
        tree_tokens = [t for t in tree if isinstance(t["idx"], int) or isinstance(t["idx"], tuple)]
        embeddings = {t["idx"]: {} for t in tree}
        deprel_tree_distribution = None
        deprel_label_distribution = None
        for field_name in field_names:
            if field_name not in predictions:
                continue
            if field_name == "deprel":
                sentence_length = len(tree_tokens)
                deprel_tree_distribution = np.matrix(predictions["deprel_tree_distribution"])[:sentence_length + 1,
                                           :sentence_length + 1]
                deprel_label_distribution = np.matrix(predictions["deprel_label_distribution"])[:sentence_length, :]
            field_predictions = predictions[field_name]
            for idx, token in enumerate(tree_tokens):
                if field_name in {"xpostag", "upostag", "semrel", "deprel"}:
                    value = self.vocab.get_token_from_index(field_predictions[idx], field_name + "_labels")
                    setattr(token, field_name, value)
                    embeddings[token["idx"]][field_name] = predictions[f"{field_name}_token_embedding"][idx]
                elif field_name == "head":
                    setattr(token, field_name, int(field_predictions[idx]))
                elif field_name == "deps":
                    # Handled after every other decoding
                    continue

                elif field_name == "feats":
                    slices = self._model.morphological_feat.slices
                    features = []
                    prediction = field_predictions[idx]
                    for (cat, cat_indices), pred_idx in zip(slices.items(), prediction):
                        if cat not in ["__PAD__", "_"]:
                            value = self.vocab.get_token_from_index(cat_indices[pred_idx],
                                                                    field_name + "_labels")
                            # Exclude auxiliary values
                            if "=None" not in value:
                                features.append(value)
                    if len(features) == 0:
                        field_value = "_"
                    else:
                        lowercase_features = [f.lower() for f in features]
                        arg_indices = sorted(range(len(lowercase_features)), key=lowercase_features.__getitem__)
                        field_value = "|".join(np.array(features)[arg_indices].tolist())

                    setattr(token, field_name, field_value)
                    embeddings[token["idx"]][field_name] = predictions[f"{field_name}_token_embedding"][idx]
                elif field_name == "lemma":
                    prediction = field_predictions[idx]
                    word_chars = []
                    for char_idx in prediction[1:-1]:
                        pred_char = self.vocab.get_token_from_index(char_idx, "lemma_characters")

                        if pred_char == "__END__":
                            break
                        elif pred_char == "__PAD__":
                            continue
                        elif "_" in pred_char:
                            pred_char = "?"

                        word_chars.append(pred_char)
                    setattr(token, field_name, "".join(word_chars))
                else:
                    raise NotImplementedError(f"Unknown field name {field_name}!")

        if "enhanced_head" in predictions and predictions["enhanced_head"]:
            # TODO off-by-one hotfix, refactor
            sentence_length = len(tree_tokens)
            h = np.array(predictions["enhanced_head"])[:sentence_length, :sentence_length]
            h = np.concatenate((h[-1:], h[:-1]))
            r = np.array(predictions["enhanced_deprel_prob"])[:sentence_length, :sentence_length, :]
            r = np.concatenate((r[-1:], r[:-1]))

            graph.graph_and_tree_merge(
                tree_arc_scores=predictions["head"][:sentence_length],
                tree_rel_scores=predictions["deprel"][:sentence_length],
                graph_arc_scores=h,
                graph_rel_scores=r,
                idx2label=self.vocab.get_index_to_token_vocabulary("deprel_labels"),
                label2idx=self.vocab.get_token_to_index_vocabulary("deprel_labels"),
                graph_idx2label=self.vocab.get_index_to_token_vocabulary("enhanced_deprel_labels"),
                graph_label2idx=self.vocab.get_token_to_index_vocabulary("enhanced_deprel_labels"),
                tokens=tree_tokens
            )

            empty_tokens = graph.restore_collapse_edges(tree_tokens)
            tree.tokens.extend(empty_tokens)

        return tree, predictions["sentence_embedding"], embeddings, \
               deprel_tree_distribution, deprel_label_distribution

    @classmethod
    def from_pretrained(cls,
                        path: str,
                        batch_size: int = 1024,
                        cuda_device: int = -1):
        if os.path.exists(path):
            model_path = path
        else:
            try:
                logger.debug("Downloading model.")
                model_path = download.download_file(path)
            except Exception as e:
                logger.error(e)
                raise e

        archive = load_archive(model_path, cuda_device=cuda_device)
        model = archive.model
        dataset_reader = archive.dataset_reader or default_ud_dataset_reader(archive.config.get("model_name"))
        return cls(model, dataset_reader, batch_size)
