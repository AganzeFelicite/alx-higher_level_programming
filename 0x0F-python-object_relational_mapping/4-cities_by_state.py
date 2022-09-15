#!/usr/bin/python3
"""this is a python script to print for printing states and the cities"""

import MySQLdb
from sys import argv


def cities():
    """this creates a conneection to the database"""
    hostname = "localhost"
    User = argv[1]
    password = argv[2]
    database = argv[3]
    con = MySQLdb.connect(
        host=hostname,
        user=User,
        passwd=password,
        db=database,
        port=3306)
    cur = con.cursor()
    cur.execute(
        """SELECT cities.id , cities.name, states.name
        FROM cities  JOIN states ON state_id = states.id
        ORDER BY cities.id""")
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    cities()
