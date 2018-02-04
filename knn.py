"""CSC411: Project 1 (bonus)
   Dhruv Chawla"""

# Imports
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
from scipy.ndimage import filters
import matplotlib.cbook as cbook
from pylab import *

from generate_data import *

plt.switch_backend('agg')

# Dataset and labels
X, y = generate_data()

K = []
performance = []

# Run kNN with increasing K
for n in range(1, len(y)):
    neigh = KNeighborsClassifier(n)
    neigh.fit(X, y)

    prediction = neigh.predict(X)

    total = len(prediction)
    correct = sum(1 - np.absolute(y - prediction))

    K += [n]
    performance += [100 * correct/float(total)]

# Plot performance and save image
plt.plot(K, performance, color="b", linewidth=2)

plt.title("Performance on training set with K")
plt.xlabel("K")
plt.ylabel("Performance on training set (%)")
plt.savefig("performance.png")
