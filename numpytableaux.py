import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

#création d'un tableau 0-D avec la valeur 42
arr = np.array(42)
print(arr)

#vérification du nombre de dimension d'un tableau
a = np.array(42)
b = np.array ([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
#création d'un tableau a 5 dimensions
arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)