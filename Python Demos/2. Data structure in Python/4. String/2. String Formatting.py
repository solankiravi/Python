# Working with " and '
#print('what's your name')
print("what's your name"); print('what'+"'"+'s your name'); print('what\'s your name'); print('what\"s your name')
#Reverse String
hello = "Hello"; world="World"; print(world[::-1])
#Argument passing
print(f"{hello} {world} program is completed"); print("{0} {1} program is completed".format(hello,world))
print("%s %s program is completed" %(hello,world))
#Escape Sequence
print("Tab involves \t 8 spaces"); print("Hi \n  New line starts from here ")    
print('\\t') # to Escape a ' or " or \, use \