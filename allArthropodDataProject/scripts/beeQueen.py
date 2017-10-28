#!/usr/bin/python
# insectList - Fetch and display the rows from a MySQL database query
# import the MySQLdb and sys modules
# katja seltmann October 27, 2017 to run on scan data

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
outfilename = "../output/specimenDataBee_%s.tsv" % now
outfile = open(outfilename, 'w')

#define a criteria for a list of insects
def insectList():
	cursor.execute ("""select distinct sciname from omoccurrences where family='Apidae' and sciname !='Bombus' and sciname !='Bombus suckleyi ?' and sex='Female_Queen';""")
	data = cursor.fetchall()
	for x in data:
		name = x[0]
        allInsects(name)
        
#get all records whose scientific name match that list
def allInsects(name):
        cursor.execute ("""select distinct year, sciname, eventDate,decimalLatitude,decimalLongitude,associatedTaxa,sex from omoccurrences where decimalLatitude !='0.0000' and sciname =""" +  "'" + name + "'")
        bees = cursor.fetchall()
        for x in bees:
            a = "Executed: %s" % x + "\n"
            print a
            b = "\t ".join([str(c) for c in x]) + "\n"
            outfile.write(b)   
        outfile.write('\n')
	
    			
insectList()	


#close all connections
cursor.close()
connect.close()
sys.exit()


