# Imports
import numpy as np

def generate_data():
	X = []
	y = []

	X.append([0, 0])
	y.append(0)

	label = 1

	for i in range(1, 3):
		X += [[0, i]] + [[i, 0]] + [[0, -1*i]] + [[-1*i, 0]]
		y += 4*[label]

		label = 1 - label

	return X, y
