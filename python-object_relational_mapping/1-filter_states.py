#!/usr/bin/python3
"""Module to display certain states"""
import sys
import MySQLdb as mysql

if __name__ == "__main__":
    connector = mysql.connect(host="localhost", port=3306,
                              user=sys.argv[1], passwd=sys.argv[2],
                              db=sys.argv[3])
    cur = connector.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    x = cur.fetchall()
    for i in x:
        print(x)
    cur.close()
    connector.close()
