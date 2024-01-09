#ici on utilise la methode choice() et le module random

#Générez un tableau 1D contenant 100 valeurs, où chaque valeur doit être 3, 5, 7 ou 9.
""""
La probabilité que la valeur soit 3 est fixée à 0,1

La probabilité que la valeur soit 5 est fixée à 0,3

La probabilité que la valeur soit 7 est fixée à 0,6

La probabilité que la valeur soit 9 est fixée à 0
"""

from numpy import random
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
print(x)