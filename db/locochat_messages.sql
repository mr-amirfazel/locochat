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
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `messages` (
  `message_ID` varchar(30) NOT NULL,
  `sender_token` varchar(200) DEFAULT NULL,
  `receiver_token` varchar(200) DEFAULT NULL,
  `sender_user_ID` varchar(25) DEFAULT NULL,
  `receiver_user_ID` varchar(25) DEFAULT NULL,
  `message_content` varchar(500) DEFAULT NULL,
  `message_time` timestamp NULL DEFAULT NULL,
  `seen` tinyint DEFAULT '0',
  PRIMARY KEY (`message_ID`),
  KEY `sender_token_idx` (`sender_token`),
  KEY `sender_ID_idx` (`sender_user_ID`),
  KEY `receiver_ID_idx` (`receiver_user_ID`),
  CONSTRAINT `receiver_user_ID` FOREIGN KEY (`receiver_user_ID`) REFERENCES `users` (`userID`) ON DELETE SET NULL,
  CONSTRAINT `sender_user_ID` FOREIGN KEY (`sender_user_ID`) REFERENCES `users` (`userID`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES ('085eb9b4c8f99975869f','d33445fbd8d5b78d5f1b1ea90f71cb81e612c0f69a30748f66','7359e77ed6fdce0a832ee2d1fa2242c529a8f93c2f91f3543a','amirfazel45','Dummy8','hi','2022-06-30 10:09:59',1),('118a53633a0c4b2c53ff','7359e77ed6fdce0a832ee2d1fa2242c529a8f93c2f91f3543a','d33445fbd8d5b78d5f1b1ea90f71cb81e612c0f69a30748f66','Dummy8','amirfazel45','lets try it on web :)','2022-06-30 07:49:08',1),('166659f9ecf6f1a52fef','b7967f7e600f504f06e72580e985fd6f60a7e235c831447cf1','d33445fbd8d5b78d5f1b1ea90f71cb81e612c0f69a30748f66',NULL,'amirfazel45','hi','2022-06-28 07:10:54',1),('1692cc0e9cf86b085705','d33445fbd8d5b78d5f1b1ea90f71cb81e612c0f69a30748f66','7359e77ed6fdce0a832ee2d1fa2242c529a8f93c2f91f3543a','amirfazel45','Dummy8','hello from web :)','2022-06-30 10:10:10',1),('19b60dc681ef6c17f3f4','bc4f7adb473e723dfe3dc5661b2721f8672f00fcbd4831b734','533aa8e389352d70060d58baa7055c0941447b5eac0be82890',NULL,NULL,'hiiiiiiiiii','2022-06-23 23:21:17',0),('270012836dec183ed657','b7967f7e600f504f06e72580e985fd6f60a7e235c831447cf1','d33445fbd8d5b78d5f1b1ea90f71cb81e612c0f69a30748f66',NULL,'amirfazel45','I am dummy12','2022-06-28 07:14:40',1),('271d079d54479f8ba951','533aa8e389352d70060d58baa7055c0941447b5eac0be82890','d33445fbd8d5b78d5f1b1ea90f71cb81e612c0f69a30748f66',NULL,'amirfazel45','testing and debugging','2022-06-20 17:19:58',1),('34849593ca1216b54f03','533aa8e389352d70060d58baa7055c0941447b5eac0be82890','d33445fbd8d5b78d5f1b1ea90f71cb81e612c0f69a30748f66',NULL,'amirfazel45','imma delete my acc to try this ability wish me luck','2022-06-23 22:42:12',1),('3a7c61f8d8efc9e8265f','533aa8e389352d70060d58baa7055c0941447b5eac0be82890','d33445fbd8d5b78d5f1b1ea90f71cb81e612c0f69a30748f66',NULL,'amirfazel45','a little factorization bro','2022-06-23 05:57:18',1),('42600b4bf40dea68c8a4','d33445fbd8d5b78d5f1b1ea90f71cb81e612c0f69a30748f66','7359e77ed6fdce0a832ee2d1fa2242c529a8f93c2f91f3543a','amirfazel45','Dummy8','arrrrrrrr','2022-06-30 08:19:22',1),('572fae25b1f7f0c1664a','abee67ffdf42a450ea498fe50480f0af0edcc410ba17b36d4a','7359e77ed6fdce0a832ee2d1fa2242c529a8f93c2f91f3543a','Dummy9','Dummy8','what a nice day ','2022-06-30 12:12:29',0),('5fe4c1d9162e189cb27d','533aa8e389352d70060d58baa7055c0941447b5eac0be82890','d33445fbd8d5b78d5f1b1ea90f71cb81e612c0f69a30748f66',NULL,'amirfazel45','yo bro new features added','2022-06-22 12:19:37',1),('6cb5432b7fe7878597f3','7359e77ed6fdce0a832ee2d1fa2242c529a8f93c2f91f3543a','d33445fbd8d5b78d5f1b1ea90f71cb81e612c0f69a30748f66','Dummy8','amirfazel45','hi fazel','2022-06-30 07:48:45',1),('6d97c66c27d2ec6b63d2','533aa8e389352d70060d58baa7055c0941447b5eac0be82890','d33445fbd8d5b78d5f1b1ea90f71cb81e612c0f69a30748f66',NULL,'amirfazel45','hi, fazel hows it going?','2022-06-20 17:04:35',1),('6e08a0cf35e2570ce461','6d23b9ade96b7ffb77a84f296cb6bc679cb58b9b612c8b0196','533aa8e389352d70060d58baa7055c0941447b5eac0be82890',NULL,NULL,'hi','2022-06-23 23:18:54',0),('88c464eeab457b028f73','7359e77ed6fdce0a832ee2d1fa2242c529a8f93c2f91f3543a','abee67ffdf42a450ea498fe50480f0af0edcc410ba17b36d4a','Dummy8','Dummy9','hello from web :)','2022-06-30 12:09:42',1),('acb55db12ddcfa497355','7359e77ed6fdce0a832ee2d1fa2242c529a8f93c2f91f3543a','abee67ffdf42a450ea498fe50480f0af0edcc410ba17b36d4a','Dummy8','Dummy9','hi dummy 9','2022-06-30 12:09:33',1),('b13e4a94e8398d9fa70f','d33445fbd8d5b78d5f1b1ea90f71cb81e612c0f69a30748f66','533aa8e389352d70060d58baa7055c0941447b5eac0be82890','amirfazel45',NULL,'hi dummy 4 , thanks for creating such a cool app','2022-06-20 17:28:25',1),('b16c686432c5a79d3258','533aa8e389352d70060d58baa7055c0941447b5eac0be82890','d33445fbd8d5b78d5f1b1ea90f71cb81e612c0f69a30748f66',NULL,'amirfazel45','yo','2022-06-20 17:24:35',1),('b75af5ba16f3446980c8','abee67ffdf42a450ea498fe50480f0af0edcc410ba17b36d4a','7359e77ed6fdce0a832ee2d1fa2242c529a8f93c2f91f3543a','Dummy9','Dummy8','hi dummy 8','2022-06-30 12:08:43',1),('bab09fd9fced490bdd36','e3422c76dfe5f5b8404d8423154062ff2923b4f4e2d8e79145','7d726315c1822caefe6eafa10257b086dd22bbf54c1d979db6',NULL,'Dummy4','hello, thi is test','2022-06-29 10:31:34',1),('bb3eb9dd56e78721c4a2','d33445fbd8d5b78d5f1b1ea90f71cb81e612c0f69a30748f66','533aa8e389352d70060d58baa7055c0941447b5eac0be82890','amirfazel45',NULL,'yo nice job, I also finished my exams do u need help?','2022-06-22 12:22:07',1),('bd5cf1375600cde1724e','533aa8e389352d70060d58baa7055c0941447b5eac0be82890','d33445fbd8d5b78d5f1b1ea90f71cb81e612c0f69a30748f66',NULL,'amirfazel45','I am dummy 4, testing the send message ability','2022-06-20 17:05:24',1),('c97485abb1e832548493','d33445fbd8d5b78d5f1b1ea90f71cb81e612c0f69a30748f66','533aa8e389352d70060d58baa7055c0941447b5eac0be82890','amirfazel45',NULL,'yo','2022-06-23 22:41:13',1),('c981d052439a4d7a3ee5','d33445fbd8d5b78d5f1b1ea90f71cb81e612c0f69a30748f66','7359e77ed6fdce0a832ee2d1fa2242c529a8f93c2f91f3543a','amirfazel45','Dummy8','salam dummy 8 azizam','2022-06-30 08:19:34',1),('c9e8fd92691d8661d276','d33445fbd8d5b78d5f1b1ea90f71cb81e612c0f69a30748f66','7359e77ed6fdce0a832ee2d1fa2242c529a8f93c2f91f3543a','amirfazel45','Dummy8','dummy6','2022-06-30 11:01:34',1),('eae6c61ba3935b408d86','7359e77ed6fdce0a832ee2d1fa2242c529a8f93c2f91f3543a','d33445fbd8d5b78d5f1b1ea90f71cb81e612c0f69a30748f66','Dummy8','amirfazel45','yo second message','2022-06-30 07:48:54',1);
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
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
