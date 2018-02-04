# Imports
import numpy as np

def generate_data():
    """Generate random data resembling a chess board

    Returns
    X: list(list(x, y)) : coordinates of chess board
    y: list(either 0 or 1)
    """
    X = []
    y = []

    label = 1

    np.random.seed(5)

    for k in range(100):
        x_coord = 1 - 0.5 + np.random.random_sample()
        y_coord = 1 - 0.5 + np.random.random_sample()

        X += [[x_coord, y_coord]]
        y += [label]

    label = 1 - label

    for i in range(3):
        for j in range(3):

            if i == 1 and j == 1: continue

            for k in range(100):
                x_coord = i - 0.5 + np.random.random_sample()
                y_coord = j - 0.5 + np.random.random_sample()

                X += [[x_coord, y_coord]]
                y += [label]

            #label = 1 - label

        #label = 1 - label

    return X, y
