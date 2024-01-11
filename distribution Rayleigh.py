#possede deux paramètre scale et size

#échantillon pour la distribution de Rayleigh avec une échelle de 2 et une taille 2x3 :
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
x = random.rayleigh(scale=2, size=(2, 3))
print(x)

#Visualisation
sns.distplot(random.rayleigh(size=1000), hist=False)

plt.show()