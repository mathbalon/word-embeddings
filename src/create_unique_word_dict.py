def create_unique_word_dict(words:list) -> dict:
    unique_words = sorted(list(set(words)))

    words_dict = {}
    for i, word in enumerate(unique_words):
        words_dict.update({
            word: i
        })

    return words_dict