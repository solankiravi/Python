#Benefits of ndarray over list - Less Memory , Fast, Convenient
import numpy as np
 
import time
import sys
starttimeList= time.time()
l1= range(10000)
l2=range(10000)
result = [(x,y) for x,y in zip(l1,l2)]
print("List Size "+ str(sys.getsizeof(result)))
print("List time "+ str(time.time() - starttimeList)) 
starttimenp = time.time()
A1= np.arange(10000)
A2= np.arange(10000)
result = A1 + A2
print("Numpy Size : "+str(sys.getsizeof(result)))
print("Numpy execution : "+str(time.time() - starttimenp))