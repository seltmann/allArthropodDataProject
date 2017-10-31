-- Host: localhost    Database: symbscan
-- ------------------------------------------------------
 
-- Table structure for table `sums`
--
 
DROP TABLE IF EXISTS `dups`;
CREATE TABLE `dups` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `occid` int(10) DEFAULT NULL,
  `catalogNumber` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

