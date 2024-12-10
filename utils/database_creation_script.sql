CREATE DATABASE `bank_database`;

use bank_database;

CREATE TABLE `bank_details` (
  `account_number` int NOT NULL,
  `balance` decimal(10,2) NOT NULL,
  `last_transaction` varchar(50) DEFAULT NULL,
  `last_transacted_date` varchar(100) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`account_number`)
);

CREATE TABLE `transaction_history` (
  `account_number` int DEFAULT NULL,
  `transaction_type` varchar(20) DEFAULT NULL,
  `amount` decimal(10,2) DEFAULT NULL,
  `transaction_date` date DEFAULT NULL,
  KEY `Account_Number` (`account_number`),
  CONSTRAINT `transaction_history_ibfk_1` FOREIGN KEY (`account_number`) REFERENCES `bank_details` (`account_number`)
) ;

CREATE TABLE `user_details` (
  `account_number` int NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `age` int DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `number` int DEFAULT NULL,
  PRIMARY KEY (`account_number`)
);

