filepath = r'C:\Users\Ravi\Desktop\Python\CheckVersion.py'
#Step 1
'''
#Open file
f = open(filepath,'r')
print(f.name)
#Close file
f.close()
'''
#step 2
with open(filepath,'r') as f:
    fileContent = f.read()
    print(fileContent)