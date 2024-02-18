import numpy as np


def get_factors(n):
	factors = []
	for i in range(1, n):
		if n % i == 0:
			factors.append(i)
	return factors


def normalise_to_range(x, min_orig, max_orig, min_new, max_new):
	if isinstance(x, list): x = np.array(x)
	return np.round((x - min_orig) * (max_new - min_new) / (max_orig - min_orig) + min_new, 3)