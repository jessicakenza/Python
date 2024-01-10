#Deux paramètre 'scale et 'size'
#un échantillon pour une distribution exponentielle avec une échelle 2.0 et une taille 2x3 :

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.exponential(scale=2, size=(2, 3))
print(x)

#Visualisation de la distribution exponentielle
sns.distplot(random.exponential(size=1000), hist=False)

plt.show()