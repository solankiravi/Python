import numpy as np
oneDArray =  np.array([1,2,3])
print(type(oneDArray))   #<class 'numpy.ndarray'>
print(oneDArray.dtype)   #int32
print(np.shape(oneDArray))  #(3,)
print(np.ndim(oneDArray)) # 1
print(np.size(oneDArray)) # 3
twoDArray =  np.array([[1,2,3],[5,6,7]])
print(np.shape(twoDArray))  #(2, 3)
multiDArray = np.array([[[0, 1],[2, 3]],[[4, 5],[6, 7]]])
print(np.shape(multiDArray))    #(3, 3)
print(multiDArray[0,1]) #[2 3]