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
outfilename = "stats_%s.tsv" % now
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
infilename = '../dataUpdates/cleaner-add/taxonomyESA.txt'
infile = open(infilename, 'r')
	
for line in infile:
	line = line.strip()
	ExecuteMysql(line)

#close all connections
cursor.close()
connect.close()
sys.exit()
