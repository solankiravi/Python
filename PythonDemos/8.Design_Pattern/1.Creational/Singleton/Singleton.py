
class Singleton:

    _instance = None

    @staticmethod
    def getInstance():
        if Singleton._instance == None:
            Singleton()
        return Singleton._instance
    
    def __init__(self) -> None:
        if Singleton._instance == None:
            Singleton._instance = self

if __name__=="__main__":
    s= Singleton()
    print(s)
    s= Singleton.getInstance()
    print(s)
    print(Singleton.getInstance())
