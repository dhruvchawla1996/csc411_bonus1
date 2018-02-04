"""CSC411: Project 1 (bonus)
   Dhruv Chawla"""

# Imports
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

from generate_data import *

# Dataset and labels
X, y = generate_data()

# Run kNN with increasing K
for n in range(1, len(y)):
    neigh = KNeighborsClassifier(n)
    neigh.fit(X, y)

    prediction = neigh.predict(X)

    total = len(prediction)
    correct = sum(1 - np.absolute(y - prediction))

    print(100* correct/float(total))
