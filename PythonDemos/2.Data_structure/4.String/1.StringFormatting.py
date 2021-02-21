
firstname="Ravi";lastname='Kumar'

print("First Digit ", firstname[0])

fullname = firstname.__add__(lastname)
#Argument passing
print("My name is  %s %s" %(firstname,lastname))
print("My name is  {0} {1}".format(firstname,lastname))
print(f"{firstname} {lastname}"); 

#Escape Sequence
print("Tab involves \t 8 spaces"); print("Hi \n  New line starts from here ")    
#long string 
about = """ I'm Ravi.
A software engineer, Teacher and a problem solver.
""" 
print(about)

# question='what's your name'

# Working with " and '
#print('what's your name')
print("what's your name")
print('what'+"'"+'s your name')
print('what\'s your name')

print('\\t') # to Escape a ' or " or \, use \

