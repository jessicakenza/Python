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