#!/usr/bin/python3
"""Module to display all states"""
import sys
import MySQLdb as mysql

connector = mysql.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
cursor = connector.cursor()
cursor.execute("SELECT * FROM states")
x = cursor.fetchall()
for i in x:
    print(x)
