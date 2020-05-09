#function Declaration and definition
def SumOfTwoNumber(a,b):
	return a+b
#Calling a funtion
Sum = SumOfTwoNumber(5,8);
print(Sum)

#Anonymous Function
lamdaSum = lambda a,b = 9 : a + b
print(lamdaSum(7))