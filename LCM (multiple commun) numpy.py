#recherche du LCM(plus petit commun multiple)
import numpy as np
#il es question d'afficher le ppcm
num1 = 4
num2 = 6
x = np.lcm(num1, num2)
print(x)
#recherche de LCM dans des tableaux
#utiliser la fonction reduce()
arr = np.array([3, 6, 9])
x = np.lcm.reduce(arr)
print(x)
#chercher le ppcm de toutes les valeurs d'un tableau(entre 1 et 10)
arr = np.arange(1, 11)
x=np.lcm.reduce(arr)
print(x)