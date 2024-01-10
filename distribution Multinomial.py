#trois paramètres 'n' , 'pvals' , 'size'

#échantillon pour le lancer de dés :

from numpy import random
x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6])
print(x)