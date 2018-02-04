# Imports
import numpy as np

def generate_data():
	X = []
	y = []

	X.append([0, 0])
	y.append(0)

	label = 1

	for i in range(1, 3):

		for j in range(8):
			X += [[i * np.cos(j/8 * 2*np.pi), i * np.sin(j/8 * 2*np.pi)]]
			y += [label]

		label = 1 - label

	return X, y
