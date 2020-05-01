tuple1=(100,92,189,"Ravi","Solanki",True,0.5)
#Return an element from the tuple at any given position.
print(tuple1[2])
#Multipy elements with n times
print(tuple1 * 2)
#Search for an element in tuple
print(292 in tuple1)
#return number of element in tuple
print(len(tuple1))
tuple2 = (4,6)
#Combine elements of two tuples
print(tuple1 + tuple2)
#Convert tuple into list
list1 = list(tuple1)
list1.append("Hello World")
print(list1)
print(tuple1)