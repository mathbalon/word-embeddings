import sys
import yaml

from logger import init_logger_file
from model import create_neural_network_model, plot_results
from one_hot_matrices import create_one_hot_matrices
from word_data_points import create_unique_word_dict, create_word_data_points

file_name = sys.argv[1]

with open("data/" + file_name, "r") as file:
    text = file.readlines()

with open("settings.yml", "r") as file:
    settings = yaml.load(file, Loader=yaml.FullLoader)

logger_path = init_logger_file(file_name, settings)

word_pairs, all_words = create_word_data_points(text, settings["window"], logger_path)

unique_word_dict = create_unique_word_dict(all_words, logger_path)

X, Y = create_one_hot_matrices(word_pairs, unique_word_dict, logger_path)

weights = create_neural_network_model(X, Y, settings, logger_path)

plot_results(weights, unique_word_dict, logger_path)
