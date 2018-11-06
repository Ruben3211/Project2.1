-- phpMyAdmin SQL Dump
-- version 4.8.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Gegenereerd op: 06 nov 2018 om 10:27
-- Serverversie: 10.1.31-MariaDB
-- PHP-versie: 7.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `jeloambo`
--

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `j_units`
--

CREATE TABLE `j_units` (
  `id` int(11) NOT NULL,
  `name` varchar(32) NOT NULL,
  `type` int(11) NOT NULL,
  `sensitivity` int(11) NOT NULL,
  `measure_freq` int(11) NOT NULL,
  `share_freq` int(11) NOT NULL,
  `datetime_added` datetime NOT NULL,
  `manual` smallint(6) NOT NULL,
  `port` varchar(16) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `j_values`
--

CREATE TABLE `j_values` (
  `value` double NOT NULL,
  `datetime` datetime NOT NULL,
  `unit_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexen voor geëxporteerde tabellen
--

--
-- Indexen voor tabel `j_units`
--
ALTER TABLE `j_units`
  ADD PRIMARY KEY (`id`);

--
-- Indexen voor tabel `j_values`
--
ALTER TABLE `j_values`
  ADD PRIMARY KEY (`unit_id`,`datetime`);

--
-- AUTO_INCREMENT voor geëxporteerde tabellen
--

--
-- AUTO_INCREMENT voor een tabel `j_units`
--
ALTER TABLE `j_units`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- Beperkingen voor geëxporteerde tabellen
--

--
-- Beperkingen voor tabel `j_values`
--
ALTER TABLE `j_values`
  ADD CONSTRAINT `values_unit_FK` FOREIGN KEY (`unit_id`) REFERENCES `j_units` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
