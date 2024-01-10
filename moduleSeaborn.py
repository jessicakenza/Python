import matplotlib.pyplot as plt
import seaborn as sns

#Diagramme de disstribution
sns.displot([0, 1, 2, 3, 4, 5])
plt.show()
#plt.pause(10)

#Diagramme de repartition sans histogramme
sns.displot([0, 1, 2, 3, 4, 5],  hist=False)
plt.show()