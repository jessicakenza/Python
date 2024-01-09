#Fonction pour lire un fichier
f = open("demofile.txt" , "r")
print(f.read())

#Entrer les caracteres du fichier
f = open("demofile.txt" , "r")
print(f.read(5))

#Lire les lignes
f = open("demofile.txt" , "r")
print(f.readline())

#Intégration du fichier ligne par ligne
f = open("demofile.txt" , "r")
for x in f:
    print(x)

#Fermeture du fichier
f = open("demofile.txt" , "r")
print(f.readline())
f.close()
