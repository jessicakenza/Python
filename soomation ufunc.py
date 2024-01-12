import numpy as np
#Sommation sur tous les éléments
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr = np.sum([arr1, arr2])
print(newarr)

#sommation sur n éléments
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr = np.sum([arr1, arr2], axis=1)
print(newarr)

#somme cumulée (fonction cumsum)
arr = np.array([1, 2, 3])
newarr = np.cumsum(arr)
print(newarr)