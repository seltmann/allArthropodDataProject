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
outfilename = "geocoordState_%s.tsv" % now
outfile = open(outfilename, 'w')


def GeoCoordinated():
	cursor.execute ("""select occid,concat(family, genus, specificEpithet) from sums2 where georeferenced >= 30""")
	data = cursor.fetchall()
	for x in data:
		concat_string = x[1]
		print concat_string
		occid = str(x[0])

		cursor.execute ("""select distinct family, genus, specificEpithet, country,stateProvince,decimalLatitude,decimalLongitude from omoccurrences where decimalLatitude !='0.0000' and concat(family,genus,specificEpithet) =""" +  "'" + concat_string + "'")
		data = cursor.fetchall()
		a = "Executed: %s" % concat_string + "\n"
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

