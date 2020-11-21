#Given a list of values inputs and a positive integer n, 
# write a function that splits inputs into groups of length n. 
# For simplicity, assume that the length of the input list is divisible by n. 
#For example, if inputs = [1, 2, 3, 4, 5, 6] and n = 2, your function should return [(1, 2), (3, 4), (5, 6)].

inputs = [1, 2, 3, 4, 5, 6]

def naive_grouper(inputs, n):
    num_groups = len(inputs)     
    return [tuple(inputs[i*n:(i+1)*n]) for i in range(num_groups)]
