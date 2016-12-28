#Mapping of time series of all arthropod collecting events
#kseltmann 2014@2016

rm(list=ls())
install.packages("eeptools")

library(maps)
library(mapdata)
library(maptools)  #for shapefiles
library(scales)  #for transparency

plot.new()

samps <- read.table(file="GeoBetween.tsv",sep="\t", header=TRUE)   #my data for sampling sites, contains a column of "decimalLatitude" and a column of "decimalLongitude" with GPS points in decimal degrees

head(samps$decimalLatitude)

#pdf(file='1811.pdf',height=10, width=10)

	map("worldHires","Canada", col="gray90", xlim = range(samps$decimalLongitude), ylim = range(samps$decimalLatitude),fill=TRUE)  
	map("worldHires","Mexico", col="gray90", xlim = range(samps$decimalLongitude), ylim = range(samps$decimalLatitude),fill=TRUE,add=TRUE)
	map("worldHires","usa", col="gray90", xlim = range(samps$decimalLongitude), ylim = range(samps$decimalLatitude),fill=TRUE,add=TRUE)
	map("state", col="gray95", boundary = False, xlim = range(samps$decimalLongitude), ylim = range(samps$decimalLatitude),fill=TRUE, add=TRUE)
	box()
	
#not required because creating one map	
#for (x in unique(samps$t)) {
#	samps.subset <- subset(samps, t == x)
#	points(samps.subset$decimalLongitude, samps.subset$decimalLatitude, pch=19, col = "red", cex=.05)
#	#title(x)
#	}
	
# puts down series of points	
colors = c("#cccc81")
points(samps$decimalLongitude, samps$decimalLatitude, pch=19, col = colors, cex=.005)	

#pdf(file='specimenMap.pdf',height=10, width=10)
		help(map)
dev.off()
help(rect)

#if (require(maps)) {
#states <- map_data("state")
#arrests <- USArrests
#names(arrests) <- tolower(names(arrests))
#arrests$region <- tolower(rownames(USArrests))

#choro <- merge(states, arrests, sort = FALSE, by = "region")
#choro <- choro[order(choro$order), ]
#qplot(decimalLongitude, decimalLatitude, data = choro, group = group, fill = assault,
geom="polygon")
#qplot(decimalLongitude, decimalLatitude, data = choro, group = group, fill = assault / murder,
geom="polygon")
#}
