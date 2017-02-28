#!/usr/bin/python
# view_rows.py - Fetch and display the rows from a MySQL database query
# import the MySQLdb and sys modules
# katja seltmann April 16, 2013 to run on arthropod data in scan symbiota database

import MySQLdb
import sys

moduleName = input('/raid/scratch/seltmann/allArthropodDataProject/includes.py')
import_module(moduleName)

#add date to file export
from datetime import date
now = date.today()

#connection information from mysql
#main database
#connect = MySQLdb.connect("127.0.0.1", user="", passwd="", db="" )

#test database
#connect = MySQLdb.connect("127.0.0.1", user="", passwd="", db="" )

cursor = connect.cursor ()

#define an outfile
outfilename = "allDuplicates_%s.tsv" % now
outfile = open(outfilename, 'w')


def GeoCoordinated():
	cursor.execute ("""SELECT catalogNumber, locality, genus, specificEpithet, COUNT(*) c FROM omoccurrences WHERE catalogNumber REGEXP '[a-z]' GROUP BY catalogNumber, locality, genus, specificEpithet HAVING c > 1 limit 10;""")
	data = cursor.fetchall()
	for x in data:
		concat_string = x[1]
		print concat_string
		catalogNumber = str(x[0])

		cursor.execute ("""select collid, institutionCode, catalogNumber, locality, family, genus, specificEpithet where catalogNumber=""" +  "'" + catalogNumber + "'")
		data = cursor.fetchall()
		a = "Executed: %s" % catalogNumber + "\n"
		print a
		outfile.write(a)
		for x in data:
			b = "\t ".join([str(c) for c in x]) + "\n"
			outfile.write(b)
		outfile.write('\n')
				
GeoCoordinated()	

#close all connections
cursor.close()
connect.close()
sys.exit()
