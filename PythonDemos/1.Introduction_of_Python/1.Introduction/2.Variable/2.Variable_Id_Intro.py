
intVariable = 10
floatVariable = 10.10
stringVariable="Ravi"
booleanValue = True

print(type(intVariable))
print(type(floatVariable))
print(type(stringVariable))
print(type(booleanValue))


x= 42
y = 24
w = 42
z = x
print(id(x))
print(id(w))
print(id(z))
print(id(y))
print(type(y))
y = "Hello"
print(id(y))
print(type(y))

from sys import getsizeof
print(getsizeof(x))
print(getsizeof(y))
print(getsizeof("Ravi"))
print(getsizeof(True))