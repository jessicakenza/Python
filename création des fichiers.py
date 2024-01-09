#fonction pour écrire
f = open("demofile2.txt" , "a")
f.write("Now the file has more content!")
f.close()
#lecture du fichier après modification
f = open("demofile2.txt" , "r")
print(f.read())
#écrasage du contenu
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
f = open("demofile3.txt", "r")
print(f.read())

#création d'un nouveau fichier
f = open("myfile.txt", "x")