# *args and **kwargs are mostly used in function definitions. 
# *args and **kwargs allow you to pass a variable number of arguments to a function.

# *args is used to send a non-keyworded variable length argument list to the function

def return_sum(*argv):
    sum = 0
    for arg in argv:
        sum += arg
    return sum

print(return_sum(1,2,3))

# You should use **kwargs if you want to handle named arguments in a function
def return_value(**kwargs):
    # print(kwargs)
    for key,val in kwargs.items():
        print("{} = {}".format(key,val))
print(return_value(id=1,name='Ravi'))

#ordering of arguments
# def example2(arg_1, arg_2, *args, kw_1="name1", kw_2="name2", **kwargs):