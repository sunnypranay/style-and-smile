-- MySQL dump 10.13  Distrib 8.0.18, for Win64 (x86_64)
--
-- Host: localhost    Database: gitam
-- ------------------------------------------------------
-- Server version	8.0.18

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `design`
--

DROP TABLE IF EXISTS `design`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `design` (
  `UUID` varchar(100) NOT NULL,
  `type` varchar(45) NOT NULL,
  `description` varchar(1000) NOT NULL,
  `price` int(11) NOT NULL,
  `product_id` varchar(500) NOT NULL,
  PRIMARY KEY (`product_id`),
  KEY `UUID_idx` (`UUID`),
  CONSTRAINT `UUID` FOREIGN KEY (`UUID`) REFERENCES `freelancer` (`UUID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `design`
--

LOCK TABLES `design` WRITE;
/*!40000 ALTER TABLE `design` DISABLE KEYS */;
INSERT INTO `design` VALUES ('123124','Mehendi','Flower',50,'1'),('123124','Nail Art','Flower',50,'2'),('123124','Nail Art','Flower',50,'3'),('00001','Mehendi-Arabic','Best known for their free-flowing trails and modish appearance, Arabic mehndi designs have an unparalleled eye-pleasing charm. They are unsurprisingly one of the most loved and sought after kind of mehndi designs among women of all ages',150,'3e35a569-7686-4fec-90d0-ec30d1a2f87d'),('123123','Nail Art','Flower',50,'4'),('123123','Mehendi','Flower',50,'5'),('00002','Nail-Art','Nail art is a creative way to paint, decorate, enhance, and embellish the nails. It is a type of artwork that can be done on fingernails and toenails, usually after manicures or pedicures.',89,'d1a00335-d2cb-40a2-81db-8a02fc62397c'),('00001','Nail-Art','Nail art is a creative way to paint, decorate, enhance, and embellish the nails. It is a type of artwork that can be done on fingernails and toenails, usually after manicures or pedicures.',98,'e4ad03c5-985c-4450-b49e-7b0696b5117e'),('00002','Nail-Art','Nail art is a creative way to paint, decorate, enhance, and embellish the nails. It is a type of artwork that can be done on fingernails and toenails, usually after manicures or pedicures. ',100,'f4045caa-bcbd-437f-8e44-1d0a5cdd26ef');
/*!40000 ALTER TABLE `design` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-01-18 18:14:54
