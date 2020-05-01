class Employee:
    favSong = "Song 1"
    def __init__(self,firstName,lastName): 
        self.firstName = firstName
        self.lastName = lastName
    def FavSong(self):
        return self.favSong
    @classmethod    
    def SetFavSong(cls,favSong):
        cls.favSong = favSong

#creating objects
emp1 = Employee("Ravi","Solanki");emp2 = Employee("Vikash","Solanki")
#Calling class's Methods
Employee.favSong = "Song 2"
print(emp2.favSong);print(emp1.favSong)