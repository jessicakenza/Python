#Ici on va utiliser ma fonction plot() 'elle permet de tracer une ligne d'un point à un autre'
#Tracer une ligne dans un diagramme de la position (1, 3) à la position (8, 10) :
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 18])
plt.plot(xpoints, ypoints)
plt.show()

#Traçage sans ligne (Dessiner deux points dans le diagramme, un en position (1, 3) et un en position (8, 10)
xpoints = np.array([1, 3])
ypoints = np.array([3, 10])
plt.plot(xpoints , ypoints, 'o:r')
plt.show()

#points multiples
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])
plt.plot(xpoints, ypoints)
plt.show()

#point x par défaut
ypoints