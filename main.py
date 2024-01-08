
import random
import variables


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

#Les fonctions
def my_function():
  print("Hello from a function")
my_function()

#Les arguments
def my_function (fname):
    print(fname + "Jess")

my_function("Email")
my_function("Tobias")
my_function("linus")

def my_function(*kids):
    print("The youngest child is " +kids[2])

my_function("Emilie" , "Thomas" , "Lary")

#return

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


#Recursivité

def tri_recursion(k):
    if(k>0):
        result = k+ tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(4)

#Python Lamda
x = lambda a : a + 10
print(x((5)))

x = lambda a, b, c : a + b +c
print(x(5,6,2))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

#les tableaux
cars = ["Ford", "Volvo", "BMW"]

x = cars[0]

print(x)
cars = ["Ford", "Volvo", "BMW"]

cars[0] = "Toyota"

print(cars)

#Classes
class Myclass:
    x=5
#Creation d'un objet et y inserer une valeur
p1 = Myclass()
print(p1.x)

#La fonction __init et les méthodes__()
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()









