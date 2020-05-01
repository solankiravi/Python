#Creating dictionary - use { }
dict = {"Name": "Ravi",
        "Project" : "FCA Engineering IT",
        "Experience (In Years)" : 1.5,
        "Mentors" : {"PTHIL" : "Vijay Sanap", "PowerCal" : "BharatKumar Mori", "DN" : "Anirban Mitra"},
        "Skill Set" : ["WPF","MongoDB","Python"]
        }

#Get specific key value
print(dict["Name"])
#Add elements in a dictionary
if("Greade" not in dict):
    dict["Grade"] = "B"
#Update value of key
if("Name" in dict):
    dict["Name"] = "Ravi Solanki"
print(dict)