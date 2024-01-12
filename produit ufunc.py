#ici on utilise la fonction prod()
import numpy as np
#Produit des éléments d'un tableau
arr = np.array([1, 2, 3, 4])
x = np.prod(arr)
print(x)

#Produit des éléments de deux tableaux
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
x = np.prod([arr1, arr2])
print(x)

#produit cumulatif
arr = np.array([5, 6, 7, 8])
newarr = np.cumprod(arr)
print(newarr)