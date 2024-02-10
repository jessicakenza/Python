#Utiliser la fonction open() pour lire et ecrire un fichier
#write (w) pour ecraser un fichier
#réation  d'un fichier appelé « hello.txt » et remplacer par « Hello, world! »,
with open("file.txt") as fichier:
    for ligne in fichier:
        # faire quelque chose avec une ligne
        print(ligne)