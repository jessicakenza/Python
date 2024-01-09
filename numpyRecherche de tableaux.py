#pour rechercher un tableau, utiliser la méthode "where"
import numpy as np

#chercher les indices où les éléments de arr sont égaux à 4.
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)

#index ont les valeurs sont paires.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)
print(x)

#index ont les valeurs sont impaires.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 1)
print(x)

#recherche triée(searchsorted())
#Recherchez les index où la valeur 7 doit être insérée :
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x)

#Recherchez les index où la valeur 7 doit être insérée, en commençant par droite:
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side='right')
print(x)


