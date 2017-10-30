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

#insert statement moved out
def InsertMysql(family, Forder):
	try:
		cursor.execute ("""insert into `familyOrder` (occid, family, Forder) values (NULL,\"%s\",\"%s\")"""% (occid,family,Forder))
		connect.commit()
	except:
		connect.rollback()

def orderFind(family):
	cursor.execute ("""SELECT distinct familyOrder, family FROM omoccurrences WHERE family=""" +  "'" + family + "'")
	data = cursor.fetchall()
	for x in data:
		b = "\t ".join([str(c) for c in x]) + "\n"
        family = str(x[1])
        Forder = str(x[0])
        InsertMysql(family, Forder)
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

# DROP TABLE IF EXISTS `familyOrder`;
# CREATE TABLE `familyOrder` (
#   `occid` int(10) NOT NULL AUTO_INCREMENT,
#   `family` varchar(255) DEFAULT NULL,
#   `order` varchar(255) DEFAULT NULL,
#   PRIMARY KEY (`occid`) USING BTREE
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
