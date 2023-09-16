#!/usr/bin/python3

"""
This script lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    state_name = argv[4]

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE '{:s}'
                ORDER BY id ASC".format(state_name))

    for row in cur.fetchall():
        if row[1] == state_name:
            print(row)

    cur.close()
    db.close()
