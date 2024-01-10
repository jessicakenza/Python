#Ici on va utiliser les paramètres 'loc','scale' et 'size'

#distribution normale aléatoire de taille 2x3 :

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.normal(size=(2, 3))
print(x)

#distribution normale aléatoire de taille 2x3 avec une moyenne à 1 et un écart type de 2 :
from numpy import random
x = random.normal(loc=1, scale=2, size=(2, 3))
print(x)

#Visualisation de la distribution normale
sns.displot(random.normal(size=1000), hist=False)

plt.show()