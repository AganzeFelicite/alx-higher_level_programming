#!/usr/bin/python3
"""This a simple script that Write
 a script that lists all states with a
 name starting with N (upper N) from the database
"""
import MySQLdb
from sys import argv


def filters():
    """this function create an sql connection and sort the data
    """
    hostName = "localhost"
    User = argv[1]
    password = argv[2]
    database = argv[3]
    con = MySQLdb.connect(
        host=hostName,
        user=User,
        passwd=password,
        db=database)
    cur = con.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE \"N%\"")
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    filters()
