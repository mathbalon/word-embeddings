
from typing import Tuple
from preprocessing import text_preprocessing

def create_word_data_points(text:list, window:int) -> Tuple[list, list]:
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

    return word_pairs, all_words

def create_unique_word_dict(words:list) -> dict:
    unique_words = sorted(list(set(words)))

    words_dict = {}
    for i, word in enumerate(unique_words):
        words_dict.update({
            word: i
        })

    return words_dict
