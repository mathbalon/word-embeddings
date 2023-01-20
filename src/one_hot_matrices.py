import time
import numpy as np

from typing import Tuple
from logger import logger

def create_one_hot_matrices(word_pairs:list, unique_word_dict:dict, logger_path:str) -> Tuple[np.ndarray, np.ndarray]:
    st = time.time()

    qty_words = len(unique_word_dict)
    
    X = []
    Y = []
    
    for i, word_pair in enumerate(word_pairs):
        focus_word_idx = unique_word_dict.get(word_pair[0])
        context_word_idx = unique_word_dict.get(word_pair[1])
        
        X_row = np.zeros(qty_words)
        X_row[focus_word_idx]
        X.append(X_row)
        
        Y_row = np.zeros(qty_words)
        Y_row[context_word_idx]
        Y.append(Y_row)
    
    X = np.asarray(X)
    Y = np.asarray(Y)

    et = time.time()
    
    logger(logger_path, "create_one_hot_matrices", et-st)
    
    return X, Y