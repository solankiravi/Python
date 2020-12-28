'''
Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
'''

# NOTE: Use Dictionary for better performance.

# Approach 1 - Nested List : 

expense_list=[
    ['January',2200],
    ['February',2350],
    ['March',2600],
    ['April',2130],
    ['May',2190]
]

# In Feb, how many dollars you spent extra compare to January?
extra_spend_in_feb= expense_list[1][1]-expense_list[0][1]
print(extra_spend_in_feb)

# Find out your total expense in first quarter (first three months) of the year.
total_expense=0
for index, val in enumerate(expense_list[0:3]):
    total_expense += expense_list[index][1]
print(total_expense)

# Find out if you spent exactly 2000 dollars in any month
keyword=2600
for val in expense_list:
    print(val[0]) if keyword in val else None

#June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
june_expense=['June',1980]
expense_list.append(june_expense)

#You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this
expense_list[3][1] -= 200
print(expense_list)