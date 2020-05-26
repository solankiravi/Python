# Given an integer array, output all pairs that sum up to a specific value k.
arr=[2,5,3,2,4,5,1,4,6,7,7,8]

def get_pair(arr,val):
    #base case handle
    if(len(arr) < 2):
        return    
    arr.sort()
    left,right = (0, len(arr) - 1)
    while left < right:
        temp = arr[left] + arr[right]
        if(temp == val):
            print(arr[left],arr[right])
            left +=1
        elif(temp < val):
            left += 1
        else:
            right -=1
get_pair(arr,9)