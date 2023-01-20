import sys
import yaml

from model import create_neural_network_model, plot_results
from one_hot_matrices import create_one_hot_matrices

from word_data_points import create_word_data_points, create_unique_word_dict

with open("data/" + sys.argv[1], "r") as file:
    text = file.readlines()

with open("settings.yml", "r") as file:
    settings = yaml.load(file, Loader=yaml.FullLoader)
    
word_pairs, all_words = create_word_data_points(text, settings["window"])

unique_word_dict = create_unique_word_dict(all_words)

X, Y = create_one_hot_matrices(word_pairs, unique_word_dict)

weights = create_neural_network_model(X, Y, settings["embed_size"])

plot_results(weights, unique_word_dict)
