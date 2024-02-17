"""
A default model and classes, mainly for testing the package
"""
from typing import Optional

from combo.data import DatasetReader
from combo.data.batch import Batch
from combo.data.dataset_loaders import SimpleDataLoader, DataLoader
from combo.data.dataset_readers import UniversalDependenciesDatasetReader
from combo.data.token_indexers import TokenConstPaddingCharactersIndexer, \
    TokenFeatsIndexer, SingleIdTokenIndexer, PretrainedTransformerFixedMismatchedIndexer
from combo.data.tokenizers import CharacterTokenizer
from combo.data.vocabulary import Vocabulary
from combo.combo_model import ComboModel
from combo.models.encoder import ComboEncoder, ComboStackedBidirectionalLSTM
from combo.models.dilated_cnn import DilatedCnnEncoder
from combo.modules.lemma import LemmatizerModel
from combo.modules.morpho import MorphologicalFeatures
from combo.modules.parser import DependencyRelationModel, HeadPredictionModel
from combo.modules.text_field_embedders import BasicTextFieldEmbedder
from combo.modules.token_embedders import CharacterBasedWordEmbedder, TransformersWordEmbedder
from combo.nn.activations import ReLUActivation, TanhActivation, LinearActivation
from combo.modules import FeedForwardPredictor
from combo.nn.base import Linear
from combo.nn.regularizers.regularizers import L2Regularizer
from combo.nn import RegularizerApplicator
from combo.data import Tokenizer, LamboTokenizer


def default_character_indexer(namespace=None,
                              min_padding_length: int = 32) -> TokenConstPaddingCharactersIndexer:
    if namespace:
        return TokenConstPaddingCharactersIndexer(
            tokenizer=CharacterTokenizer(end_tokens=["__END__"],
                                         start_tokens=["__START__"]),
            min_padding_length=min_padding_length,
            namespace=namespace
        )
    else:
        return TokenConstPaddingCharactersIndexer(
            tokenizer=CharacterTokenizer(end_tokens=["__END__"],
                                         start_tokens=["__START__"]),
            min_padding_length=min_padding_length
        )


def default_ud_dataset_reader(pretrained_transformer_name: str,
                              tokenizer: Optional[Tokenizer] = None) -> UniversalDependenciesDatasetReader:
    tokenizer = tokenizer or LamboTokenizer()
    return UniversalDependenciesDatasetReader(
        features=["token", "char"],
        lemma_indexers={
            "char": default_character_indexer("lemma_characters")
        },
        targets=["deprel", "head", "upostag", "lemma", "feats", "xpostag"],
        token_indexers={
            "char": default_character_indexer(),
            "feats": TokenFeatsIndexer(),
            "lemma": default_character_indexer(),
            "token": PretrainedTransformerFixedMismatchedIndexer(pretrained_transformer_name),
            "upostag": SingleIdTokenIndexer(
                feature_name="pos_",
                namespace="upostag"
            ),
            "xpostag": SingleIdTokenIndexer(
                feature_name="tag_",
                namespace="xpostag"
            )
        },
        use_sem=False,
        tokenizer=tokenizer
    )


def default_data_loader(dataset_reader: DatasetReader,
                        file_path: str,
                        batch_size: int = 16,
                        batches_per_epoch: int = 4) -> SimpleDataLoader:
    return SimpleDataLoader.from_dataset_reader(dataset_reader,
                                                data_path=file_path,
                                                batch_size=batch_size,
                                                batches_per_epoch=batches_per_epoch,
                                                shuffle=True,
                                                collate_fn=lambda instances: Batch(instances).as_tensor_dict())


def default_vocabulary(data_loader: DataLoader) -> Vocabulary:
    return Vocabulary.from_data_loader_extended(
        data_loader,
        non_padded_namespaces=['head_labels'],
        only_include_pretrained_words=False,
        oov_token='_',
        padding_token='__PAD__'
    )


