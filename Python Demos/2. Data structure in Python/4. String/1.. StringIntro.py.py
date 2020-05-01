firstName = "Ravi"; lastName = "Solanki"
projectName = 'FCA Engineering IT'    # '' or "" is treated same 
#Concatenation
FullName = firstName +" " + lastName; print("Full Name ",FullName)
#Sub String
print("Name starts with letter ",firstName[0])
#range : Sub string
print(FullName[:2]) # starts from 0 to 1
print(FullName[0:2]) # starts from 0 to 1
print(FullName[2:]) # starts from 2 to last 
print(FullName[0:-2]) #starts from 0 to last - 2
print(FullName[:]) #starts from 0 to last
#long string 
longString = """ I'm Ravi working with "FCA Engineering IT" from last 1 year.""" 
print(longString)