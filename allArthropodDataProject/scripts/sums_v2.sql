-- Host: localhost    Database: symbscan
-- ------------------------------------------------------
 
-- Table structure for table `sums`
--
 
DROP TABLE IF EXISTS `sums2`;
CREATE TABLE `sums2` (
  `occid` int(10) NOT NULL AUTO_INCREMENT,
  `order` varchar(255) DEFAULT NULL,
  `family` varchar(255) DEFAULT NULL,
  `sciname` varchar(255) DEFAULT NULL,
  `genus` varchar(255) DEFAULT NULL,
  `specificEpithet` varchar(255) DEFAULT NULL,
  `coleventsLat` int(10) DEFAULT NULL,
  `georeferenced` int(10) DEFAULT NULL,
  PRIMARY KEY (`occid`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;