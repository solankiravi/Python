# filter creates a list of elements for which a function returns true.

number_list = range(-5,5)
less_than_zero = list(filter(lambda x: x < 0,number_list))
print(less_than_zero)

def is_less_than_zero(x):
    return x < 0

less_than_zero = list(filter(is_less_than_zero,number_list))
print(less_than_zero)