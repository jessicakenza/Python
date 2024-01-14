#ici il faut trouver la vitesse moyenne , on utilise mean()
import numpy
from scipy import stats


speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed)

print(x)

#pour trouver la médiane on utilise la méthode median()
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.median(speed)

print(x)

#la valeur 'mode' (c'est celle la qui apparait plusieurs fois)
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = stats.mode(speed)

print(x)