import secrets
import pandas

filepath = r'E:\Coding\Python\Python-Practice\Python Demos\1. Introduction of Python\Random_Name_Generator\helper\Data.xlsx'
team_name='FCA_CI'
df = pandas.read_excel(filepath,sheet_name=team_name,header=0)

team_members=df['Name']

list1=list(team_members)
list2=list(team_members)
counter=0
print("From => To")
for item in list1:
    val=secrets.choice(list2)
    if(item==val):
        if(counter >= 3):
            print("Sorry... No match found for {item}")
            break
        counter +=1 
        list1.append(item)
       
        print("Trying Again ...")
        continue
    else:
        counter=0
        print(f'{item} => '+ val)
        list2.remove(val)
