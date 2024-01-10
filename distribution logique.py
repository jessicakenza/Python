# utilisée pour décrire la croissance.
#comporte 3 paramètre 'loc' , 'scale, 'size'

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
x = random.logistic(loc=1, scale=2, size=(2, 3))
print(x)

#visualisation
sns.distplot(random.logistic(size=1000), hist=False)
plt.show()

#Différence entre la logistique et la distribution normale
sns.distplot(random.normal(scale=2, size=1000), hist=False, label='normal')
sns.distplot(random.logistic(size=1000), hist=False, label='logistic')
plt.show()