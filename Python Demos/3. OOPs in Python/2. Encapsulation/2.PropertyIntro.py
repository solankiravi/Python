
class Person:

    def __init__(self,name) -> None:
        self.name=name
    
    @property
    def name(self):
        print("Getting the name")
        return self.__name
    
    @name.setter
    def name(self,val):
        print("Setting the name")
        self.__name=val
    
    def __str__(self) -> str:
        return f"{self._name}"

obj = Person("Ravi")
obj._name="Anil"
print(obj._name)