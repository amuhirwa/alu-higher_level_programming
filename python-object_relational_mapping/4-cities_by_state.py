#!/usr/bin/python3
"""Display cities by state"""
import sys
import MySQLdb as mysql

if __name__ == "__main__":
    if ';' in sys.argv[4]:
        exit()
    connector = mysql.connect(host="localhost", port=3306,
                              user=sys.argv[1], passwd=sys.argv[2],
                              db=sys.argv[3])
    cur = connector.cursor()
    cur.execute("SELECT * FROM states"
                "INNER JOIN cities"
                "ON states.id=cities.state_id"
                " ORDER BY cities.id ASC")
    x = cur.fetchall()
    for i in x:
        print(i)
    cur.close()
    connector.close()
