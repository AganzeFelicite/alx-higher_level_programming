#!/usr/bin/python3
"""this is safe search using a paramerised querry"""

import imp


import MySQLdb
from sys import argv


def gosafe():
    """this creates a database connection and do a safe querry"""
    hostname = "localhost"
    User = argv[1]
    password = argv[2]
    database = argv[3]
    word = argv[4]

    con = MySQLdb.connect(
        host=hostname,
        user=User,
        passwd=password,
        db=database,
        port=3306)
    cur = con.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC",
        (word,)
        )
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    gosafe()
