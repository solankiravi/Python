"""
Problem statement:

Count the number of occurrences for each element in list.

input =>
a=[1,2,2,3,4,4,4,5]

Output
1 => 1
2 => 2
3 => 1
4 => 3
5 => 1
"""
a=[1,2,2,3,4,4,4,5]
temp=[]
# for item in a:
#     if item not in temp:
#         print(f"{item} = {a.count(item)}")
#         temp.append(item)
"""List Comprehension"""
[(temp.append(item),print(f"{item} = {a.count(item)}")) for item in a if item not in temp]

# a=sorted(a)
# last_ele=None
# for index, item in enumerate(a):
#     if item != last_ele:
#         print(f"{item} = {a.count(item)}")
#         last_ele=item

# temp=[]
# for item in a:
#     count=0
#     for j in a:
#         if item == j:
#             count +=1
#     if item not in temp:
#         print(f"{item} = {count}")
#         temp.append(item)


# for item in set(a):
#     print(f"{item} = {a.count(item)}")

# temp={}
# for item in a:
#     count=0
#     for j in a:
#         if item == j:
#             count +=1
#     temp[item]=count
# print(temp)

# from collections import Counter
# print(Counter(a))    