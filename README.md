# allArthropodDataProject

The goal of this project is to evaluate all known arthropod data. We have a first draft that was presented at several meetings in 2014-2015. The new information starts July 2016. 

http://www.slideshare.net/taxonbytes/franz-cobb-seltmann-2015-spnhc-current-state-of-arthropod-biodiversity-data

http://www.slideshare.net/taxonbytes/cobb-seltmann-franz-2014-the-current-state-of-arthropod-biodiversity-data-addressing-impacts-of-global-change

#July 23 2016
new cleaned data from GBIF and SCAN DB from Ben Brandt.

#September 2016
Total number of records: 8,376,162

Total georeferenced localities: 7,121,499

Total distinct localities: 391,627

Total distinct families: 2,858

Total distinct species [concat family,genus,specificEpithet]: 111,660

Total number of families that have specimens determined to species: 2,283


#Data limits
	1. determined to species
	2. number of species per family bins of <30, >30, >100 distinct collecting events that are georeferenced

family, number <30, number >30, >100, >500, >1000

select family,count(*) from sums2 where georeferenced < 30 group by family;
select family,count(*) from sums2 where georeferenced >= 30 group by family;
select family,count(*) from sums2 where georeferenced >= 100 group by family;
select family,count(*) from sums2 where georeferenced >= 500 group by family;
select family,count(*) from sums2 where georeferenced >= 1000 group by family;
