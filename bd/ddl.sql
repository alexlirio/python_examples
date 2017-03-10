CREATE DATABASE IF NOT EXISTS `bd_python_examples`;
USE `bd_python_examples`;

CREATE TABLE IF NOT EXISTS `company` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `mail` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
);

INSERT INTO `company` (`id`, `name`, `mail`) VALUES
	(1, 'Company 1', 'contact@company1.com'),
	(2, 'Company 2', 'contact@company2.com');
