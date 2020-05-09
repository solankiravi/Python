#Map() is a built-in Python function used to apply a function 
# to a sequence of elements like a list or dictionary.

def square_it_func(a):
    return a * a

x = map(square_it_func, [1, 2, 3])
print(x) # prints '[1, 4, 9]'

def multiply_fun(a,b):
    return a * b

x = map(multiply_fun,[1,2,3],[4,5,6])
print(x) # prints '[4,10,18]'