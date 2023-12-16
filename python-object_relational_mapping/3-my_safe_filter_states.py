#!/usr/bin/python3
"""Module to display states according to input but safe"""
import sys
import MySQLdb as mysql

if __name__ == "__main__":
    if ';' in sys.argv[4]:
        exit()
    connector = mysql.connect(host="localhost", port=3306,
                              user=sys.argv[1], passwd=sys.argv[2],
                              db=sys.argv[3])
    cur = connector.cursor()
    cur.execute("SELECT * FROM states WHERE name='{}'"
                " ORDER BY id ASC".format(sys.argv[4]))
    x = cur.fetchall()
    for i in x:
        print(i)
    cur.close()
    connector.close()
