'''
Create a list of all odd numbers between 1 and a max number. 
Max number is something you need to take from a user using input() function
'''


def populate_list():
    max_number=int(input('Input any number - (NA :tring and float)'))
    max_list=[]
    for i in range(0,max_number):
        if i % 2 == 0:
            max_list.append(i)
    print(max_list)

retry_count=0
try:
    populate_list()
except Exception as identifier:
    retry_count += 1
    print(f"Enter a valid number.. Retrying {retry_count}")
    populate_list()


