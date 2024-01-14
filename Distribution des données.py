#un tableau contenant 250 flottants aléatoires entre 0 et 5 :

import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 250)

print(x)

#Histogramme pour visualiser l'ensemble des données
x = numpy.random.uniform(0.0, 5.0, 250)

plt.hist(x, 5)
plt.show()