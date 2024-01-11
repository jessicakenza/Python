#deux parametre: (a parametre de distribution et size : forme envoyée

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.zipf(a=2, size=(2, 3))
print(x)

#visualisation:
x = random.zipf(a=2, size=1000)
sns.distplot(x[x<10], kde=False)

plt.show()