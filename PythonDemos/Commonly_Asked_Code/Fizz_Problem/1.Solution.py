
"""
In FizzBuzz, you are given a list of integers. Your task is to do the following:

1. Replace all integers that are evenly divisible by 3 with "fizz"
2. Replace all integers divisible by 5 with "buzz"
3. Replace all integers divisible by both 3 and 5 with "fizzbuzz"
"""
numbers = [45, 22, 14, 65, 97, 72]

for index in range(len(numbers)):
    if(numbers[index] % 3 == 0):
        numbers[index] ='fizz'
    elif(numbers[index] % 5 == 0):
        numbers[index] ='buzz'
    elif(numbers[index] % 3 == 0 and numbers[index] % 5 == 0 ):
        numbers[index] ='fizzbuzz'
print(numbers)
    