import sys
import yaml
from create_unique_word_dict import create_unique_word_dict

from create_word_data_points import create_word_data_points

with open("data/" + sys.argv[1], "r") as file:
    text = file.readlines()

with open("settings.yml", "r") as file:
    settings = yaml.load(file, Loader=yaml.FullLoader)
    
word_pairs, all_words = create_word_data_points(text, settings["window"])

unique_word_dict = create_unique_word_dict(all_words)
