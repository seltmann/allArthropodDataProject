#!/usr/bin/python
# katja seltmann April 29, 2017


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


def InsertMysql(sciname):
	try:
		cursor.execute ("""INSERT INTO GeoSums (occid,sciname,georeferenced,geoRound) VALUES(NULL,"%s",NULL,NULL);"""% (sciname))
		connect.commit()
	except:
		connect.rollback()

def SciName():
	cursor.execute ("""select distinct sciname from omoccurrences where specificEpithet != 'UNKNOWN_NULL' and occid='20067418'""")
	data = cursor.fetchall()
	for x in data:
		sciname = x[0]
		InsertMysql(sciname)

def Georeferenced():
	cursor.execute ("""select occid,sciname from GeoSums where georeferenced is NULL""")
	data = cursor.fetchall()
	for x in data:
		sciname = x[1]
		occid = str(x[0])

		cursor.execute ("""select count(distinct decimalLatitude,decimalLongitude) from omoccurrences where decimalLatitude != '0.0000' and sciname=""" +  "'" + sciname + "'")
		data = cursor.fetchone()
		local = data[0]
		if data:
			try:
				cursor.execute ("""update GeoSums set georeferenced = '%s' where occid = '%s';"""% (local,occid))
				connect.commit()
			except:
				connect.rollback()
                
def GeoRound():
	cursor.execute ("""select occid,sciname from GeoSums where georeferenced is NULL""")
	data = cursor.fetchall()
	for x in data:
		sciname = x[1]
		occid = str(x[0])

		cursor.execute ("""select count(distinct round(decimalLatitude,4),round(decimalLongitude,4)) from omoccurrences where decimalLatitude != '0.0000' and sciname=""" +  "'" + sciname + "'")
		data = cursor.fetchone()
		local = data[0]
		if data:
			try:
				cursor.execute ("""update GeoSums set geoRound = '%s' where occid = '%s';"""% (local,occid))
				connect.commit()
			except:
				connect.rollback()                

SciName()
#Georeferenced()
#GeoRound()
connect.close()


		
# DROP TABLE IF EXISTS `GeoSums`;
# CREATE TABLE `GeoSums` (
#   `occid` int(10) NOT NULL AUTO_INCREMENT,
#   `sciname` varchar(255) DEFAULT NULL,
#   `georeferenced` int(10) DEFAULT NULL,
#   `geoRound` int(10) DEFAULT NULL,
#   PRIMARY KEY (`occid`) USING BTREE
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
