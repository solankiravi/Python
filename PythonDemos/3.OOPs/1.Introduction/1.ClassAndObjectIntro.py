#Class is created using class keyword
class Employee:
    pass
#creating objects
emp1 = Employee()
emp2 = Employee()
#Verify each objects are stored at different has memory
print(emp1);print(emp2)
#Assigning object's values
emp1.firstName = "Ravi";emp1.lastName = "Solanki";emp1.email="ravi.solanki@abcd.com"
emp2.firstName = "Vikash";emp2.lastName = "Solanki";emp2.email="vikash.solanki@abcd.com"
#Accessing object's value
print(emp1.email);print(emp2.email)