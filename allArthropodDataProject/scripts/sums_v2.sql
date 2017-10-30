-- Host: localhost    Database: symbscan
-- ------------------------------------------------------
 
-- Table structure for table `sums`
--
 
DROP TABLE IF EXISTS `GeoSums`;
CREATE TABLE `GeoSums` (
  `occid` int(10) NOT NULL AUTO_INCREMENT,
  `sciname` varchar(255) DEFAULT NULL,
  `georeferenced` int(10) DEFAULT NULL,
  `geoRound` int(10) DEFAULT NULL,
  PRIMARY KEY (`occid`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

