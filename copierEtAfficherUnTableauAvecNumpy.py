import numpy as np

#copie et modification du tableau d'origine
arr = np.array([1, 2, 3, 4, 5])
x= arr.copy()
arr[0] = 42
print(arr)
print(x)

#création d'une vue, modification du tableau d'origine et affichage des deux tableaux
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42
print(arr)
print(x)

#création d'une vue, modification de la vue et affichage des deux tableaux
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31
print(arr)
print(x)
#vérifier si le tableau possède des donnée(impréssion de l'attribut de base)
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()
print(x.base)
print(y.base)
