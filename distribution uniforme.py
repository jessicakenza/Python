#Utilisée pour décrire la probabilité selon laquelle chaque évènement a des chances égales de se reproduire
#comporte 3 paramètres 'a' , 'b' , size'

#Créez un échantillon de distribution uniforme 2 x 3 :

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
x = random.uniform(size=(2, 3))
print(x)

#Visualisation de la distribution uniforme
sns.distplot(random.uniform(size=1000), hist=False)
plt.show()