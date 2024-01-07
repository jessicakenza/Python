
import random
print(random.randrange(1, 10))
def print_hi(name):

    print(f'Hi, {name}')

if __name__ == '__main__':
    print_hi('PyCharm')

    if 5 > 2:
        print("Five is greater than two!")

    x = 13j
    y = 18
    z = 5.5
    a = complex(x)
    b = float(y)
    c = int(z)

    print(a)
    print(b)
    print(c)

    print(type(a))
    print(type(b))
    print(type(c))

    a = "Hello Jessy"
    print(a)

    a = "World"
    print(a[3])

for x in "banana":
    print(x)

a = "Hey Dear"
print(len(a))

txt = "The best things in life are free!!"
print("free" in txt)

txt = "Don't be different, be the difference"
if "free" in txt:
    print("Yess, 'free' is present.")
else:
    print("No 'free here'")

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#Opérateurs
print(10+5)
print(2**3)
print(5%2)
print(27//2)
print((6 + 3) - (6 + 3))

#Listes
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

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
def myfunc(n):
  return abs(n - 50)
#les ensembles
thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)


thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
#Copie de la liste
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#Tuples
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Dictionnaires
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
#if
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

  a = 200
  b = 33
  if b > a:
      print("b is greater than a")
  elif a == b:
      print("a and b are equal")
  else:
      print("a is greater than b")
