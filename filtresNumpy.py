#Filtrer les tableaux à l'aide de la liste de l'index booléens.
import numpy as np

arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)

#Création du tableau de filtres
arr = np.array([41, 42, 43, 44])

filter_arr = []
for element in arr:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

#Tableau de filtres qui renverra uniquement les éléments pairs de l'original tableau
arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = []
for element in arr:
  if element % 2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)


