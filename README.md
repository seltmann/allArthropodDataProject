# allArthropodDataProject

The goal of this project is to evaluate all known arthropod data as of May 2015 to see where our community has research ready data. 

# May 14 2015
select count(*) from omoccurrences; just scan data = 3943069 records (prior to adding AEC and GBIf)

	TODO: add a flag to the data for its origin

	DONE: added dataSource column to table

	TIME: 20 min for mysql to create new column or restore SCAN from source.
	
Downloading data from symbiota2.symbscan.occurrences table to upload on different server for merging with GBIF and AEC data

Renamed table to omo

#May 18 2015
created an import for AEC data to match new SCAN table structure

exporting all NA data from AEC

#May 20 2015
import into symbscan database AEC data using Load Data
create GBIF database from occurrence.txt files

#July 23 2016
new cleaned data from GBIF and SCAN DB from Ben Brandt.

