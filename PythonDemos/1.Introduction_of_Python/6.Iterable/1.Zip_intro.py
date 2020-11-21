
#zip takes any number of iterables and returns a zip object that is an iterator of tuples.
a = [1,2,3]
b = ['a','b','c']

for i in zip(a,b):
    print(i)


print("=================")
print(list(zip(a,b)))