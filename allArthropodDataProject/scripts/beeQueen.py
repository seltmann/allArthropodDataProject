#!/usr/bin/python
# insectList - Fetch and display the rows from a MySQL database query
# import the MySQLdb and sys modules
# katja seltmann October 27, 2017 to run on scan data

import MySQLdb
import sys
import os
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('../config.ini')
username = config.get('mysqlDB', 'user')
hostname = config.get('mysqlDB', 'host')
password = config.get('mysqlDB','password')
database = config.get('mysqlDB','db')

quotes = """
connect = MySQLdb.connect("127.0.0.1", user= quotes + username + quotes, passwd=password + quotes, db=quotes + database + quotes)
cursor = connect.cursor()

#add date to file export
from datetime import date
now = date.today()

#define an outfile
outfilename = "specimenDataBee_%s.tsv" % now
outfile = open(outfilename, 'w')

def insectList():
	cursor.execute ("""select distinct sciname from omoccurrences where family="Apidae" and sciname !="Bombus" and sciname !="Bombus suckleyi ?" and sex="Female_Queen";""")
	data = cursor.fetchall()
	for x in data:
		name = x[0]
		print name

        # cursor.execute ("""select distinct year, sciname, eventDate,decimalLatitude,decimalLongitude,associatedTaxa,sex from omoccurrences where decimalLatitude !='0.0000' and sciname =""" +  "'" + name + "'")
        # data = cursor.fetchall()
        # a = "Executed: %s" % name + "\n"
        # print a
        # outfile.write(a)
        # for x in data:
        #     b = "\t ".join([str(c) for c in x]) + "\n"
        #     outfile.write(b)
        # outfile.write('\n')
				
insectList()	


#close all connections
cursor.close()
connect.close()
sys.exit()


