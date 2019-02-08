import numpy as np

# Constructing a record array from CSV file
r = np.genfromtxt("jester-data-1.csv", delimiter=',', dtype=None, encoding="utf8")

# Printing array and its dimensions
#print(r)
#print(r.shape[0], r.shape[1])
