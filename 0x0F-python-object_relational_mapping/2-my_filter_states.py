#!/usr/bin/python3
"""this is a script to search for a user's input in the database"""
import MySQLdb
from sys import argv


def search():
    """
    this is a function that creates
    a database connection and do the
    select of the argv input
    """
    hostname = "localhost"
    User = argv[1]
    password = argv[2]
    database = argv[3]
    word = argv[4]
    con = MySQLdb.connect(
        host=hostname,
        user=User,
        passwd=password, db=database, port=3306)
    cur = con.cursor()
    querry = """SELECT * FROM states WHERE name = '{:s}'
            ORDER BY id ASC""".format(word)
    cur.execute(querry)
    rows = cur.fetchall()
    for row in rows:
        if row[1] == word:
            print(row)


if __name__ == "__main__":
    search()
