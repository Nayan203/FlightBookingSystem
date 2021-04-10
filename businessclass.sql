-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Apr 09, 2021 at 05:16 AM
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
-- Table structure for table `businessclass`
--

DROP TABLE IF EXISTS `businessclass`;
CREATE TABLE IF NOT EXISTS `businessclass` (
  `Sno` int(5) NOT NULL,
  `SeatNo` varchar(5) NOT NULL,
  `Category` text NOT NULL,
  `Status` text NOT NULL,
  `BookingID` varchar(20) NOT NULL,
  `PName` text NOT NULL,
  `PEmail` text NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `businessclass`
--

INSERT INTO `businessclass` (`Sno`, `SeatNo`, `Category`, `Status`, `BookingID`, `PName`, `PEmail`) VALUES
(1, 'A1', 'Window', 'Unreserved', '', '', ''),
(2, 'B1', 'Aisle', 'Unreserved', '', '', ''),
(3, 'C1', 'Aisle', 'Unreserved', '', '', ''),
(4, 'D1', 'Window', 'Unreserved', '', '', ''),
(5, 'A2', 'Window', 'Unreserved', '', '', ''),
(6, 'B2', 'Aisle', 'Unreserved', '', '', ''),
(7, 'C2', 'Aisle', 'Unreserved', '', '', ''),
(8, 'D2', 'Window', 'Unreserved', '', '', ''),
(9, 'A3', 'Window', 'Unreserved', '', '', ''),
(10, 'B3', 'Aisle', 'Unreserved', '', '', ''),
(11, 'C3', 'Aisle', 'Unreserved', '', '', ''),
(12, 'D3', 'Window', 'Unreserved', '', '', ''),
(13, 'A4', 'Window', 'Unreserved', '', '', ''),
(14, 'B4', 'Aisle', 'Unreserved', '', '', ''),
(15, 'C4', 'Aisle', 'Unreserved', '', '', ''),
(16, 'D4', 'Window', 'Unreserved', '', '', ''),
(17, 'A5', 'Window', 'Unreserved', '', '', ''),
(18, 'B5', 'Aisle', 'Unreserved', '', '', ''),
(19, 'C5', 'Aisle', 'Unreserved', '', '', ''),
(20, 'D5', 'Window', 'Unreserved', '', '', '');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
