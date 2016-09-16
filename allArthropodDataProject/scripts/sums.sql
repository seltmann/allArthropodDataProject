-- Host: localhost    Database: symbscan
-- ------------------------------------------------------
 
-- Table structure for table `sums`
--
 
DROP TABLE IF EXISTS `sums2`;
CREATE TABLE `sums2` (
  `occid` int(10) NOT NULL AUTO_INCREMENT,
  `family` varchar(255) DEFAULT NULL,
  `scientificName` varchar(255) DEFAULT NULL,
  `genus` varchar(255) DEFAULT NULL,
  `specificEpithet` varchar(255) DEFAULT NULL,
  `coleventsLat` int(10) DEFAULT NULL,
  `georeferenced` int(10) DEFAULT NULL,
  PRIMARY KEY (`occid`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;