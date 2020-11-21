from array import *
initializer = [20,30,40,50]
array1 = array('i',initializer)

#Insert
array1.insert(0,10) #insert at specific index (middle or first)
array1.append(60) #Insert at last
print(array1)

#update
array1[1]=15
print(array1)