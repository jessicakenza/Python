#les méthodes utilisées ici sont shuffle() et permutation()

#Mélange aléatoire des élément du tableau
from numpy import random
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)
print(arr)

#génération des permutations de tableaux
arr = np.array([1, 2, 3, 4, 5])
print(random.permutation(arr))