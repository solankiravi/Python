from functools import reduce
import operator
number_list = range(-5,5)

#find the sum of list
print(reduce(lambda a,b:a+b, number_list))
print(reduce(operator.add,number_list))
#find max element
print(reduce(lambda a, b : a if a > b else b,number_list))
# filter creates a list of elements for which a function returns true.
number_list = range(-5,5)
less_than_zero = list(filter(lambda x: x < 0,number_list))
#zip takes any number of iterables and returns a zip object that is an iterator of tuples.
a = [1,2,3]
b = ['a','b','c']

for i in zip(a,b):
    print(i)