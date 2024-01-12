import matplotlib.pyplot as plt
import numpy as np

#Tracez une ligne dans un diagramme de la position (0,0) à la position (6,250) :
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()