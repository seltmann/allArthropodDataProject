#!/usr/bin/python
# view_rows.py - Fetch and display the rows from a MySQL database query
# import the MySQLdb and sys modules
# katja seltmann April 16, 2013 to run on arthropod data in scan symbiota database

import MySQLdb
import sys

#add date to file export
from datetime import date
now = date.today()

connect = MySQLdb.connect("", user="", passwd="", db="" )
cursor = connect.cursor ()

#define an outfile
#outfilename = "allDuplicatesAlpha_%s.tsv" % now
#outfile = open(outfilename, 'w')
#outfile.write('select occid \t collid \t institutionCode \t catalogNumber \t otherCatalogNumbers \t family \t genus \t specificEpithet \t country \t stateProvince \t municipality \t locality \t decimalLongitude \t decimalLatitude \n')


def Duplicates():
	cursor.execute ("""SELECT catalogNumber, locality, genus, specificEpithet, occid, family, COUNT(*) c FROM omoccurrences WHERE catalogNumber REGEXP '[a-z]' GROUP BY catalogNumber, locality, genus, specificEpithet HAVING c > 1 limit 10;""")
	data = cursor.fetchall()
	for x in data:
		catalogNumber = str(x[0])
		locality = str(x[1])
		genus = str(x[2])
		specificEpithet = str(x[3])
		occid = str(x[4])
		family = str(x[5])
		print catalogNumber

		#sql = """select occid, collid, institutionCode, catalogNumber, otherCatalogNumbers, family, genus, specificEpithet,country, stateProvince, municipality, locality, decimalLongitude, decimalLatitude from omoccurrences where catalogNumber=\"%s\" and locality=\"%s\" and genus=\"%s\" and specificEpithet=\"%s\";""" % (catalogNumber,locality,genus,specificEpithet)
		sql = """insert into `dups` (occid, catalogNumber, family, genus, specificEpithet, locality) values (occid=\"%s\", catalogNumber=\"%s\",family=\"%s\",genus=\"%s\",specificEpithet=\"%s\",locality=\"%s\");""" % (occid,catalogNumber,family,genus,specificEpithet,locality)

		print sql
		cursor.execute(sql)
		#data = cursor.fetchall()
		a = "Executed: %s" % catalogNumber + "\n"
		print a
		#outfile.write(a)
		#for x in data:
		#	b = "\t ".join([str(c) for c in x]) + "\n"
		#	outfile.write(b)
		#outfile.write('\n')
				
Duplicates()

#close all connections
cursor.close()
connect.close()
sys.exit()


#SELECT catalogNumber, locality, genus, specificEpithet, COUNT(*) c FROM omoccurrences WHERE catalogNumber REGEXP '[a-z]' GROUP BY catalogNumber, locality, genus, specificEpithet HAVING c > 1;

#sort -k 4 file.txt
#awk '{outfile=sprintf("file%02d.txt",NR/100000+1);print > outfile}' yourfile

#/usr/bin/python allDuplicates-v2.py

#cursor.execute ("""SELECT catalogNumber, institutionCode, locality, genus, specificEpithet, COUNT(*) c FROM omoccurrences WHERE catalogNumber REGEXP '^[0-9]*$' GROUP BY institutionCode,catalogNumber, locality, genus, specificEpithet HAVING c > 1 order by institutionCode,catalogNumber;""")
#sql = """select occid, collid, institutionCode, catalogNumber, otherCatalogNumbers, family, genus, specificEpithet,country, stateProvince, municipality, locality, decimalLongitude, decimalLatitude from omoccurrences where catalogNumber=\"%s\" and institutionCode=\"%s\" and locality=\"%s\" and genus=\"%s\" and specificEpithet=\"%s\";""" % (catalogNumber,institutionCode,locality,genus,specificEpithet)

#cursor.execute ("""SELECT catalogNumber, locality, genus, specificEpithet, COUNT(*) c FROM omoccurrences WHERE catalogNumber REGEXP '[a-z]' GROUP BY catalogNumber, locality, genus, specificEpithet HAVING c > 1;""")
#sql = """select occid, collid, institutionCode, catalogNumber, otherCatalogNumbers, family, genus, specificEpithet,country, stateProvince, municipality, locality, decimalLongitude, decimalLatitude from omoccurrences where catalogNumber=\"%s\" and locality=\"%s\" and genus=\"%s\" and specificEpithet=\"%s\";""" % (catalogNumber,locality,genus,specificEpithet)

#SELECT REPLACE(locality, '\"', '') from omoccurrences where catalogNumber="BBSL175528";
#UPDATE  omoccurrences set locality = REPLACE(%, '\"', '') where catalogNumber="BBSL175528";