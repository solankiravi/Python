from abc import abstractclassmethod, abstractmethod
from srp import Logger
import logging
import sqlite3
from sqlite3 import Error
import abc
from abc import ABC, abstractmethod



# class ErrorLogger(Logger):

#     def WriteToTextFile(self,message):
#         with open('log.txt', 'a') as writer:
#             writer.write(message,+'\n')
#             writer.flush()
    
#     def WriteToDB(self,message):
#         con=sqlite3.connect(r'Helpers\sqldb.db')
#         query=f"insert into ErrorLog values {message}"
#         con.execute(query)
#         con.commit()


class BaseLogger(ABC):
    @abstractmethod
    def writelog(self,message):
        pass

class DBLogger(BaseLogger):
    def writelog(self, message):
        con=sqlite3.connect(r'Helpers\sqldb.db')
        query=f"insert into ErrorLog values {message}"
        con.execute(query)
        con.commit()
    

class TxtLogger(BaseLogger):
    
    def writelog(self, message):
        with open('log.txt', 'a') as writer:
            writer.write(message,+'\n')
            writer.flush()




