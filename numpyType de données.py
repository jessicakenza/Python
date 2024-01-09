import numpy as np
#vérification du type de données d'un tableau
arr = np.array([1, 2, 3, 4])
print(arr.dtype)

#obtention du type de données d'un tableau contenant les chaines
arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)

#création des tableaux avec type de données definis
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)

#Créez un tableau avec un type de données entier de 4 octets :
arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)

#convertion des types de données sur les tableaux existants (Changez le type de données de float à integer en utilisant 'i' comme valeur de paramètre :)
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)