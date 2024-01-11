#elle possède deux parametres df('dégré de liberté) et size
#Extrayez un échantillon pour la distribution du chi carré avec un degré de liberté 2 et une taille 2x3 :

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.chisquare(df=2, size=(2, 3))
print(x)

#visualisation
sns.distplot(random.chisquare(df=1, size=1000), hist=False)
plt.show()