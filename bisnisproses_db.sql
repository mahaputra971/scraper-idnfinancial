-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 18, 2024 at 02:36 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bisnisproses_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `tb_announcements`
--

CREATE TABLE `tb_announcements` (
  `id` int(11) NOT NULL,
  `kode_emiten` int(11) DEFAULT NULL,
  `announcement` text DEFAULT NULL,
  `date` date DEFAULT NULL,
  `source` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tb_emiten`
--

CREATE TABLE `tb_emiten` (
  `id` int(11) NOT NULL,
  `nama_perusahaan` varchar(255) DEFAULT NULL,
  `kode_emiten` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tb_ipo`
--

CREATE TABLE `tb_ipo` (
  `id` int(11) NOT NULL,
  `kode_emiten` int(11) DEFAULT NULL,
  `ipo_date` date DEFAULT NULL,
  `Offering_Shares` int(11) DEFAULT NULL,
  `Founders_Shares` int(11) DEFAULT NULL,
  `Total_Listed_Shares` int(11) DEFAULT NULL,
  `Percentage` decimal(5,2) DEFAULT NULL,
  `Offering_Price` decimal(18,2) DEFAULT NULL,
  `Fund_Raised` decimal(18,2) DEFAULT NULL,
  `Securities_Administration_Bureau` varchar(255) DEFAULT NULL,
  `Lead_Underwriter` varchar(255) DEFAULT NULL,
  `Listing_Board` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tb_managements`
--

CREATE TABLE `tb_managements` (
  `id` int(11) NOT NULL,
  `kode_emiten` int(11) DEFAULT NULL,
  `Nama` varchar(100) DEFAULT NULL,
  `Jabatan` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tb_market_activity_temp`
--

CREATE TABLE `tb_market_activity_temp` (
  `id` int(11) NOT NULL,
  `kode_emiten` int(11) DEFAULT NULL,
  `Open` decimal(18,2) DEFAULT NULL,
  `Offer` decimal(18,2) DEFAULT NULL,
  `Previous_Close` decimal(18,2) DEFAULT NULL,
  `Day_Low` decimal(18,2) DEFAULT NULL,
  `Day_High` decimal(18,2) DEFAULT NULL,
  `Volume` int(11) DEFAULT NULL,
  `Value` decimal(18,2) DEFAULT NULL,
  `Frequency` int(11) DEFAULT NULL,
  `Market_Cap_Rank_in_Industry` int(11) DEFAULT NULL,
  `Market_Cap_Rank_in_All_Companies` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tb_net_foreign`
--

CREATE TABLE `tb_net_foreign` (
  `id` int(11) NOT NULL,
  `kode_emiten` int(11) DEFAULT NULL,
  `shares_volume` int(11) DEFAULT NULL,
  `tanggal` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tb_news`
--

CREATE TABLE `tb_news` (
  `id` int(11) NOT NULL,
  `kode_emiten` int(11) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tb_overview`
--

CREATE TABLE `tb_overview` (
  `id` int(11) NOT NULL,
  `kode_emiten` int(11) DEFAULT NULL,
  `decs` text DEFAULT NULL,
  `Address` varchar(255) DEFAULT NULL,
  `Phone_or_fax` varchar(20) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `website` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tb_shareholders`
--

CREATE TABLE `tb_shareholders` (
  `id` int(11) NOT NULL,
  `kode_emiten` int(11) DEFAULT NULL,
  `Shareholder_name` varchar(255) DEFAULT NULL,
  `number_of_shares` int(11) DEFAULT NULL,
  `paid_up_capital` decimal(18,2) DEFAULT NULL,
  `Percentage` decimal(5,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tb_stock_emiten`
--

CREATE TABLE `tb_stock_emiten` (
  `Id` int(11) NOT NULL,
  `kode_emiten` int(11) DEFAULT NULL,
  `harga_saham` decimal(18,2) DEFAULT NULL,
  `tanggal` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tb_subsidiary_affiliation`
--

CREATE TABLE `tb_subsidiary_affiliation` (
  `id` int(11) NOT NULL,
  `kode_emiten` int(11) DEFAULT NULL,
  `company_name` varchar(255) DEFAULT NULL,
  `Percentage` decimal(5,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tb_announcements`
--
ALTER TABLE `tb_announcements`
  ADD PRIMARY KEY (`id`),
  ADD KEY `kode_emiten` (`kode_emiten`);

--
-- Indexes for table `tb_emiten`
--
ALTER TABLE `tb_emiten`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tb_ipo`
--
ALTER TABLE `tb_ipo`
  ADD PRIMARY KEY (`id`),
  ADD KEY `kode_emiten` (`kode_emiten`);

--
-- Indexes for table `tb_managements`
--
ALTER TABLE `tb_managements`
  ADD PRIMARY KEY (`id`),
  ADD KEY `kode_emiten` (`kode_emiten`);

--
-- Indexes for table `tb_market_activity_temp`
--
ALTER TABLE `tb_market_activity_temp`
  ADD PRIMARY KEY (`id`),
  ADD KEY `kode_emiten` (`kode_emiten`);

--
-- Indexes for table `tb_net_foreign`
--
ALTER TABLE `tb_net_foreign`
  ADD PRIMARY KEY (`id`),
  ADD KEY `kode_emiten` (`kode_emiten`);

--
-- Indexes for table `tb_news`
--
ALTER TABLE `tb_news`
  ADD PRIMARY KEY (`id`),
  ADD KEY `kode_emiten` (`kode_emiten`);

--
-- Indexes for table `tb_overview`
--
ALTER TABLE `tb_overview`
  ADD PRIMARY KEY (`id`),
  ADD KEY `kode_emiten` (`kode_emiten`);

--
-- Indexes for table `tb_shareholders`
--
ALTER TABLE `tb_shareholders`
  ADD PRIMARY KEY (`id`),
  ADD KEY `kode_emiten` (`kode_emiten`);

--
-- Indexes for table `tb_stock_emiten`
--
ALTER TABLE `tb_stock_emiten`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `kode_emiten` (`kode_emiten`);

--
-- Indexes for table `tb_subsidiary_affiliation`
--
ALTER TABLE `tb_subsidiary_affiliation`
  ADD PRIMARY KEY (`id`),
  ADD KEY `kode_emiten` (`kode_emiten`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tb_announcements`
--
ALTER TABLE `tb_announcements`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tb_emiten`
--
ALTER TABLE `tb_emiten`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tb_ipo`
--
ALTER TABLE `tb_ipo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tb_managements`
--
ALTER TABLE `tb_managements`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tb_market_activity_temp`
--
ALTER TABLE `tb_market_activity_temp`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tb_net_foreign`
--
ALTER TABLE `tb_net_foreign`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tb_news`
--
ALTER TABLE `tb_news`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tb_overview`
--
ALTER TABLE `tb_overview`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tb_shareholders`
--
ALTER TABLE `tb_shareholders`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tb_stock_emiten`
--
ALTER TABLE `tb_stock_emiten`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tb_subsidiary_affiliation`
--
ALTER TABLE `tb_subsidiary_affiliation`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `tb_announcements`
--
ALTER TABLE `tb_announcements`
  ADD CONSTRAINT `tb_announcements_ibfk_1` FOREIGN KEY (`kode_emiten`) REFERENCES `tb_emiten` (`id`);

--
-- Constraints for table `tb_ipo`
--
ALTER TABLE `tb_ipo`
  ADD CONSTRAINT `tb_ipo_ibfk_1` FOREIGN KEY (`kode_emiten`) REFERENCES `tb_emiten` (`id`);

--
-- Constraints for table `tb_managements`
--
ALTER TABLE `tb_managements`
  ADD CONSTRAINT `tb_managements_ibfk_1` FOREIGN KEY (`kode_emiten`) REFERENCES `tb_emiten` (`id`);

--
-- Constraints for table `tb_market_activity_temp`
--
ALTER TABLE `tb_market_activity_temp`
  ADD CONSTRAINT `tb_market_activity_temp_ibfk_1` FOREIGN KEY (`kode_emiten`) REFERENCES `tb_emiten` (`id`);

--
-- Constraints for table `tb_net_foreign`
--
ALTER TABLE `tb_net_foreign`
  ADD CONSTRAINT `tb_net_foreign_ibfk_1` FOREIGN KEY (`kode_emiten`) REFERENCES `tb_emiten` (`id`);

--
-- Constraints for table `tb_news`
--
ALTER TABLE `tb_news`
  ADD CONSTRAINT `tb_news_ibfk_1` FOREIGN KEY (`kode_emiten`) REFERENCES `tb_emiten` (`id`);

--
-- Constraints for table `tb_overview`
--
ALTER TABLE `tb_overview`
  ADD CONSTRAINT `tb_overview_ibfk_1` FOREIGN KEY (`kode_emiten`) REFERENCES `tb_emiten` (`id`);

--
-- Constraints for table `tb_shareholders`
--
ALTER TABLE `tb_shareholders`
  ADD CONSTRAINT `tb_shareholders_ibfk_1` FOREIGN KEY (`kode_emiten`) REFERENCES `tb_emiten` (`id`);

--
-- Constraints for table `tb_stock_emiten`
--
ALTER TABLE `tb_stock_emiten`
  ADD CONSTRAINT `tb_stock_emiten_ibfk_1` FOREIGN KEY (`kode_emiten`) REFERENCES `tb_emiten` (`id`);

--
-- Constraints for table `tb_subsidiary_affiliation`
--
ALTER TABLE `tb_subsidiary_affiliation`
  ADD CONSTRAINT `tb_subsidiary_affiliation_ibfk_1` FOREIGN KEY (`kode_emiten`) REFERENCES `tb_emiten` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
