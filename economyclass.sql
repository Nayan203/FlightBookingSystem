-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Apr 07, 2021 at 07:44 AM
-- Server version: 5.7.19
-- PHP Version: 5.6.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `flightbookingsystem`
--

-- --------------------------------------------------------

--
-- Table structure for table `economyclass`
--

DROP TABLE IF EXISTS `economyclass`;
CREATE TABLE IF NOT EXISTS `economyclass` (
  `Sno` int(5) NOT NULL,
  `SeatNo` varchar(5) NOT NULL,
  `Category` text NOT NULL,
  `Status` text NOT NULL,
  `BookingID` int(30) DEFAULT NULL,
  `PName` text NOT NULL,
  `PEmail` varchar(40) NOT NULL,
  UNIQUE KEY `BookingID` (`BookingID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `economyclass`
--

INSERT INTO `economyclass` (`Sno`, `SeatNo`, `Category`, `Status`, `BookingID`, `PName`, `PEmail`) VALUES
(1, 'E1', 'Window', 'Unreserved', NULL, '', ''),
(2, 'E2', 'Middle', 'Unreserved', NULL, '', ''),
(3, 'E3', 'Aisle', 'Unreserved', NULL, '', ''),
(4, 'E4', 'Aisle', 'Unreserved', NULL, '', ''),
(5, 'E5', 'Middle', 'Unreserved', NULL, '', ''),
(6, 'E6', 'Window', 'Unreserved', NULL, '', ''),
(7, 'E7', 'Window', 'Unreserved', NULL, '', ''),
(8, 'E8', 'Middle', 'Unreserved', NULL, '', ''),
(9, 'E9', 'Aisle', 'Unreserved', NULL, '', ''),
(10, 'E10', 'Aisle', 'Unreserved', NULL, '', ''),
(11, 'E11', 'Middle', 'Unreserved', NULL, '', ''),
(12, 'E12', 'Window', 'Unreserved', NULL, '', ''),
(13, 'E13', 'Window', 'Unreserved', NULL, '', ''),
(14, 'E14', 'Middle', 'Unreserved', NULL, '', ''),
(15, 'E15', 'Aisle', 'Unreserved', NULL, '', ''),
(16, 'E16', 'Aisle', 'Unreserved', NULL, '', ''),
(17, 'E17', 'Middle', 'Unreserved', NULL, '', ''),
(18, 'E18', 'Window', 'Unreserved', NULL, '', '');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
