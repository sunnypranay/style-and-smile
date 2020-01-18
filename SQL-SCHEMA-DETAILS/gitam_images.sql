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
-- Table structure for table `images`
--

DROP TABLE IF EXISTS `images`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `images` (
  `UID` varchar(100) NOT NULL,
  `type` varchar(45) NOT NULL,
  `img_name` varchar(100) NOT NULL,
  `product_id` varchar(500) NOT NULL,
  KEY `UUID_idx` (`UID`),
  CONSTRAINT `UID` FOREIGN KEY (`UID`) REFERENCES `freelancer` (`UUID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `images`
--

LOCK TABLES `images` WRITE;
/*!40000 ALTER TABLE `images` DISABLE KEYS */;
INSERT INTO `images` VALUES ('123124','Nail Art','one.png','2'),('123124','Nail Art','two.png','2'),('123124','Mehendi','three.png','1'),('123124','Mehendi','four.png','1'),('123124','Nail Art','five.png','3'),('123124','Nail Art','six.png','3'),('123123','Nail Art','seven.png','4'),('123123','Nail Art','eight.png','4'),('123123','Mehendi','nine.png','5'),('123123','Mehendi','ten.png','5'),('00001','Mehendi-Arabic','f733c495-85a4-4e0c-882e-39bc47de61cb00001.jpg','3e35a569-7686-4fec-90d0-ec30d1a2f87d'),('00001','Mehendi-Arabic','7be4b916-dd89-4c7d-93ea-f867d656137f00001.jpg','3e35a569-7686-4fec-90d0-ec30d1a2f87d'),('00001','Mehendi-Arabic','21c5555a-f1d8-42d7-b8d3-ab225cc8402700001.jpg','3e35a569-7686-4fec-90d0-ec30d1a2f87d'),('00001','Mehendi-Arabic','7ad41122-859d-4be0-bbb2-19ed3a04486f00001.png','3e35a569-7686-4fec-90d0-ec30d1a2f87d'),('00001','Mehendi-Arabic','c21b03cb-f916-43d9-8266-d1381791217700001.png','3e35a569-7686-4fec-90d0-ec30d1a2f87d'),('00001','Mehendi-Arabic','b171bcc5-5fa1-4f03-8be1-6b33762b4de600001.png','3e35a569-7686-4fec-90d0-ec30d1a2f87d'),('00001','Nail-Art','549d6e9d-7c60-4d70-aa93-ea64be28228200001.png','e4ad03c5-985c-4450-b49e-7b0696b5117e'),('00001','Nail-Art','f30448fe-4427-45c7-94de-41f3799653eb00001.jpg','e4ad03c5-985c-4450-b49e-7b0696b5117e'),('00002','Nail-Art','1a65f148-1969-4ccb-8796-fd31c3794ce900002.png','d1a00335-d2cb-40a2-81db-8a02fc62397c'),('00002','Nail-Art','a443bd04-dbbf-4373-a557-b34b0cfe9fdd00002.jpg','d1a00335-d2cb-40a2-81db-8a02fc62397c');
/*!40000 ALTER TABLE `images` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-01-18 18:14:53
