import imp
from models import Person
from typing import List

def showAllView(data : List[Person]):
    print(f"No of users = {len(data)}")
    for item in data:
        print(item.first_name)

def startView():
    print("Start View")

def endView():
    print("End View")