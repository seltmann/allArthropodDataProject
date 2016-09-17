#!/usr/bin/python
# view_rows.py - Fetch and display the rows from a MySQL database query
# import the MySQLdb and sys modules
# katja seltmann April 16, 2013 to run on arthropod data in scan symbiota database


#DO NOT USE

import MySQLdb
import sys
import os

os.system("/raid/scratch/seltmann/allArthropodDataProject/includes.py")

#add date to file export
from datetime import date
now = date.today()

#connection information from mysql
#main database
#connect = MySQLdb.connect("", user="", passwd="", db="" )

cursor = connect.cursor ()

#function to execute mysql commands one at a time
def ExecuteMysql(line):
	if line:
		cursor.execute ("""%s"""% (line))
		a = "Executed: %s" % line + "\n"
		print a
		
x = "9-updates_scan.txt"
	
infilename = "../dataUpdates/cleaner-add/"  + x
infile = open(infilename, 'r')

for line in infile:
	line = line.strip()
	ExecuteMysql(line)

#close all connections
cursor.close()
connect.close()
sys.exit()
