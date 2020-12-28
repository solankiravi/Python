# Given an integer array, output all pairs that sum up to a specific value k.
arr=[2,5,3,2,4,5,1,4,6,7,7,8]

def pairSum2(arr, k):
    if len(arr)<2:
        return
    seen=set()
    output=set()
    for num in arr:
        target=k-num
        if target not in seen:
            seen.add(num)
        else:
            output.add( (min(num, target), max(num, target)) )
    print('\n'.join( map(str, list(output)) ))

pairSum2(arr,9)