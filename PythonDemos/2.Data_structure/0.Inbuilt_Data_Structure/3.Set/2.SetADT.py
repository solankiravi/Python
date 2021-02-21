set1 = {"John","Ravi", "Ravi", "Anil",("WPF","MOngoDB","Python") }
set2 = {"John","Ravi", "Solanki", "Singh",'Snow' }
#Add Elements
set1.add("Vikash")
#Remove element
set1.pop() # removes a random value
set1.discard("Solanki") #remove if found, else do nothing
set1.remove("Ravi")
#update set1 : Add all ements of set2 to set1
set1.update(set2)
#Union of Two set
print(set1.union(set2))
#Intersection of Two Set
print(set1.intersection(set2))
#Difference of Two Set
print(set1.difference(set2))
print(set1.symmetric_difference(set2))
print(set1)