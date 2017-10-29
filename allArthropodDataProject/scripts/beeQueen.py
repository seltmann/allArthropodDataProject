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
outfilename = "../output/specimenData_Bug_%s.tsv" % now
outfile = open(outfilename, 'w')

#define a criteria for a list of insects. List groups are defining different datasets
# def QueenBeeList():
#     cursor.execute ("""select distinct sciname from omoccurrences where family='Apidae' and sciname !='Bombus' and sciname !='Bombus suckleyi ?' and sex='Female_Queen';""")
#     data = cursor.fetchall()
#     for x in data:
#         name=x[0]
#         allInsects(name)

# def AllBeeList():
#     #outfilename = "../output/specimenData_allBee_%s.tsv" % now
#     #all bees from AMNH project
#     #177,058 messy scientific names
#     #12117312 records
#     cursor.execute ("""select distinct sciname from omoccurrences where collid='45' and family != 'UNKNOWN_NULL' or family !='Crabronidae' or family != 'Sphecidae';""")
#     data = cursor.fetchall()
#     for x in data:
#         name=x[0]
#         allInsects(name)
        
def AllBugList():
    #outfilename = "../output/specimenData_Bug_%s.tsv" % now
    #all PlantBugs from AMNH project
    #1780 distinct scientific names
    #1644 distinct associatedTaxa
    #178291 data records
    cursor.execute ("""select distinct sciname from omoccurrences where family='Miridae' and collid='93';""")
    data = cursor.fetchall()
    for x in data:
        name=x[0]
        allInsects(name)            
        
#get all records whose scientific name match
def allInsects(name):
    cursor.execute ("""select year, sciname, eventDate,decimalLatitude,decimalLongitude,associatedTaxa,sex from omoccurrences where decimalLatitude !='0.0000' and sciname =""" +  "'" + name + "'")
    bees = cursor.fetchall()
    for x in bees:
        b = "\t ".join([str(c) for c in x]) + "\n"
        outfile.write(b)
    outfile.write('\n')
	
    			
AllBugList()	


#close all connections
cursor.close()
connect.close()
sys.exit()


