#!/usr/bin/python
# view_rows.py - Fetch and display the rows from a MySQL database query
# import the MySQLdb and sys modules
# katja seltmann April 16, 2013 to run on arthropod data in scan symbiota database

#run ExecuteMysql first

import MySQLdb
import sys

#connection information from mysql

#test database
#connect = MySQLdb.connect("", user="", passwd="", db="")

cursor = connect.cursor ()


def InsertMysql(family,genus,specificEpithet):
	try:
		cursor.execute ("""INSERT INTO sums2 (occid,family,genus,specificEpithet,coleventsLat,georeferenced) VALUES(NULL,"%s","%s","%s",NULL,NULL);"""% (family,genus,specificEpithet))
		connect.commit()
	except:
		connect.rollback()

def ExecuteMysql():
	cursor.execute ("""select distinct family,genus,specificEpithet from omoccurrences where specificEpithet != 'UNKNOWN_NULL'""")
	data = cursor.fetchall()
	for x in data:
		family = x[0]
		genus = x[1]
		specificEpithet = x[2]
		InsertMysql(family,genus,specificEpithet)

def ColeventsNOLAT():
	cursor.execute ("""select occid,scientificName from sums2 where georeferenced is NULL""")
	data = cursor.fetchall()
	for x in data:
		concat_string = x[1]
		occid = str(x[0])

		cursor.execute ("""select count(distinct decimalLatitude,decimalLongitude) from omoccurrences where decimalLatitude != '0.0000' and sciname=""" +  "'" + concat_string + "'")
		data = cursor.fetchone()
		local = data[0]
		if data:
			try:
				cursor.execute ("""update sums2 set georeferenced = '%s' where occid = '%s';"""% (local,occid))
				connect.commit()
			except:
				connect.rollback()

#did not use this script in 2015 analysis		
def GeoCoordinated():
		cursor.execute ("""select sums2.occid,omoccurrences.nameOMOConcat,count(distinct decimalLatitude,decimalLongitude,year,month,day) from omoccurrences join sums2 on omoccurrences.nameOMOConcat = sums2.nameConcat where decimalLatitude !='0.0000' and georeferenced is NULL group by omoccurrences.nameOMOConcat limit 20""")
		data = cursor.fetchall()
		for x in data:
			occid = x[0]
			georefenced = x[2]
			concat_string = x[1]
			print occid
			print concat_string
			print georefenced
			if x:
				try:
					cursor.execute ("""update sums2 set georeferenced = '%s' where occid = '%s';"""% (georefenced,occid))
					connect.commit()
				except:
					connect.rollback()	


#ExecuteMysql()
ColeventsNOLAT()
#GeoCoordinated()
connect.close()


	# cursor.execute ("""select occid,nameConcat from sums2 where georeferenced is NULL""")
	# data = cursor.fetchall()
	# for x in data:
	# 	concat_string = x[1]
	# 	print concat_string
	# 	occid = str(x[0])

		# cursor.execute ("""select count(distinct decimalLatitude,decimalLongitude,year,month,day) as locality from omoccurrences where decimalLatitude !='0.0000'  and concat(family,genus,specificEpithet) =""" +  "'" + concat_string + "'")
		# data = cursor.fetchone()
		# georefenced = data[0]
		# if data:
		# 	try:
		# 		cursor.execute ("""update sums2 set georeferenced = '%s' where occid = '%s';"""% (georefenced,occid))
		# 		connect.commit()
		# 	except:
		# 		connect.rollback()
		
# +-----------------+--------------+------+-----+---------+----------------+
# | Field           | Type         | Null | Key | Default | Extra          |
# +-----------------+--------------+------+-----+---------+----------------+
# | occid           | int(10)      | NO   | PRI | NULL    | auto_increment |
# | family          | varchar(255) | YES  |     | NULL    |                |
# | scientificName  | varchar(255) | YES  |     | NULL    |                |
# | genus           | varchar(255) | YES  |     | NULL    |                |
# | specificEpithet | varchar(255) | YES  |     | NULL    |                |
# | coleventsLat    | int(10)      | YES  |     | NULL    |                |
# | georeferenced   | int(10)      | YES  |     | NULL    |                |
# +-----------------+--------------+------+-----+---------+----------------+
