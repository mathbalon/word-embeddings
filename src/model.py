import time
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

from logger import logger

def create_neural_network_model(X:np.ndarray, Y:np.ndarray, settings:dict, logger_file_name:str):
    st = time.time()

    input_layer = tf.keras.Input(shape=(X.shape[1],))
    hidden_layer = tf.keras.layers.Dense(units=settings["embed_size"], activation='linear')(input_layer)
    output_layer = tf.keras.layers.Dense(units=Y.shape[1], activation='softmax')(hidden_layer)

    model = tf.keras.Model(inputs=input_layer, outputs=output_layer)
    model.compile(loss = 'categorical_crossentropy', optimizer = 'adam')

    model.fit(
        x=X, 
        y=Y, 
        batch_size=settings["batch_size"],
        epochs=settings["epochs"]
        )

    et = time.time()
    
    logger(logger_file_name, "create_neural_network_model", et-st)

    return model.get_weights()[0]

def plot_results(weights, unique_word_dict:dict, logger_file_name:str):
    embedding_dict = {}

    for word in unique_word_dict.keys(): 
        embedding_dict.update({
            word: weights[unique_word_dict.get(word)]
            })
    
    plt.figure(figsize=(10, 10))

    for word in list(unique_word_dict.keys()):
        coord = embedding_dict.get(word)
        plt.scatter(coord[0], coord[1])
        plt.annotate(word, (coord[0], coord[1]))

    plt.savefig("logs/" + logger_file_name + ".png")