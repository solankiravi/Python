#anything which can be traversed is iterator
#There are 3 concepts : Iteration , Interable and iterator

#iterable is any object which can provide us with an iterator.
#Iterator is any object which has next method
#Iteration is the process of accessing element one by one

#Generator are iterators but they are interated only once. It requires less resources
# It is mainly implemented as functions but they yield value not return.

def fibonacci(n):
    a = b = 1
    for i in range(n):
        yield a
        a , b = b , a + b

for x in fibonacci(5):
    print(x)

def get_first_three_number():
    for i in range(3):
        yield i
gen=get_first_three_number()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen)) # you will get StopIteration error here, becuase there are no elements left to iterate