#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)
    
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    conn.close()

