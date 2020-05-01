filepath = r'C:\Users\Ravi\Desktop\someFile.txt'

#Open file in read mode
with open(filepath,'r') as f:
    sizeOfContent = 100
    # print(f.readable())  #Check whether there is read permission or not - Returns boolean
    #print(f.readline()) #First Line
    #print(f.read(sizeOfContent), end="****") #Read Specific number of characters
    #print(f.readlines()) #Read all lines

    