int_arr=[3,4,1,10,6,7,-3,5,0]
number=7
"""
pair sum(a,b)=k
(3,4)
(7,0)
(10-3)
"""
list_of_pairs=[]
temp_arr=sorted(int_arr)
temp_arr.append(0)
#[-3,0,1,3,4,5,6,7,10].append(0)

for index, val in enumerate(temp_arr[:-1]):
	if(val + temp_arr[index+1] == number):
		list_of_pairs.append((val, temp_arr[index+1]))

print(list_of_pairs)