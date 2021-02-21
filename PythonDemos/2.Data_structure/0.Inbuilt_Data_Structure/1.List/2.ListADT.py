list1=[1,"Ravi","Vikash",4.58,True]
#__getitem__(index) : returns element of specified index.
print(list1.__getitem__(0))
# Insert Elements
list1.append("FCA") #Insertion at last index
list1.insert(2,"Solanki") #Insertion at specified index 
#Remove Elements
list1.remove("Ravi") #remove by Value
del(list1[1]) #remove at index
list1.pop(list1[0]) #removes at index and return 
#Replace Elements Value
list1[0] = 2
#Length of List
print(list1.__len__()); print(len(list1))
#Print List
print(list1)