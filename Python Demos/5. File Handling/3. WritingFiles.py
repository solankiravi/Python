filepath = r'C:\Users\Ravi\Desktop\someFile.txt'

#Write to a file
with open(filepath,'w') as f:
    fileContent = "Hello World."
    f.write(fileContent)
#Append data
with open(filepath,'a') as f:
    fileContent = "Python is really easy. isn't it?"
    f.write(fileContent)


with open(filepath,'r') as f:
    print(f.readlines())