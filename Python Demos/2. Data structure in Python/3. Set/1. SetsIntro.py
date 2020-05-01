#Create Empty Set
emptySet = {} 
print(type(emptySet))
emptySetSuccessful = set({})
print(type(emptySetSuccessful))
#Create Set
set = {"Ravi", "Ravi", ("WPF","MOngoDB","Python") }
#Check Type
print(type(set))
#Number of elements in set
print(len(set))
#print set
print(set)
#Elements should be of only immutable types - List and dictionary are not allowed.
WrongSet = {"Ravi", "Ravi", ["WPF","MOngoDB","Python"],{"Name" : "Solanki"} }