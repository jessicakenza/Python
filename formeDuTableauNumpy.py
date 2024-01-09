import numpy as np
#obtension des dimensions du tableau
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)

#création d'un tableau à 5 dimensions en utilisant ndmin et verification de la dimension la dernière valeur
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('shape of array :', arr.shape)
