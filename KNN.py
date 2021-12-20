"""
This is a comment
written in
more than just one line
"""
from typing import List

print("Hello, World!")

x = str(5)
y = bool(5<2)
z = float(44)
print(x,y,z)

a = 10
b = 44.009
c = "true"
d = 555

print(type(a))
print(type(b))
print(type(c))


myVariableName = "MSPK"
print(myVariableName)

fruits = ["apple", "banana", "cherry"]
g, h, i = fruits

print(g)
print(h)
print(i)


e = "swetha"
f = "mspk"

review = e + f

print(review)

x = "Nice"
def myfunc():
    global x
    x = "not bad"


myfunc()

print("Who is " + x + " ?")
