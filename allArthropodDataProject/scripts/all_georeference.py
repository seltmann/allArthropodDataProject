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
outfilename = "geocoordAll_%s.tsv" % now
outfile = open(outfilename, 'w')


def GeoCoordinated():
	cursor.execute ("""select distinct family, genus, specificEpithet, decimalLatitude,decimalLongitude from omoccurrences where decimalLatitude !='0.0000' and specificEpithet !='UNKNOWN_NULL'""")
	data = cursor.fetchall()
	for x in data:
		b = "\t ".join([str(c) for c in x]) + "\n"
		outfile.write(b)
	outfile.write('\n')
				
GeoCoordinated()	

#close all connections
cursor.close()
connect.close()
sys.exit()