def default_model(pretrained_transformer_name: str, vocabulary: Vocabulary) -> ComboModel:
    return ComboModel(
        vocabulary=vocabulary,
        dependency_relation=DependencyRelationModel(
            vocabulary=vocabulary,
            dependency_projection_layer=Linear(
                activation=TanhActivation(),
                dropout_rate=0.25,
                in_features=1024,
                out_features=128
            ),
            head_predictor=HeadPredictionModel(
                cycle_loss_n=0,
                dependency_projection_layer=Linear(
                    activation=TanhActivation(),
                    in_features=1024,
                    out_features=512
                ),
                head_projection_layer=Linear(
                    activation=TanhActivation(),
                    in_features=1024,
                    out_features=512
                )
            ),
            head_projection_layer=Linear(
                activation=TanhActivation(),
                dropout_rate=0.25,
                in_features=1024,
                out_features=128
            ),
            vocab_namespace="deprel_labels"
        ),
        lemmatizer=LemmatizerModel(
            vocabulary=vocabulary,
            activations=[ReLUActivation(), ReLUActivation(), ReLUActivation(), LinearActivation()],
            char_vocab_namespace="token_characters",
            dilation=[1, 2, 4, 1],
            embedding_dim=256,
            filters=[256, 256, 256],
            input_projection_layer=Linear(
                activation=TanhActivation(),
                dropout_rate=0.25,
                in_features=1024,
                out_features=32
            ),
            kernel_size=[3, 3, 3, 1],
            lemma_vocab_namespace="lemma_characters",
            padding=[1, 2, 4, 0],
            stride=[1, 1, 1, 1]
        ),
        loss_weights={
            "deprel": 0.8,
            "feats": 0.2,
            "head": 0.2,
            "lemma": 0.05,
            "semrel": 0.05,
            "upostag": 0.05,
            "xpostag": 0.05
        },
        morphological_feat=MorphologicalFeatures(
            vocabulary=vocabulary,
            activations=[TanhActivation(), LinearActivation()],
            dropout=[0.25, 0.],
            hidden_dims=[128],
            input_dim=1024,
            num_layers=2,
            vocab_namespace="feats_labels"
        ),
        regularizer=RegularizerApplicator([
            (".*conv1d.*", L2Regularizer(1e-6)),
            (".*forward.*", L2Regularizer(1e-6)),
            (".*backward.*", L2Regularizer(1e-6)),
            (".*char_embed.*", L2Regularizer(1e-5))
        ]),
        seq_encoder=ComboEncoder(
            layer_dropout_probability=0.33,
            stacked_bilstm=ComboStackedBidirectionalLSTM(
                hidden_size=512,
                input_size=164,
                layer_dropout_probability=0.33,
                num_layers=2,
                recurrent_dropout_probability=0.33
            )
        ),
        text_field_embedder=BasicTextFieldEmbedder(
            token_embedders={
                "char": CharacterBasedWordEmbedder(
                    vocabulary=vocabulary,
                    dilated_cnn_encoder=DilatedCnnEncoder(
                        activations=[ReLUActivation(), ReLUActivation(), LinearActivation()],
                        dilation=[1, 2, 4],
                        filters=[512, 256, 64],
                        input_dim=64,
                        kernel_size=[3, 3, 3],
                        padding=[1, 2, 4],
                        stride=[1, 1, 1],
                    ),
                    embedding_dim=64
                ),
                "token": TransformersWordEmbedder(pretrained_transformer_name, projection_dim=100)
            }
        ),
        upos_tagger=FeedForwardPredictor.from_vocab(
            vocabulary=vocabulary,
            activations=[TanhActivation(), LinearActivation()],
            dropout=[0.25, 0.],
            hidden_dims=[64],
            input_dim=1024,
            num_layers=2,
            vocab_namespace="upostag_labels"
        ),
        xpos_tagger=FeedForwardPredictor.from_vocab(
            vocabulary=vocabulary,
            activations=[TanhActivation(), LinearActivation()],
            dropout=[0.25, 0.],
            hidden_dims=[64],
            input_dim=1024,
            num_layers=2,
            vocab_namespace="xpostag_labels"
        )
    )
