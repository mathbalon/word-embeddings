import sys
import yaml
import time

from model import create_neural_network_model, plot_results
from one_hot_matrices import create_one_hot_matrices
from logger import init_logger_file

from word_data_points import create_word_data_points, create_unique_word_dict

with open("data/" + sys.argv[1], "r") as file:
    text = file.readlines()

with open("settings.yml", "r") as file:
    settings = yaml.load(file, Loader=yaml.FullLoader)

logger_file_name = init_logger_file(settings)

word_pairs, all_words = create_word_data_points(text, settings["window"], logger_file_name)

unique_word_dict = create_unique_word_dict(all_words, logger_file_name)

X, Y = create_one_hot_matrices(word_pairs, unique_word_dict, logger_file_name)

weights = create_neural_network_model(X, Y, settings, logger_file_name)

plot_results(weights, unique_word_dict, logger_file_name)
