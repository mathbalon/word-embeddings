import sys
import yaml

with open("data/" + sys.argv[1], "r") as file:
    sentences = file.readlines()

with open("settings.yml", "r") as file:
    settings = yaml.load(file, Loader=yaml.FullLoader)
    