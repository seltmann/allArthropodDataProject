#!/usr/bin/python
# view_rows.py - Fetch and display the rows from a MySQL database query
# import the MySQLdb and sys modules
# katja seltmann April 16, 2013 to run on arthropod data in scan symbiota database

import MySQLdb
import sys

#add date to file export
from datetime import date
now = date.today()

#connect = MySQLdb.connect("localhost", user="", passwd="", db="" )
cursor = connect.cursor()

#insert statement moved out
def InsertMysql(occid, catalogNumber,family,genus,specificEpithet,locality):
	try:
		cursor.execute ("""insert into `dups` (occid, catalogNumber, family, genus, specificEpithet, locality) values (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")"""% (occid,catalogNumber,family,genus,specificEpithet,locality))
		connect.commit()
	except:
		connect.rollback()
		
def allDuplicates(catalogNumber):
	cursor.execute ("""SELECT catalogNumber, locality, genus, specificEpithet, family, occid FROM omoccurrences WHERE catalogNumber REGEXP '[a-z]' and catalogNumber=""" +  "'" + catalogNumber + "'")
	data = cursor.fetchall()
	for x in data:
		catalogNumber = str(x[0])
		locality = str(x[1])
		genus = str(x[2])
		specificEpithet = str(x[3])
		family = str(x[4])
		occid = x[5]
		InsertMysql(occid, catalogNumber,family,genus,specificEpithet,locality)
	

def Duplicates():
	cursor.execute ("""SELECT COUNT(*) cnt, catalogNumber FROM omoccurrences WHERE catalogNumber REGEXP '[a-z]' GROUP BY catalogNumber HAVING cnt > 1""")
	data = cursor.fetchall()
	for x in data:
		catalogNumber = str(x[1])
		allDuplicates(catalogNumber)


Duplicates()

#close all connections
cursor.close()
connect.close()
sys.exit()

