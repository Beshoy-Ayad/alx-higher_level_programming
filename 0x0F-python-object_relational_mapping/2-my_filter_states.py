#!/usr/bin/python3

"""
This script lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE '{}'
                ORDER BY id ASC".format(state_name))

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
