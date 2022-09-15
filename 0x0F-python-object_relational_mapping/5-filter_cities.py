#!/usr/bin/python3
"""this is the all cities by state script"""

import MySQLdb
from sys import argv


def cities_by_state():
    """takes in 4 arguments"""
    hostname = "localhost"
    User = argv[1]
    password = argv[2]
    database = argv[3]
    state = argv[4]
    con = MySQLdb.connect(
        host=hostname,
        user=User,
        passwd=password,
        db=database,
        port=3306
    )
    cur = con.cursor()
    cur.execute(
        """SELECT c.name
        FROM cities AS c
        JOIN states AS s
        ON c.state_id = s.id
        AND s.name = %s""",
        (state,))
    rows = cur.fetchall()
    city = []
    for row in rows:
        city.append(row[0])
    print(", ".join(city))


if __name__ == "__main__":
    cities_by_state()
