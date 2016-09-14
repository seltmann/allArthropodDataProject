#!/usr/bin/python
# view_rows.py - Fetch and display the rows from a MySQL database query
# import the MySQLdb and sys modules
# katja seltmann April 16, 2013 to run on arthropod data in scan symbiota database

import MySQLdb
import sys

#add date to file export
from datetime import date
now = date.today()

#connection information from mysql
#main database
connect = MySQLdb.connect("127.0.0.1", user="", passwd="", db="" )

#test database
#connect = MySQLdb.connect("127.0.0.1", user="", passwd="", db="" )

cursor = connect.cursor ()

#define an outfile
outfilename = "scientificNameCounts_%s.tsv" % now
outfile = open(outfilename, 'w')

#function to execute mysql commands one at a time
def ExecuteMysql(line):
	if line:
		cursor.execute ("""%s"""% (line))
		a = "Executed: %s" % line + "\n"
		print a
		outfile.write(a)
		data = cursor.fetchall()
		for x in data:
			b = "\t ".join([str(c) for c in x]) + "\n"
			outfile.write(b)
		outfile.write('\n')
	
#open and iterate through commands, can add to this list
infilename = 'master.txt'
infile = open(infilename, 'r')
	
for line in infile:
	line = line.strip()
	ExecuteMysql(line)

#close all connections
cursor.close()
connect.close()
sys.exit()
