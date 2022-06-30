-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: locochat
-- ------------------------------------------------------
-- Server version	8.0.28

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
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `token` varchar(200) NOT NULL,
  `userID` varchar(25) NOT NULL,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `phone_number` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `password_hashed` varchar(256) NOT NULL,
  `security_question_answer` varchar(100) NOT NULL,
  PRIMARY KEY (`userID`),
  UNIQUE KEY `token_UNIQUE` (`token`),
  UNIQUE KEY `phone_number_UNIQUE` (`phone_number`),
  UNIQUE KEY `userID_UNIQUE` (`userID`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('d33445fbd8d5b78d5f1b1ea90f71cb81e612c0f69a30748f66','amirfazel45','amirfazel','koozegar','09308100815','amirfazel45@gmail.com','fa2145a5ffc6812095af5f9926b1ba3d5156b3b2bbeec0fb07c13181f0fbfbcb','blue'),('87573dfd25145d77b6683ef81207952589b00f6fe5933f71df','Dummy1','dummy','dumdum','11111111111','dummy@gmail.com','eca24d737963e4b9a84a7e03fee6cef80c9d7c9894170cdd9e9b64979fbc2f91','dum color'),('7d726315c1822caefe6eafa10257b086dd22bbf54c1d979db6','Dummy4','Dummy4','dummy four','09444444444','dumy4@dummy.com','35af3f47035ba0b242b6e22df2e06b584d4e2c829631f869c9a897bebe6b4908','dummy color'),('f58edf61dd1f49fd1577e9edb13b14ce93a57a5a59576ee6c7','Dummy7','dummy 7','ds','09777777777','dum@dum.com','79a6236c2bfd1314b03e6bade0c09ab038f4c8756bb456baade141eccd053dfc','dumclr'),('7359e77ed6fdce0a832ee2d1fa2242c529a8f93c2f91f3543a','Dummy8','Dummy8','Dummy8','09888888888','dum8@dum.com','8eeecc0ab208628de9cf91e258e4ac35f96da3e6a5d63d75be688f0c332aa671','dum8'),('abee67ffdf42a450ea498fe50480f0af0edcc410ba17b36d4a','Dummy9','Dummy9','Dummy9','09999999999','dum9@dummail.com','780cfce876ae819f69cc66bb944274bb6e55da89745e0a789c117a5c2bb422e0','dum9');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-30 17:40:07
