import numpy as np

#division du tableau en 3 parties
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)

