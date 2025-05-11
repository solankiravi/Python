n = int(input())
# Convert n to binary and remove the '0b' prefix
binary_n = str(bin(n)[2:])
print(binary_n)
# Find the maximum number of consecutive 1's in the binary representation of n
max_con=0
current_con=0
for item in binary_n:
    if item == '1':
        current_con += 1
        max_con = max(max_con, current_con)
        continue
    current_con=0
print(max_con)