#Creating dictionary - use { }
dict = {"Name": "Ravi", "Project" : "FCA Engineering IT", "Experience (In Years)" : 1.5,"Mentors" : 
       {"PTHIL" : "Vijay Sanap", "PowerCal" : "BharatKumar Mori", "DN" : "Anirban Mitra"},
        "Skill Set" : ["WPF","MongoDB","Python"]}
#Remove last Key 
print(dict.popitem())
#Remove specific Key 
print(dict.pop("Name"))
#Iteration of elements dictionary
count = 0
for i in dict:
    print(i , dict[i])
    count += 1
print(count)
#Clear Dictionary
print(dict.clear())
#delete Dictionary
del(dict)