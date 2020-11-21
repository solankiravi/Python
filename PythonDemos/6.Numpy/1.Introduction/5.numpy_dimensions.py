import numpy as np
oneDArray = np.array([1,2,3])
twoDArray = np.array([[1,2,3],[1,2,3]])
thirdDArray = [[[1,2,3],[1,2,3]],[[1,2,3],[1,2,3]]]
fourDArray = [[[[1,2,3],[1,2,3]],[[1,2,3],[1,2,3]]],[[[1,2,3],[1,2,3]],[[1,2,3],[1,2,3]]]]
print(np.ndim(oneDArray))
print(np.ndim(twoDArray))
print(np.ndim(thirdDArray))
print(np.ndim(fourDArray))