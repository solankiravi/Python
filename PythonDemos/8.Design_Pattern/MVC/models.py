from dataclasses import dataclass
import json,os

class Person(object):
    DB_URL = os.path.join(os.path.dirname(__file__),'db.json')

    def __init__(self, first_name : str =None, last_name : str = None) -> None:
        self.first_name=first_name
        self.last_name = last_name

    def name(self):
        return f"{self.first_name} {self.last_name}"
    
    @classmethod
    def getAll(self):
        results = []
        items = json.load(open(self.DB_URL))

        for item in items:
            person = Person(item['first_name'], item['last_name'])
            results.append(person)
        return results
        