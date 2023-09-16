#!/usr/bin/python3
"""
This script displays all values in the states table of hbtn_0e_0_usa where name matches the argument in a case-sensitive way.

Arguments: mysql username, mysql password, database name, state name
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

    # Use %s placeholder and BINARY operator for case-sensitive comparison
    cur.execute("SELECT * FROM states WHERE BINARY name LIKE %s
                ORDER BY id ASC", (state_name,))

    # Print all matching rows
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
