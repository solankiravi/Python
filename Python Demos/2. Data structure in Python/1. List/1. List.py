#Creating a list - Hetrogenous container having ordered structure
list1=[1,"Ravi","Vikash",4.58,True];list2 = [True,"Vikash","Ravi",4.58,1]
list3=[True,"Ravi","Vikash",4.58,1]
print(list1 == list2); print(list1 == list3) 
#Access List Items
list1[1] = "Solanki" #Index starts from 0.
print(list1[1]) 
#Slice List
print(list1[1:3]) # returns list item within range of 1 and 3
print(list1[:-2]) # start from 1st element to last-2th element 
print(list1[2-2 : 4]) #starts from 0th to 3th indexed elements
#Print alternate elements in a list
print(list1[0:: 2])  #returns elements with stride 2
#Reverse List
print(list1[::-1]) # Reverse list
#Concat List
print(list1 + list2)