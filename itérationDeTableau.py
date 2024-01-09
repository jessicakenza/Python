import numpy as np

#parcours des tableaux
arr = np.array([1, 2, 3])
for x in arr:
  print(x)

#itération sur  les éléments du tableau 2D
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  print(x)

#parcourir jusqu'aux scalaire
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
  for y in x:
    for z in y:
      print(z)


#itération de tableaux à l'aide de nditer()
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
  print(x)

  #tableau itéré avec différents types de données
  arr = np.array([1, 2, 3])
  for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)

 #iteré en utilisant ndenumerate
arr = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr):
  print(idx, x)