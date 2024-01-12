#les parametres utilisés ici sont sinh() , cosh() et tanh()

#trouver la valeur sinh de Pi/2
import numpy as np
x = np.sinh(np.pi/2)
print(x)

#les valeurs cosh pour toutes les valeurs dans arr :
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.cosh(arr)
print((x))

#Triuver les angles
x = np.arcsinh(1.0)
print(x)

#angles de chaque valeur dans le tableau
arr = np.array([0.1, 0.2, 0.5])
x = np.arctanh(arr)
print(x)