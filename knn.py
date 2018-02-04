"""CSC411: Project 1 (bonus)
   Dhruv Chawla"""

# Imports
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

from generate_data import *

n_neighbors = [1, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750]

# Dataset and labels
X, y = generate_data()

for n in n_neighbors:
    neigh = KNeighborsClassifier(n)
    neigh.fit(X, y)

    prediction = neigh.predict(X)

    total = len(prediction)
    correct = sum(np.absolute(y - prediction))

    print(correct/(float)total)
