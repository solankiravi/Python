numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Function that filters out all numbers which are odd
def filter_odd_numbers(num):
    return True if num%2 == 0 else False

filtered_numbers = filter(filter_odd_numbers, numbers)

print(filtered_numbers)
# filtered_numbers = [2, 4, 6, 8, 10, 12, 14]    