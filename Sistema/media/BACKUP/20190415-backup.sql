-- MySQL dump 10.13  Distrib 5.7.25, for Linux (x86_64)
--
-- Host: localhost    Database: FarmaciaDA
-- ------------------------------------------------------
-- Server version	5.7.25-0ubuntu0.18.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Farmacia_categoria`
--

DROP TABLE IF EXISTS `Farmacia_categoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Farmacia_categoria` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_categoria` varchar(100) NOT NULL,
  `descripcion` longtext NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre_categoria` (`nombre_categoria`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Farmacia_categoria`
--

LOCK TABLES `Farmacia_categoria` WRITE;
/*!40000 ALTER TABLE `Farmacia_categoria` DISABLE KEYS */;
INSERT INTO `Farmacia_categoria` VALUES (1,'Medicamento','N/H');
/*!40000 ALTER TABLE `Farmacia_categoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Farmacia_cliente`
--

DROP TABLE IF EXISTS `Farmacia_cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Farmacia_cliente` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cedula` varchar(13) NOT NULL,
  `nombres` varchar(100) NOT NULL,
  `apellidos` varchar(100) NOT NULL,
  `direccion` varchar(200) NOT NULL,
  `telefono` varchar(10) NOT NULL,
  `email` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cedula` (`cedula`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Farmacia_cliente`
--

LOCK TABLES `Farmacia_cliente` WRITE;
/*!40000 ALTER TABLE `Farmacia_cliente` DISABLE KEYS */;
/*!40000 ALTER TABLE `Farmacia_cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Farmacia_compra`
--

DROP TABLE IF EXISTS `Farmacia_compra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Farmacia_compra` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `comprobante` varchar(100) DEFAULT NULL,
  `proveedor_id` int(11) NOT NULL,
  `descripcion` varchar(200) NOT NULL,
  `estadopago` varchar(10) NOT NULL,
  `formapago` varchar(7) NOT NULL,
  `numCompra` varchar(10) NOT NULL,
  `numFactura` varchar(20) NOT NULL,
  `plazopago` int(11) NOT NULL,
  `totalcompra` decimal(6,2) NOT NULL,
  `fechacompra` date NOT NULL,
  `fechalimite` date NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Farmacia_compra_numCompra_d569d6c7_uniq` (`numCompra`),
  KEY `Farmacia_compra_proveedor_id_e05376d2_fk_Farmacia_proveedor_id` (`proveedor_id`),
  CONSTRAINT `Farmacia_compra_proveedor_id_e05376d2_fk_Farmacia_proveedor_id` FOREIGN KEY (`proveedor_id`) REFERENCES `Farmacia_proveedor` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Farmacia_compra`
--

LOCK TABLES `Farmacia_compra` WRITE;
/*!40000 ALTER TABLE `Farmacia_compra` DISABLE KEYS */;
INSERT INTO `Farmacia_compra` VALUES (1,'Comprobantes/c06d2272-f9ff-495a-97e7-bd41fff60f9e.jpeg',1,'Por compra de medicamentos','PAGADO','CONTADO','0000000001','001005000022918',0,200.00,'2019-04-12','2019-04-12');
/*!40000 ALTER TABLE `Farmacia_compra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Farmacia_detallefactura`
--

DROP TABLE IF EXISTS `Farmacia_detallefactura`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Farmacia_detallefactura` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cantidad` int(11) NOT NULL,
  `concepto` varchar(100) NOT NULL,
  `valorUnitario` decimal(6,2) NOT NULL,
  `valorTotal` decimal(6,2) NOT NULL,
  `producto_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Farmacia_detallefact_producto_id_638c4139_fk_Farmacia_` (`producto_id`),
  CONSTRAINT `Farmacia_detallefact_producto_id_638c4139_fk_Farmacia_` FOREIGN KEY (`producto_id`) REFERENCES `Farmacia_producto` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Farmacia_detallefactura`
--

LOCK TABLES `Farmacia_detallefactura` WRITE;
/*!40000 ALTER TABLE `Farmacia_detallefactura` DISABLE KEYS */;
/*!40000 ALTER TABLE `Farmacia_detallefactura` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Farmacia_empresa`
--

DROP TABLE IF EXISTS `Farmacia_empresa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Farmacia_empresa` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_empresa` varchar(50) NOT NULL,
  `ruc` varchar(13) NOT NULL,
  `direccion` varchar(200) NOT NULL,
  `telefono` varchar(10) NOT NULL,
  `email` varchar(100) NOT NULL,
  `logo` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Farmacia_empresa`
--

LOCK TABLES `Farmacia_empresa` WRITE;
/*!40000 ALTER TABLE `Farmacia_empresa` DISABLE KEYS */;
/*!40000 ALTER TABLE `Farmacia_empresa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Farmacia_factura`
--

DROP TABLE IF EXISTS `Farmacia_factura`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Farmacia_factura` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `serie` int(11) NOT NULL,
  `numero` varchar(7) NOT NULL,
  `tipoPago` varchar(50) NOT NULL,
  `pagado` tinyint(1) NOT NULL,
  `fecha` datetime(6) NOT NULL,
  `subtotal` decimal(6,2) NOT NULL,
  `descuento` decimal(6,2) NOT NULL,
  `iva0` decimal(6,2) NOT NULL,
  `iva12` decimal(6,2) NOT NULL,
  `valorTotal` decimal(6,2) NOT NULL,
  `cliente_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `numero` (`numero`),
  UNIQUE KEY `Farmacia_factura_serie_numero_5806a46a_uniq` (`serie`,`numero`),
  KEY `Farmacia_factura_cliente_id_34cabd8b_fk_Farmacia_cliente_id` (`cliente_id`),
  CONSTRAINT `Farmacia_factura_cliente_id_34cabd8b_fk_Farmacia_cliente_id` FOREIGN KEY (`cliente_id`) REFERENCES `Farmacia_cliente` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Farmacia_factura`
--

LOCK TABLES `Farmacia_factura` WRITE;
/*!40000 ALTER TABLE `Farmacia_factura` DISABLE KEYS */;
/*!40000 ALTER TABLE `Farmacia_factura` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Farmacia_factura_detalleFactura`
--

DROP TABLE IF EXISTS `Farmacia_factura_detalleFactura`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Farmacia_factura_detalleFactura` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `factura_id` int(11) NOT NULL,
  `detallefactura_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Farmacia_factura_detalle_factura_id_detallefactur_f13fba0c_uniq` (`factura_id`,`detallefactura_id`),
  KEY `Farmacia_factura_det_detallefactura_id_a4802153_fk_Farmacia_` (`detallefactura_id`),
  CONSTRAINT `Farmacia_factura_det_detallefactura_id_a4802153_fk_Farmacia_` FOREIGN KEY (`detallefactura_id`) REFERENCES `Farmacia_detallefactura` (`id`),
  CONSTRAINT `Farmacia_factura_det_factura_id_752324bc_fk_Farmacia_` FOREIGN KEY (`factura_id`) REFERENCES `Farmacia_factura` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Farmacia_factura_detalleFactura`
--

LOCK TABLES `Farmacia_factura_detalleFactura` WRITE;
/*!40000 ALTER TABLE `Farmacia_factura_detalleFactura` DISABLE KEYS */;
/*!40000 ALTER TABLE `Farmacia_factura_detalleFactura` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Farmacia_pago`
--

DROP TABLE IF EXISTS `Farmacia_pago`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Farmacia_pago` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `valorPago` decimal(6,2) NOT NULL,
  `fechaPago` date NOT NULL,
  `compra_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Farmacia_pago_compra_id_b8d01be6_fk_Farmacia_compra_id` (`compra_id`),
  CONSTRAINT `Farmacia_pago_compra_id_b8d01be6_fk_Farmacia_compra_id` FOREIGN KEY (`compra_id`) REFERENCES `Farmacia_compra` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Farmacia_pago`
--

LOCK TABLES `Farmacia_pago` WRITE;
/*!40000 ALTER TABLE `Farmacia_pago` DISABLE KEYS */;
INSERT INTO `Farmacia_pago` VALUES (1,0.00,'2019-04-12',1);
/*!40000 ALTER TABLE `Farmacia_pago` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Farmacia_presentacion`
--

DROP TABLE IF EXISTS `Farmacia_presentacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Farmacia_presentacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_presentacion` varchar(60) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Farmacia_presentacion_nombre_presentacion_5466f46c_uniq` (`nombre_presentacion`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Farmacia_presentacion`
--

LOCK TABLES `Farmacia_presentacion` WRITE;
/*!40000 ALTER TABLE `Farmacia_presentacion` DISABLE KEYS */;
INSERT INTO `Farmacia_presentacion` VALUES (1,'TABLETAS  1 MG X 100');
/*!40000 ALTER TABLE `Farmacia_presentacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Farmacia_producto`
--

DROP TABLE IF EXISTS `Farmacia_producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Farmacia_producto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `codigo_producto` varchar(10) NOT NULL,
  `nombre_producto` varchar(100) NOT NULL,
  `nombre_generico` varchar(100) NOT NULL,
  `casa_comercial_id` int(11) NOT NULL,
  `fecha_expiracion` date NOT NULL,
  `fecha_elaboracion` date NOT NULL,
  `detalle_producto` longtext NOT NULL,
  `stock` int(11) NOT NULL,
  `valor_Compra` decimal(5,2) NOT NULL,
  `precio_producto` decimal(10,2) NOT NULL,
  `valor_venta_cajas` decimal(5,2) NOT NULL,
  `descuento` decimal(6,2) NOT NULL,
  `categoria_id` int(11) NOT NULL,
  `presentacion_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `codigo_producto` (`codigo_producto`),
  KEY `Farmacia_producto_categoria_id_27333751_fk_Farmacia_categoria_id` (`categoria_id`),
  KEY `Farmacia_producto_presentacion_id_6911933d_fk_Farmacia_` (`presentacion_id`),
  KEY `Farmacia_producto_casa_comercial_id_069f4720` (`casa_comercial_id`),
  CONSTRAINT `Farmacia_producto_casa_comercial_id_069f4720_fk_Farmacia_` FOREIGN KEY (`casa_comercial_id`) REFERENCES `Farmacia_proveedor` (`id`),
  CONSTRAINT `Farmacia_producto_categoria_id_27333751_fk_Farmacia_categoria_id` FOREIGN KEY (`categoria_id`) REFERENCES `Farmacia_categoria` (`id`),
  CONSTRAINT `Farmacia_producto_presentacion_id_6911933d_fk_Farmacia_` FOREIGN KEY (`presentacion_id`) REFERENCES `Farmacia_presentacion` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Farmacia_producto`
--

LOCK TABLES `Farmacia_producto` WRITE;
/*!40000 ALTER TABLE `Farmacia_producto` DISABLE KEYS */;
INSERT INTO `Farmacia_producto` VALUES (1,'0000000001','Enalpril','Enalapril',1,'2019-01-14','2017-06-01','N/H',10,0.15,0.15,3.00,2.80,1,1);
/*!40000 ALTER TABLE `Farmacia_producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Farmacia_proveedor`
--

DROP TABLE IF EXISTS `Farmacia_proveedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Farmacia_proveedor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ruc` varchar(13) NOT NULL,
  `distribuidora` varchar(50) NOT NULL,
  `empresa` varchar(100) NOT NULL,
  `nombre_responsable` varchar(100) NOT NULL,
  `direccion` varchar(100) NOT NULL,
  `telefono_empresa` varchar(10) NOT NULL,
  `telefono_responsable` varchar(10) NOT NULL,
  `email` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ruc` (`ruc`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Farmacia_proveedor`
--

LOCK TABLES `Farmacia_proveedor` WRITE;
/*!40000 ALTER TABLE `Farmacia_proveedor` DISABLE KEYS */;
INSERT INTO `Farmacia_proveedor` VALUES (1,'1190076608001','LOJAFARM','Quimica Ariston','Leon Moreta','Lauro Guerrero y Colon','2110901','0938190389','kyuhyun1998@outlook.com');
/*!40000 ALTER TABLE `Farmacia_proveedor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add permission',3,'add_permission'),(8,'Can change permission',3,'change_permission'),(9,'Can delete permission',3,'delete_permission'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add detalle factura',7,'add_detallefactura'),(20,'Can change detalle factura',7,'change_detallefactura'),(21,'Can delete detalle factura',7,'delete_detallefactura'),(22,'Can add compra',8,'add_compra'),(23,'Can change compra',8,'change_compra'),(24,'Can delete compra',8,'delete_compra'),(25,'Can add factura',9,'add_factura'),(26,'Can change factura',9,'change_factura'),(27,'Can delete factura',9,'delete_factura'),(28,'Can add categoria',10,'add_categoria'),(29,'Can change categoria',10,'change_categoria'),(30,'Can delete categoria',10,'delete_categoria'),(31,'Can add cliente',11,'add_cliente'),(32,'Can change cliente',11,'change_cliente'),(33,'Can delete cliente',11,'delete_cliente'),(34,'Can add proveedor',12,'add_proveedor'),(35,'Can change proveedor',12,'change_proveedor'),(36,'Can delete proveedor',12,'delete_proveedor'),(37,'Can add empresa',13,'add_empresa'),(38,'Can change empresa',13,'change_empresa'),(39,'Can delete empresa',13,'delete_empresa'),(40,'Can add pago',14,'add_pago'),(41,'Can change pago',14,'change_pago'),(42,'Can delete pago',14,'delete_pago'),(43,'Can add producto',15,'add_producto'),(44,'Can change producto',15,'change_producto'),(45,'Can delete producto',15,'delete_producto'),(46,'Can add presentacion',16,'add_presentacion'),(47,'Can change presentacion',16,'change_presentacion'),(48,'Can delete presentacion',16,'delete_presentacion');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$36000$MIJsoyTwxa5m$OJib52XiR/RVl0paz0MbWwVWloANnyRo5vaQfKGN2PU=','2019-04-12 17:29:09.625203',1,'admin','','','mayurita5@gmail.com',1,1,'2019-04-12 16:38:35.126126');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(2,'auth','group'),(3,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(10,'Farmacia','categoria'),(11,'Farmacia','cliente'),(8,'Farmacia','compra'),(7,'Farmacia','detallefactura'),(13,'Farmacia','empresa'),(9,'Farmacia','factura'),(14,'Farmacia','pago'),(16,'Farmacia','presentacion'),(15,'Farmacia','producto'),(12,'Farmacia','proveedor'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'Farmacia','0001_initial','2019-04-12 16:34:09.704922'),(2,'Farmacia','0002_proveedor','2019-04-12 16:34:10.164528'),(3,'Farmacia','0003_categoria_presentacion_producto','2019-04-12 16:34:13.191948'),(4,'Farmacia','0004_auto_20190220_1330','2019-04-12 16:34:19.390484'),(5,'Farmacia','0005_auto_20190220_1333','2019-04-12 16:34:19.975740'),(6,'Farmacia','0006_auto_20190226_1258','2019-04-12 16:34:25.407232'),(7,'Farmacia','0007_auto_20190305_1939','2019-04-12 16:34:25.787857'),(8,'Farmacia','0008_auto_20190306_1415','2019-04-12 16:34:25.935554'),(9,'Farmacia','0009_remove_proveedor_activa','2019-04-12 16:34:26.595507'),(10,'Farmacia','0010_auto_20190325_1145','2019-04-12 16:34:29.270219'),(11,'Farmacia','0011_auto_20190412_1134','2019-04-12 16:34:42.152560'),(12,'contenttypes','0001_initial','2019-04-12 16:34:43.160490'),(13,'auth','0001_initial','2019-04-12 16:34:56.560835'),(14,'admin','0001_initial','2019-04-12 16:35:01.030025'),(15,'admin','0002_logentry_remove_auto_add','2019-04-12 16:35:01.323293'),(16,'contenttypes','0002_remove_content_type_name','2019-04-12 16:35:04.598906'),(17,'auth','0002_alter_permission_name_max_length','2019-04-12 16:35:04.746450'),(18,'auth','0003_alter_user_email_max_length','2019-04-12 16:35:04.935916'),(19,'auth','0004_alter_user_username_opts','2019-04-12 16:35:05.047868'),(20,'auth','0005_alter_user_last_login_null','2019-04-12 16:35:05.582937'),(21,'auth','0006_require_contenttypes_0002','2019-04-12 16:35:05.776415'),(22,'auth','0007_alter_validators_add_error_messages','2019-04-12 16:35:05.850864'),(23,'auth','0008_alter_user_username_max_length','2019-04-12 16:35:06.055860'),(24,'sessions','0001_initial','2019-04-12 16:35:06.834033'),(25,'Farmacia','0012_auto_20190412_1140','2019-04-12 16:40:47.989888'),(26,'Farmacia','0013_auto_20190412_1145','2019-04-12 16:45:11.320126'),(27,'Farmacia','0014_auto_20190412_1150','2019-04-12 16:50:24.157392');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('p84o4sjx21b06mk1d5ivciedd0yb7mdb','MjQ5MmQwMmY0ZjNiNzNiYTg3NGY5MTY3NzA3NTZiOGFmOTQ2NTc4YTp7Il9hdXRoX3VzZXJfaGFzaCI6IjFlMjUzZDczM2E0MTlmM2E2MmQ5ZjMxOGE4MzBlY2Q5NmMzZGIyOGIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2019-04-26 17:29:09.714633');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-04-12 13:04:09
