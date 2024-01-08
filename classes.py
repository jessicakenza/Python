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
