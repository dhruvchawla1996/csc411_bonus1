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

    for i in range(3):
        for j in range(8):
            for k in range(60):
                x_coord = (i - 0.5 + np.random.random_sample()) * np.cos(j/8 * 2*np.pi)
                y_coord = (i - 0.5 + np.random.random_sample()) * np.sin(j/8 * 2*np.pi)

                X += [[x_coord, y_coord]]
                y += [label]

        label = 1 - label

    return X, y
