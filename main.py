
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