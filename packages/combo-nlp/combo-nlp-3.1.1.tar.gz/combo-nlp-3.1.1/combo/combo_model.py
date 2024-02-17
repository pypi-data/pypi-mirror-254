"""Main COMBO model."""
from typing import Optional, Dict, Any, List

import numpy
import torch
from overrides import overrides
from torch import Tensor

from combo import data
from combo.config import FromParameters, Registry
from combo.config.from_parameters import register_arguments
from combo.data import Instance
from combo.data.batch import Batch
from combo.data.dataset_loaders.dataset_loader import TensorDict
from combo.modules import TextFieldEmbedder
from combo.modules.lemma import LemmatizerModel
from combo.modules.model import Model
from combo.modules.morpho import MorphologicalFeatures
from combo.modules.parser import DependencyRelationModel
from combo.modules.seq2seq_encoders.seq2seq_encoder import Seq2SeqEncoder
from combo.nn import RegularizerApplicator
from combo.nn import utils
from combo.nn.utils import get_text_field_mask
from combo.predictors import Predictor
from combo.utils import metrics
from combo.utils import ConfigurationError


@Registry.register("semantic_multitask")
class ComboModel(Model, FromParameters):
    """Main COMBO model."""

    @classmethod
    def pass_down_parameter_names(cls) -> List[str]:
        return ['vocabulary', 'serialization_dir', 'model_name']

    @register_arguments
    def __init__(self,
                 vocabulary: data.Vocabulary,
                 loss_weights: Dict[str, float],
                 text_field_embedder: TextFieldEmbedder,
                 seq_encoder: Seq2SeqEncoder,
                 use_sample_weight: bool = True,
                 lemmatizer: LemmatizerModel = None,
                 upos_tagger: MorphologicalFeatures = None,
                 xpos_tagger: MorphologicalFeatures = None,
                 semantic_relation: Predictor = None,
                 morphological_feat: MorphologicalFeatures = None,
                 dependency_relation: DependencyRelationModel = None,
                 enhanced_dependency_relation: DependencyRelationModel = None,
                 regularizer: RegularizerApplicator = None,
                 serialization_dir: Optional[str] = None) -> None:
        super().__init__(vocabulary, regularizer, serialization_dir)

        self.text_field_embedder = text_field_embedder
        self.loss_weights = loss_weights
        self.use_sample_weight = use_sample_weight
        self.seq_encoder = seq_encoder
        self.lemmatizer = lemmatizer
        self.upos_tagger = upos_tagger
        self.xpos_tagger = xpos_tagger
        self.semantic_relation = semantic_relation
        self.morphological_feat = morphological_feat
        self.dependency_relation = dependency_relation
        self.enhanced_dependency_relation = enhanced_dependency_relation
        self._head_sentinel = torch.nn.Parameter(torch.randn([1, 1, self.seq_encoder.get_output_dim()]))
        self.scores = metrics.SemanticMetrics()
        self._partial_losses = None

        self.model_name = getattr(
            getattr(self.text_field_embedder, '_token_embedders', {}).get('token'), 'constructed_args'
        ).get('model_name', '')

    def forward_on_tensors(self,
                           sentence: Dict[str, Dict[str, torch.Tensor]],
                           metadata: List[Dict[str, Any]],
                           upostag: torch.Tensor = None,
                           xpostag: torch.Tensor = None,
                           lemma: Dict[str, Dict[str, torch.Tensor]] = None,
                           feats: torch.Tensor = None,
                           head: torch.Tensor = None,
                           deprel: torch.Tensor = None,
                           semrel: torch.Tensor = None,
                           enhanced_heads: torch.Tensor = None,
                           enhanced_deprels: torch.Tensor = None) -> Dict[str, torch.Tensor]:

        # Prepare masks
        char_mask = sentence["char"]["token_characters"].gt(0)
        word_mask = get_text_field_mask(sentence)

        device = word_mask.device

        # If enabled weight samples loss by log(sentence_length)
        sample_weights = word_mask.sum(-1).float().log() if self.use_sample_weight else None

        encoder_input = self.text_field_embedder(sentence, char_mask=char_mask)
        encoder_emb = self.seq_encoder(encoder_input, word_mask)

        batch_size, _, encoding_dim = encoder_emb.size()

        # Concatenate the head sentinel (ROOT) onto the sentence representation.
        head_sentinel = self._head_sentinel.expand(batch_size, 1, encoding_dim)
        encoder_emb_with_root = torch.cat([head_sentinel, encoder_emb], 1)
        word_mask_with_root = torch.cat([torch.ones((batch_size, 1), device=device), word_mask], 1)

        upos_output = self._optional(self.upos_tagger,
                                     encoder_emb,
                                     mask=word_mask,
                                     labels=upostag,
                                     sample_weights=sample_weights)
        xpos_output = self._optional(self.xpos_tagger,
                                     encoder_emb,
                                     mask=word_mask,
                                     labels=xpostag,
                                     sample_weights=sample_weights)
        semrel_output = self._optional(self.semantic_relation,
                                       encoder_emb,
                                       mask=word_mask,
                                       labels=semrel,
                                       sample_weights=sample_weights)
        morpho_output = self._optional(self.morphological_feat,
                                       encoder_emb,
                                       mask=word_mask,
                                       labels=feats,
                                       sample_weights=sample_weights)
        lemma_output = self._optional(self.lemmatizer,
                                      (encoder_emb, sentence.get("char").get("token_characters")
                                      if sentence.get("char") else None),
                                      mask=word_mask,
                                      labels=lemma.get("char").get("token_characters") if lemma else None,
                                      sample_weights=sample_weights)
        parser_output = self._optional(self.dependency_relation,
                                       encoder_emb_with_root,
                                       returns_tuple=True,
                                       mask=word_mask_with_root,
                                       labels=(deprel, head),
                                       sample_weights=sample_weights)
        enhanced_parser_output = self._optional(self.enhanced_dependency_relation,
                                                encoder_emb_with_root,
                                                returns_tuple=True,
                                                mask=word_mask_with_root,
                                                labels=(enhanced_deprels, head, enhanced_heads),
                                                sample_weights=sample_weights)
        relations_pred, head_pred = parser_output["prediction"]
        enhanced_relations_pred, enhanced_head_pred = enhanced_parser_output["prediction"]
        output = {
            "upostag": upos_output["prediction"],
            "xpostag": xpos_output["prediction"],
            "semrel": semrel_output["prediction"],
            "feats": morpho_output["prediction"],
            "lemma": lemma_output["prediction"],
            "head": head_pred,
            "deprel": relations_pred,
            "enhanced_head": enhanced_head_pred,
            "enhanced_deprel": enhanced_relations_pred,
            "sentence_embedding": torch.max(encoder_emb, dim=1)[0],
            "upostag_token_embedding": upos_output["embedding"],
            "xpostag_token_embedding": xpos_output["embedding"],
            "semrel_token_embedding": semrel_output["embedding"],
            "feats_token_embedding": morpho_output["embedding"],
            "deprel_token_embedding": parser_output["embedding"],
            "deprel_tree_distribution": parser_output["deprel_tree_distribution"],
            "deprel_label_distribution": parser_output["deprel_label_distribution"]
        }

        if "rel_probability" in enhanced_parser_output:
            output["enhanced_deprel_prob"] = enhanced_parser_output["rel_probability"]

        if self._has_labels([upostag, xpostag, lemma, feats, head, deprel, semrel]):

            # Feats mapping
            if self.morphological_feat:
                mapped_gold_labels = []
                for _, cat_indices in self.morphological_feat.slices.items():
                    try:
                        mapped_gold_labels.append(feats[:, :, cat_indices].argmax(dim=-1))
                    except TypeError:
                        raise ConfigurationError('Feats is None - if no feats are provided, the morphological_feat property should be set to None.')

                feats = torch.stack(mapped_gold_labels, dim=-1)

            labels = {
                "upostag": upostag,
                "xpostag": xpostag,
                "semrel": semrel,
                "feats": feats,
                "lemma": lemma.get("char").get("token_characters") if lemma else None,
                "head": head,
                "deprel": deprel,
                "enhanced_head": enhanced_heads,
                "enhanced_deprel": enhanced_deprels,
            }
            self.scores(output, labels, word_mask)
            relations_loss, head_loss = parser_output["loss"]
            enhanced_relations_loss, enhanced_head_loss = enhanced_parser_output["loss"]
            losses = {
                "upostag_loss": upos_output.get("loss"),
                "xpostag_loss": xpos_output.get("loss"),
                "semrel_loss": semrel_output.get("loss"),
                "feats_loss": morpho_output.get("loss"),
                "lemma_loss": lemma_output.get("loss"),
                "head_loss": head_loss,
                "deprel_loss": relations_loss,
                "enhanced_head_loss": enhanced_head_loss,
                "enhanced_deprel_loss": enhanced_relations_loss,
                # Cycle loss is only for the metrics purposes.
                "cycle_loss": parser_output.get("cycle_loss")
            }
            self._partial_losses = losses.copy()
            losses["loss"] = self._calculate_loss(losses)
            output.update(losses)

        return self._clean(output)

    def forward_on_instances(self, instances: List[Instance]) -> List[Dict[str, numpy.ndarray]]:
        batch_size = len(instances)
        with torch.no_grad():
            cuda_device = self._get_prediction_device()
            dataset = Batch(instances)
            dataset.index_instances(self.vocab)
            model_input = utils.move_to_device(dataset.as_tensor_dict(), cuda_device)
            outputs = self.make_output_human_readable(self.forward_on_tensors(**model_input))

            instance_separated_output: List[Dict[str, numpy.ndarray]] = [
                {} for _ in dataset.instances
            ]
            for name, output in list(outputs.items()):
                if isinstance(output, torch.Tensor):
                    # NOTE(markn): This is a hack because 0-dim pytorch tensors are not iterable.
                    # This occurs with batch size 1, because we still want to include the loss in that case.
                    if output.dim() == 0:
                        output = output.unsqueeze(0)

                    if output.size(0) != batch_size:
                        self._maybe_warn_for_unseparable_batches(name)
                        continue
                    output = output.detach().cpu().numpy()
                elif len(output) != batch_size:
                    self._maybe_warn_for_unseparable_batches(name)
                    continue
                for instance_output, batch_element in zip(instance_separated_output, output):
                    instance_output[name] = batch_element
            return instance_separated_output

    @staticmethod
    def _has_labels(labels):
        return any(x is not None for x in labels)

    def _calculate_loss(self, output):
        losses = []
        for name, value in self.loss_weights.items():
            if output.get(f"{name}_loss"):
                losses.append(output[f"{name}_loss"] * value)
        return torch.stack(losses).sum()

    @staticmethod
    def _optional(callable_model: Optional[torch.nn.Module],
                  *args,
                  returns_tuple: bool = False,
                  **kwargs):
        if callable_model:
            return callable_model(*args, **kwargs)
        if returns_tuple:
            return {"prediction": (None, None), "loss": (None, None), "embedding": (None, None)}
        return {"prediction": None, "loss": None, "embedding": None}

    @staticmethod
    def _clean(output):
        for k, v in dict(output).items():
            if v is None:
                del output[k]
        return output

    @overrides
    def get_metrics(self, reset: bool = False) -> Dict[str, float]:
        metrics = self.scores.get_metric(reset)
        if self._partial_losses:
            losses = self._clean(self._partial_losses)
            losses = {f"partial_loss/{k}": v.detach().item() for k, v in losses.items()}
            metrics.update(losses)
        return metrics

    @overrides
    def batch_outputs(self, batch: TensorDict, for_training: bool) -> Dict[str, torch.Tensor]:
        output_dict = self.forward_on_tensors(**batch)

        if for_training:
            try:
                assert "loss" in output_dict
                regularization_penalty = self.get_regularization_penalty()

                if regularization_penalty is not None:
                    output_dict["reg_loss"] = regularization_penalty
                    output_dict["loss"] += regularization_penalty

            except AssertionError:
                if for_training:
                    raise RuntimeError(
                        "The model you are trying to optimize does not contain a"
                        " 'loss' key in the output of model.forward(inputs)."
                    )

        return output_dict

    @overrides
    def forward(self, batch: TensorDict) -> TensorDict:
        return self.batch_outputs(batch, self.training)

    @overrides
    def training_step(self, batch: TensorDict, batch_idx: int) -> Tensor:
        output = self.forward(batch)
        self.log("train_loss", output['loss'], on_step=True, on_epoch=True, prog_bar=True, logger=True)
        return output["loss"]

    @overrides
    def validation_step(self, batch: TensorDict, batch_idx: int) -> Tensor:
        output = self.forward(batch)
        metrics = self.get_metrics()
        for k in metrics.keys():
            if k in self.validation_metrics:
                self.log(k, metrics[k], on_epoch=True, prog_bar=True, logger=True)
        return output["loss"]
