import time

from typing import Tuple
from preprocessing import text_preprocessing
from logger import logger

def create_word_data_points(text:list, window:int, logger_path:str) -> Tuple[list, list]:
    st = time.time()

    word_pairs = []
    all_words = []
    
    for sentence in text:
        sentence = text_preprocessing(sentence)
        
        words = sentence.split()
        
        all_words += words
        
        for i, word in enumerate(words):
            for w in range(window):
                if i + 1 + w < len(words):
                    word_pairs.append([word] + [words[(i + 1 + w)]])

                if i - w - 1 >= 0:
                    word_pairs.append([word] + [words[(i - w - 1)]])
    
    et = time.time()

    logger(logger_path, "create_word_data_points", et-st)

    return word_pairs, all_words

def create_unique_word_dict(words:list, logger_path:str) -> dict:
    st = time.time()

    unique_words = sorted(list(set(words)))

    words_dict = {}
    for i, word in enumerate(unique_words):
        words_dict.update({
            word: i
        })

    et = time.time()
    
    logger(logger_path, "create_unique_word_dict", et-st)

    return words_dict
