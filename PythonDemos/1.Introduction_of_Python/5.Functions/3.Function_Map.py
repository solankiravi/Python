# Make an iterator that computes the function using arguments 
# from each of the iterables. Stops when the shortest iterable is exhausted
def square_it_func(a):
    return a * a

x = map(square_it_func, [1, 2, 3])
print(x) # prints '[1, 4, 9]'

def multiply_fun(a,b):
    return a * b

x = map(multiply_fun,[1,2,3],[4,5,6])
print(x) # prints '[4,10,18]'