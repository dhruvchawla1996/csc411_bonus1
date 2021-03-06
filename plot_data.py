# Imports
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
from scipy.ndimage import filters
import matplotlib.cbook as cbook
from pylab import *

from generate_data import *

plt.switch_backend('agg')

def plot_data():
    # Dataset and labels
    X, y = generate_data()

    x_0, y_0, x_1, y_1 = [], [], [], []

    for i in range(len(X)):
        if y[i] == 0:
            x_0.append(X[i][0])
            y_0.append(X[i][1])
        elif y[i] == 1:
            x_1.append(X[i][0])
            y_1.append(X[i][1])

    plt.scatter(x_0, y_0, c = "r", alpha = 0.5)
    plt.scatter(x_1, y_1, c = "b", alpha = 0.5)

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Data generated by generate_data()")
    plt.savefig("data.png")
