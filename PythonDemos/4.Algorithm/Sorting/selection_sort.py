arr=[5,4,1,2,3]
print(arr)

def selection_sort(arr):
    n = len(arr)
    for out_ind in range(n) :
        min_ind=out_ind
        for inner_ind in range(out_ind+1,n):
            if arr[min_ind] > arr[inner_ind]:
                min_ind = inner_ind
        arr[out_ind], arr[min_ind] = arr[min_ind], arr[out_ind]
    return arr

print(selection_sort(arr))