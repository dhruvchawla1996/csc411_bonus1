# Imports
import numpy as np

def generate_data():
	X = []
	y = []

	X.append([0, 0])
	y.append(0)

	label = 1

	for i in range(1, 200):
		X.extend([0, i], [i, 0], [0, -1*i], [-1*i, 0])
		y.extend([label, label, label, label])

		label = 1 - label

	return X, y