#Il estime combien de fois un événement peut se produire dans un temps spécifié. par exemple. Si quelqu’un mange deux fois par jour, quelle est la probabilité qu’il mange trois fois ?
#il poddède deux parametres 'lam' et 'size'

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
x = random.poisson(lam=2, size=10)
print(x)

#visualisation de la distribution poisson
sns.displot(random.poisson(lam=2, size=1000), kde=False)
plt.show()

#différence entre la distribution poisson et la distribution normale
#La distribution normale est continue alors que poisson est discret.
sns.distplot(random.normal(loc=50, scale=7, size=1000), hist=False, label='normal')
sns.distplot(random.poisson(lam=50, size=1000), hist=False, label='poisson')
plt.show()
