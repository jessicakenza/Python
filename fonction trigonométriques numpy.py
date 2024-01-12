#ici on utilise les propriété 'cos(), 'sin() 'tan()'
import numpy as np
x = np.sin(np.pi/2)
print(x)

#valeurs sinusoïdales pour toutes les valeurs dans arr :
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.sin(arr)
print(x)

#Convertir des degrés en radians(toutes les valeurs du tableau suivant arr en radians :)
arr = np.array([90, 180, 270, 360])
x = np.deg2rad(arr)
print(x)

#valeurs du tableau suivant arr en degrés :
arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
x = np.rad2deg(arr)
print(x)

#Angles de chaque valeur dans les tableaux
arr = np.array([1, -1, 0.1])
x = np.arcsin(arr)
print(x)

#hypoténues pour 4 bases et 3 perpendiculaires :
base = 3
perp = 4
x = np.hypot(base, perp)
print(x)
