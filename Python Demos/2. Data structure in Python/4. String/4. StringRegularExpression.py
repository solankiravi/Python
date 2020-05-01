import re # Import regular expressin module
text = "My name is Ravi Solanki. Ravi is working in FCA Project"
pattern = "Solanki*"
#Pattern Matching : re.match() method finds match if it occurs at start of the string
 #if found return matched element else return none
print(re.match(pattern,text))
#Searching : The re.search() method is similar to re.match() but it doesn’t limit us to 
# find matches at the beginning of the string only.
print(re.search(pattern,text))
#Findall : re.findall() method returns list of all matches found
x = re.findall("Ravi", text)
print(len(x))
#Replace each searched value with new value
newStr=re.sub("Solanki","Kumar",text)
print(newStr)
#Split 
print(re.split("\.",text))