import numpy as np 
twoDArray = np.array([[1,2,3],[1,2,3]])
print(twoDArray)
print("=============Slicing==================")
print(twoDArray[1: ,::2])
print("=============Condition Check==================")
cond = (twoDArray % 2 != 0)
print(twoDArray[cond])
