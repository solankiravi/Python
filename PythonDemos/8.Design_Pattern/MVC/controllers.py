from models import Person
import views

def showAll():
    person_db = Person.getAll()
    return views.showAllView(person_db)

def start():
    views.startView()
    showAll()
    views.endView()

if __name__=="__main__":
    start()