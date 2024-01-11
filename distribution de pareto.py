#Deux parametres 'a: parametre de forme et 'size'/forme du tableau renvoyé

#Dessinez un échantillon pour la distribution de Pareto avec une forme de 2 et une taille de 2x3 :
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
x = random.pareto(a=2, size=(2, 3))
print(x)

#visualiser
sns.displot(random.pareto(a=1, size=1000), kde=False)

plt.show()