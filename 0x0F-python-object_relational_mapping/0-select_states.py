#!/usr/bin/python3
"""
This script that lists all states from 
the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    curs = db.cursor()
    curs.execute("SELECT * FROM states ORDER BY id ASC")
    for row in curs.fetchall():
        print(row)
    curs.close()
    db.close()

