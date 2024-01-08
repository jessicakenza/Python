mylist = ["apple", "banana", "cherry"]
print(len(mylist))

mylist = ["apple", "banana", "cherry"]
print(mylist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

print(list1)
print(list2)
print(list3)
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#Modifier un élément d'une liste
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#Modifier la valeur des élément dans une plage spécifique
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
#Ajouter les éléments à la liste
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#Supprésion des éléments(remove pour supprimer l'occurence et pop pour supprimer l'index)
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#Parcourir la liste
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
  thislist = ["apple", "banana", "cherry"]
  i = 0

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
