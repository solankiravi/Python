import sqlite3
from sqlite3 import Error

class User:

    def registerUser(self, uname,passwd,email):
        con=sqlite3.connect(r'Helpers\\sqldb.db')
        query=f"insert into users values {uname}, {passwd}, {email}"
        con.execute(query)
        con.commit()
        print(f"User Registration Succesful - {uname}")

import logging
class Logger:
    def WriteLog(self,message):
        logging.log(message)
