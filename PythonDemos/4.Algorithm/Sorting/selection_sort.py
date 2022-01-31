"""
1. consider first item as minium one
2. use two pointer approach
3. in the nested loop , get the minimum element repeatedily
4. finally, swap the elements 
"""

arr=[4,5,1,2,3]
print(arr)
for i in range(len(arr)):
    min_indx = i

    for j in range(i+1, len(arr)):
        if arr[min_indx] > arr[j]:
            min_indx = j
    
    arr[i], arr[min_indx] = arr[min_indx], arr[i]

print(arr)