#ici, on utilise les fonctions xlabel() et ylabel()
import numpy as np
import matplotlib.pyplot as plt

#titre sur l'abscisse et l'ordonnée
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y)
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.show()

#création d'un titre pour intrigue
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y)
plt.title("sports Watch Data")
plt.xlabel("Averae pulse")
plt.ylabel("Calorie Burnage")
plt.show()

#definition des propriétés de police pour le titre et les étiquettes

#ici on utilise les parametres fontdict dans xlabel(),ylabel() et title() pour definir les propriétés de police pour le titre et étiquettes.
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}
plt.title("Sports Watch Data", fontdict = font1)
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)
plt.plot(x, y)
plt.show()

#positionner le titre: ici on utilise le paramètre 'loc' dans 'title() pour positionner le titre
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.title("Sports Watch Data", loc = 'left')
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.plot(x, y)
plt.show()
