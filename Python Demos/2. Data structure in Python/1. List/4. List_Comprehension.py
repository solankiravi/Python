

# 1. new_list = [expression for member in iterable (if conditional)]
#Find all the vowels
sentence = 'the rocket came back from mars'
vowels = [word for word in sentence if word in 'aieou']
print(vowels)
# 2. new_list = [expression (if conditional) for member in iterable]
original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
#Replace negative value by 0
actual_price=[price if price > 0 else 0 for price in original_prices] 
print(actual_price)