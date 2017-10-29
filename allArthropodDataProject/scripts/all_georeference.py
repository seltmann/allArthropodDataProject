#!/usr/bin/python
# view_rows.py - Fetch and display the rows from a MySQL database query
# import the MySQLdb and sys modules
# katja seltmann April 16, 2013 to run on arthropod data in scan symbiota database

import MySQLdb
import sys
import os
import ConfigParser

#connection from config file with configparser
config = ConfigParser.ConfigParser()
config.read('../config.ini')
username = config.get('mysqlDB', 'user')
hostname = config.get('mysqlDB', 'host')
password = config.get('mysqlDB','password')
database = config.get('mysqlDB','db')

#connection to mysql
connect = MySQLdb.connect("localhost", user= username, passwd=password, db=database)
cursor = connect.cursor()

#add date to file export
from datetime import date
now = date.today()


#define an outfile
outfilename = "geocoordAll_%s.tsv" % now
outfile = open(outfilename, 'w')


def GeoCoordinated():
	cursor.execute ("""select distinct family, genus, specificEpithet, decimalLatitude,decimalLongitude from omoccurrences where decimalLatitude !='0.0000' and specificEpithet !='UNKNOWN_NULL' limit 10""")
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
