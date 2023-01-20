# word-embeddings
A simple test of study and implementation of the Word2Vec algorithm and neural network

This experiment is all based in the article [Creating Word Embeddings: Coding the Word2Vec Algorithm in Python using Deep Learning](https://towardsdatascience.com/creating-word-embeddings-coding-the-word2vec-algorithm-in-python-using-deep-learning-b337d0ba17a8) writen by _Eligijus Bujokas_.

## Structure
This project is organized to separate the entities. Below are the informtion about the directories and files:
  - `settings.yml` : This file contains the experiment variables that affect directly on the results, such as the context window and the model parameters.
  - `data/` : This directory contains the files that will be used on the experiment.
  - `logs/` : For every experiment execution the code will create a file with the date and timestamp. Inside will be generated the log file that contains information about the machine and time execution for every function. Also the plot image generated.
  - `src/` : Contains all the code. The functions are implemented in separeted files and called in `main.py`.
  - `utils/` : This directory contains files that help in the code. For example, the file within all stopwords necessary.

## How to run?
To run the experiment just run this command below:

```
make run
```

By default, the data file is seted is **the_future_king.txt**. If you want to change just run the make command changing de FILE variable like this:

```
FILE="new_data_file.txt" make run
```
