#utilisation de la méthode reader() pour afficher les ééments ligne par ligne

'''
import csv

with open('couleurs_preferees.csv') as fichier_csv:
    reader = csv.reader(fichier_csv, delimiter=',')
    for ligne in reader:
        print(ligne)
        '''
# Méthode DictReader()  . Cette méthode sait que la première ligne est un en-tête, et sauvegarde les autres lignes en tant que dictionnaires.
import csv

with open('couleurs_preferees.csv') as fichier_csv:
        reader = csv.DictReader(fichier_csv, delimiter=',')
        for ligne in reader:
            print(ligne['nom'] + " travaille en tant que " + ligne['metier'] + " et sa couleur préférée est " + ligne['couleur_preferee'])