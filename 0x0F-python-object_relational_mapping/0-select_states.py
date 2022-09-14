#!/usr/bin/python3
import MySQLdb
from sys import argv

def main():
    """this is to make a database connection 
    """
    User = argv[1]
    Passwrd = argv[2]
    DataBase = argv[3]
    hostname = "localhost"
    con = MySQLdb.Connect(host = hostname, user = User, passwd = Passwrd, db = DataBase, port=3306);
    db = con.cursor()
    db.execute("SELECT * FROM states")
    for row in db:
        print(row)


main()

