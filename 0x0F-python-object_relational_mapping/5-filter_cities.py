#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    conn = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cur = conn.cursor()

    cur.execute("""
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """, (state_name,))
    query_rows = cur.fetchall()

    cities = ', '.join(row[0] for row in query_rows)
    print(cities)

    cur.close()
    conn.close()

