"""CSC411: Project 1 (bonus)
   Dhruv Chawla"""

# Imports
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

from generate_data import *

n_neighbors = 3

# Dataset and labels
X = [[0, 0], [1, 1], [5, 4]]
y = [0, 1, 0]

neigh = KNeighborsClassifier(n_neighbors)
neigh.fit(X, y)

print(neigh.predict(X))
