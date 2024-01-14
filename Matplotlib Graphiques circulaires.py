#Ici, on utilise la fonction pie() et le parametre 'label' pour ajouter les étiquetttes,on peut également spécifier l'angle de départ en utilisant 'startangle'
import matplotlib.pyplot as plt
import numpy as np
#diagramme circulaire

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels, startangle = 90)
plt.show()

#séparation d'un coin des autres.( on utilise le parametre explode())
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode)
plt.show()

#ombres : ici on utilise shadow qui prend True
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
plt.show()
#Definissons des couleurs
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
mycolors = ["black", "c", "m", "#4CAF50"]

plt.pie(y, labels = mylabels, colors = mycolors)
plt.show()

#Ajout de la légende
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend()
plt.show()