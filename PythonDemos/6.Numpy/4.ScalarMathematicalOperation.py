import numpy as np 
a = np.random.rand(4) * 10
print(a)
print("========= Increase By 1 ===============")
print(a + 1)
print("==========Decrease By 1 ==============")
print(a - 1)
print("===========Multiply By 2=============")
print( a * 2)
print("========Divide By 2================")
print(a / 2)
print("========Square By 2================")
print(a ** 2)
print("========Matrix Operations================")
b = np.random.rand(12).reshape(4,3)
print(b)
print("========Transpose of Matrix================")
print(np.transpose(b))
print("========Sum of Matrix================")

print(np.sum(b))
print("========Sum of Matrix on axis = 1================")
print(np.sum(b, axis = 1))

