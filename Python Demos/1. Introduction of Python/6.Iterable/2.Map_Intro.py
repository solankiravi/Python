# map applies a single-parameter function to each element of an iterable one element at a time:

a = ['abc','defxy','ghijklmn']

#map takes first argument as function and second argument is iterable on which 
#it runs function one by one
print(list(map(len,a)))

def change_upper_case(s):
    return str(s).upper()

print(list(map(change_upper_case,a)))

#you can combine map and zip
n1=[1,2,3]
n2=[4,5,6]

print(list(map(sum,zip(n1,n2))))