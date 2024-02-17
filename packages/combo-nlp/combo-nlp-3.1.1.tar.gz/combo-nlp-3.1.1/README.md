# Installation

Currently, COMBO is available as a git repository. In the cloned repository directory:

## (Recommended) Create a Conda environment

```bash
conda create -n combo python=3.9.16
```

Make sure to install at least python 3.9.16.

Not all of the requirements are available on `conda`, so `pip` is also required.

```bash
conda install pip
```

## Automatic installation

```bash
pip install combo-nlp
```

## Source installation

Install the requirements using the `setup.py` file.

```bash
pip install -e .
```

## Use COMBO as a python package

```python
import combo
```

Pretrained model usage:

```python
from combo.predict import COMBO
c = COMBO.from_pretrained('polish-herbert-base-ud213')
prediction = c("To jest przykładowe zdanie. To jest drugie zdanie.")

# Display the first sentence predictions
print("{:15} {:15} {:10} {:10} {:10}".format('TOKEN', 'LEMMA', 'UPOS', 'HEAD', 'DEPREL'))
for token in prediction[0].tokens:
    print("{:15} {:15} {:10} {:10} {:10}".format(token.text, token.lemma, token.upostag, token.head, token.deprel))
```

Example output:
```
TOKEN           LEMMA           UPOS       HEAD       DEPREL
To              to              AUX                 4 cop       
jest            być             AUX                 4 cop       
przykładowe     przykładowy     ADJ                 4 amod      
zdanie          zdanie          NOUN                0 root      
.               .               PUNCT               4 punct  
```

## Use COMBO CLI

The minimal training example (make sure to download some conllu training and validation files)

```bash
combo --mode train --training_data_path <training conllu> --validation_data_path <validation conllu>
```

You can find more examples in ```docs/Training.md```

## COMBO tutorial

We encourage you to use the [beginner's tutorial](https://colab.research.google.com/drive/1-yYwOb9uOTygGhHdaJK_LKedHf_RnvYa) (colab notebook).

## Details

- [**Configuration**](docs/Configuration.md)
- [**Training**](docs/Training.md)
- [**Prediction**](docs/Prediction.md)
- [**Troubleshooting**](docs/Troubleshooting.md)

## Citing

If you use COMBO in your research, please cite [COMBO: State-of-the-Art Morphosyntactic Analysis](https://aclanthology.org/2021.emnlp-demo.7)
```bibtex
@inproceedings{klimaszewski-wroblewska-2021-combo-state,
    title = "{COMBO}: State-of-the-Art Morphosyntactic Analysis",
    author = "Klimaszewski, Mateusz  and
      Wr{\'o}blewska, Alina",
    booktitle = "Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing: System Demonstrations",
    month = nov,
    year = "2021",
    address = "Online and Punta Cana, Dominican Republic",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.emnlp-demo.7",
    pages = "50--62",
    abstract = "We introduce COMBO {--} a fully neural NLP system for accurate part-of-speech tagging, morphological analysis, lemmatisation, and (enhanced) dependency parsing. It predicts categorical morphosyntactic features whilst also exposes their vector representations, extracted from hidden layers. COMBO is an easy to install Python package with automatically downloadable pre-trained models for over 40 languages. It maintains a balance between efficiency and quality. As it is an end-to-end system and its modules are jointly trained, its training is competitively fast. As its models are optimised for accuracy, they achieve often better prediction quality than SOTA. The COMBO library is available at: https://gitlab.clarin-pl.eu/syntactic-tools/combo.",
}
```

If you use an EUD module in your research, please cite [COMBO: A New Module for EUD Parsing](https://aclanthology.org/2021.iwpt-1.16)
```bibtex
@inproceedings{klimaszewski-wroblewska-2021-combo,
    title = "{COMBO}: A New Module for {EUD} Parsing",
    author = "Klimaszewski, Mateusz  and
      Wr{\'o}blewska, Alina",
    booktitle = "Proceedings of the 17th International Conference on Parsing Technologies and the IWPT 2021 Shared Task on Parsing into Enhanced Universal Dependencies (IWPT 2021)",
    month = aug,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.iwpt-1.16",
    doi = "10.18653/v1/2021.iwpt-1.16",
    pages = "158--166",
    abstract = "We introduce the COMBO-based approach for EUD parsing and its implementation, which took part in the IWPT 2021 EUD shared task. The goal of this task is to parse raw texts in 17 languages into Enhanced Universal Dependencies (EUD). The proposed approach uses COMBO to predict UD trees and EUD graphs. These structures are then merged into the final EUD graphs. Some EUD edge labels are extended with case information using a single language-independent expansion rule. In the official evaluation, the solution ranked fourth, achieving an average ELAS of 83.79{\%}. The source code is available at https://gitlab.clarin-pl.eu/syntactic-tools/combo.",
}
```
