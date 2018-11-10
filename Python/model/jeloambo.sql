SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

CREATE DATABASE `jeloambo`;
USE `jeloambo`;

CREATE TABLE `j_units` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `type` int(2) NOT NULL,
  `port` varchar(20) NOT NULL,
  `measure_freq` int(11) NOT NULL,
  `sensitivity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `j_values` (
  `value_id` int(11) NOT NULL,
  `value` int(11) NOT NULL,
  `datetime` datetime NOT NULL,
  `unit_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE `j_units`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `j_values`
  ADD PRIMARY KEY (`value_id`);

ALTER TABLE `j_units`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=0;

ALTER TABLE `j_values`
  MODIFY `values_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=0;  

ALTER TABLE `j_values`
  ADD CONSTRAINT `values_unit_FK` FOREIGN KEY (`unit_id`) REFERENCES `j_units` (`id`) ON DELETE CASCADE;
COMMIT;
