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

    for i in range(20):
        for j in range(20):

            x_coord = i - 0.5 + np.random.random_sample()
            y_coord = j - 0.5 + np.random.random_sample()

            X += [[x_coord, y_coord]]
            y += [label]

            label = 1 - label

        label = 1 - label

    return X, y
