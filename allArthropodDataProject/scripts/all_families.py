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
outfilename = "allFamilies_%s.tsv" % now
outfile = open(outfilename, 'w')


def orderFind(family):
	cursor.execute ("""SELECT familyOrder, family FROM omoccurrences WHERE catalogNumber REGEXP '[a-z]' and family=""" +  "'" + family + "'")
	data = cursor.fetchall()
	for x in data:
		b = "\t ".join([str(c) for c in x]) + "\n"
		outfile.write(b)
	outfile.write('\n')
    
def familyFind():
	cursor.execute ("""select distinct family from omoccurrences where familyOrder is null""")
	data = cursor.fetchall()
	for x in data:
		family = str(x[1])
		orderFind(family)
				
familyFind()	

#close all connections
cursor.close()
connect.close()
sys.exit()
