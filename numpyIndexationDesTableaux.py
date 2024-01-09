import numpy as np
#recupération du premier élément du tableau
array = np.array([1, 2, 3, 4])
print(array[0])

#accès a l'element sur la prémiere ligne , deuxieme colonne
arr = np.array([[1, 2, 3, 4, 5,],[6, 7, 8, 9, 10]])
print('2nd élément on 1st row: ', arr[0, 1])

#Accès à l'élément de la 2ème ligne, 5ème colonne :
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('5th element on 2nd row: ', arr[1, 4])

#Tableaux 3D(Accès au troisième élément du deuxième tableau du premier tableau :)
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])
