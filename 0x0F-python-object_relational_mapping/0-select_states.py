#!/usr/bin/python3
"""
A script that lists all states from the
database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv


def main():
    """this is to make a database connection
    """
    User = argv[1]
    Passwrd = argv[2]
    DataBase = argv[3]
    hostname = "localhost"
    con = MySQLdb.Connect(
        host=hostname, user=User,
        passwd=Passwrd, db=DataBase,
        port=3306)
    db = con.cursor()
    db.execute("SELECT * FROM states ORDER BY id ASC")
    rows = db.fetchall()
    for row in rows:
        print(row)

if __name__ == "__main__":
    main()
    