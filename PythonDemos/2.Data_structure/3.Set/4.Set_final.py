some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

#Find duplicates in the list
duplicates = []
# for ele in some_list:
#     if some_list.count(ele) > 1:
#         if ele not in duplicates:
#             duplicates.append(ele)
# print(duplicates)

duplicates = set([x for x in some_list if some_list.count(x) > 1])
print(duplicates)