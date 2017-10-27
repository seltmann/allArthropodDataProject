#!/usr/bin/python
# insectList - Fetch and display the rows from a MySQL database query
# import the MySQLdb and sys modules
# katja seltmann October 27, 2017 to run on scan data

import MySQLdb
import sys
import os
import ConfigParser
import MySQLdb.cursors

config = ConfigParser.ConfigParser()
config.read('config.ini')

cur = MySQLdb.connect(host = config['mysqlDB']['host'],
                           user = config['mysqlDB']['user'],
                           passwd = config['mysqlDB']['pass'],
                           db = config['mysqlDB']['db'])
                           

#add date to file export
from datetime import date
now = date.today()

#define an outfile
outfilename = "specimenDataBee_%s.tsv" % now
outfile = open(outfilename, 'w')

def insectList():
	cur.execute ("""select distinct sciname from omoccurrences where family='Apidae' and sciname !='Bombus' and sciname !='Bombus suckleyi ?' and sex='Female_Queen';""")
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


