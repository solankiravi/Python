#str and int is not iterator they are iterable.
#iterable has iter method whereas iterator has next method
name = "Ravi"
age=25
try:
    print(iter(name))
    print(next(name)) #TypeError: 'str' object is not an iterator
except:
    print(iter(age)) #TypeError: 'int' object is not iterable
    print(next(age)) #TypeError: 'int' object is not an iterator

'''
conclusion : 
we can not iterate numbers like string and to iterate string we need to use iter method
'''