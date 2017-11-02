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
		cursor.execute ("""INSERT INTO GeoSums (occid,fOrder,rank,sciname,georeferenced,geoRound) VALUES(NULL,NULL,NULL,"%s",NULL,NULL);"""% (sciname))
		connect.commit()
	except:
		connect.rollback()

def SciName():
	cursor.execute ("""select distinct sciname from omoccurrencesESA""")
	data = cursor.fetchall()
	for x in data:
		sciname = x[0]
		InsertMysql(sciname)
        
def GetOrder():
	cursor.execute ("""select occid,sciname from geoSumsName where family is NULL""")
	data = cursor.fetchall()
	for x in data:
		sciname = x[1]
		occid = str(x[0])

		cursor.execute ("""select family from omoccurrencesESA where sciname=""" +  "'" + sciname + "'" + """ limit 1""")
		data = cursor.fetchone()
        if data:
            try:
                local = str(data[0])
                cursor.execute ("""update geoSumsName set family = '%s' where occid = '%s';"""% (local,occid))
                connect.commit()
            except:
                connect.rollback()
                
#def Family():
    	#cursor.execute ("""update GeoSums join omoccurrencesESA set GeoSums.family=omoccurrencesESA.family where GeoSum.sciname=omoccurrencesESA.sciname;""")

def Georeferenced():
	cursor.execute ("""select occid,sciname from GeoSums where georeferenced is NULL""")
	data = cursor.fetchall()
	for x in data:
		sciname = x[1]
		occid = str(x[0])

		cursor.execute ("""select count(distinct decimalLatitude,decimalLongitude) from omoccurrencesESA where sciname=""" +  "'" + sciname + "'")
		data = cursor.fetchone()
		local = data[0]
		if data:
			try:
				cursor.execute ("""update GeoSums set georeferenced = '%s' where occid = '%s';"""% (local,occid))
				connect.commit()
			except:
				connect.rollback()
                
def GeoRound():
	cursor.execute ("""select occid,sciname from GeoSums where geoRound is NULL""")
	data = cursor.fetchall()
	for x in data:
		sciname = x[1]
		occid = str(x[0])

		cursor.execute ("""select count(distinct round(decimalLatitude,4),round(decimalLongitude,4)) from omoccurrencesESA where decimalLatitude is not null and sciname=""" +  "'" + sciname + "'")
		data = cursor.fetchone()
		local = data[0]
		if data:
			try:
				cursor.execute ("""update GeoSums set geoRound = '%s' where occid = '%s';"""% (local,occid))
				connect.commit()
			except:
				connect.rollback()                

#SciName()
#Georeferenced()
#GeoRound()
GetOrder()
#connect.close()

#update GeoSums join omoccurrencesESA set GeoSums.family=omoccurrencesESA.family where GeoSums.sciname=omoccurrencesESA.sciname;
		
# DROP TABLE IF EXISTS `GeoSums`;
# CREATE TABLE `GeoSums` (
#   `occid` int(10) NOT NULL AUTO_INCREMENT,
#   `sciname` varchar(255) DEFAULT NULL,
#   `georeferenced` int(10) DEFAULT NULL,
#   `geoRound` int(10) DEFAULT NULL,
#   PRIMARY KEY (`occid`) USING BTREE
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
