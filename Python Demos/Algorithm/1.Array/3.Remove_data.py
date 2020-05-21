from array import *
initializer = [20,30,40,50]
array1 = array('i',initializer)

#Delete
array1.remove(20)
#array1.remove(60) #throw exception if value is not present
del(array1[0]) #Remove element from index
print(array1)