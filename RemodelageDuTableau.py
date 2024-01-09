import numpy as np

#Convertissez le tableau 1D suivant avec 12 éléments en un tableau 2D.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)

#dimension inconnue (Convertir un tableau 1D avec 8 éléments en tableau 3D avec 2x2 éléments :)
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr)

#applatir les éléments
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)


