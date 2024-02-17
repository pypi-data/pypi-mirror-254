"""
Author: Łukasz Pszenny
"""
from typing import Optional, List

from combo.common.tqdm import Tqdm
import numpy as np
import pandas as pd
from pathlib import Path

from combo.data import Sentence
from combo.utils import ComboLogger


def extract_combo_matrices(predictions: List[Sentence],
                           serialization_dir: Path,
                           input_data_path: Path,
                           logger: Optional[ComboLogger] = None,
                           logging_prefix: str = ''):
    OUTPUT_DIRECTORY_MATRICES = serialization_dir / "combo_output" / "dependency_tree_matrices"
    OUTPUT_RELATION_LABEL_DISTRIBUTION = serialization_dir / "combo_output" / "label_distribution_matrices"

    meta_ids = []
    meta_splits = []
    meta_file_names = []
    # For saving file names
    tmp_meta_file_names = []

    sentences = []
    sentence_ids = []

    # Create directory if it doesn't exist
    OUTPUT_DIRECTORY_MATRICES.mkdir(parents=True, exist_ok=True)
    OUTPUT_RELATION_LABEL_DISTRIBUTION.mkdir(parents=True, exist_ok=True)

    for sentence_id, predicted_sentence in Tqdm.tqdm(enumerate(predictions)):
        dependency_tree_matrix = predicted_sentence.relation_distribution
        np.savetxt(fname=OUTPUT_DIRECTORY_MATRICES / f'{input_data_path.stem}-{sentence_id}.csv',
                   X=dependency_tree_matrix,
                   delimiter=',')
        tmp_meta_file_names.append(f'{input_data_path.stem}-{sentence_id}.csv')

        # Save relation label matrix
        label_distribution_matrix = predicted_sentence.relation_label_distribution
        np.savetxt(fname=OUTPUT_RELATION_LABEL_DISTRIBUTION / f'{input_data_path.stem}-{sentence_id}.csv',
                   X=label_distribution_matrix,
                   delimiter=',')
        sentences.append(' '.join([t.text for t in predicted_sentence.tokens]))
        sentence_ids.append(sentence_id)
    logger.info(f"\nFinished processing : {input_data_path}", prefix=logging_prefix)

    meta_ids += sentence_ids
    meta_splits += [input_data_path.stem] * len(sentence_ids)
    meta_file_names += tmp_meta_file_names

    meta_data = pd.DataFrame({'split': meta_splits,
                              'sentence_id': meta_ids,
                              'full_sentence': sentences,
                              'file_names': meta_file_names})

    logger.info("Saving metadata", prefix=logging_prefix)
    meta_data.to_csv(serialization_dir / 'metadata.csv', index=False)
    logger.info("Finished processing", prefix=logging_prefix)
