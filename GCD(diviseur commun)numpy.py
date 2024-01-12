#Plus grand dénominateur commun
import numpy as np
num1 = 6
num2 = 9
x = np.gcd(num1, num2)
print(x)
#PGCD dans les tableaux 'reduce() comme dans le PPCM

arr = np.array([20, 8, 32, 36, 16])
x = np.gcd.reduce(arr)
print(x)