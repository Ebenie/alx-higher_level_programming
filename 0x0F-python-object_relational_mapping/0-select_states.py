#!/usr/bin/python3
import sys
import MySQLdb

def list_states(username, password, database):
    conn = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database)
    curs = conn.cursor()
    curs.execute("SELECT * FROM states ORDER BY states.id ASC")

    rows = curs.fetchall()


    for row in rows:
        print(row)

    curs.close()
    conn.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python 0-select_states.py <username> <password> <database>")
        sys.exit(1)
    
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)

