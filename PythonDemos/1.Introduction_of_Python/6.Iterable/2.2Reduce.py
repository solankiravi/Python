from functools import reduce
import operator
number_list = range(-5,5)

#find the sum of list
print(reduce(lambda a,b:a+b, number_list))
print(reduce(operator.add,number_list))
#find max element
print(reduce(lambda a, b : a if a > b else b,number_list))
