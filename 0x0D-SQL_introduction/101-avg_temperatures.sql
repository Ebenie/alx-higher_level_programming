-- This command calculates the average temperature by city from the
-- temperatures table and orders the results by temperature in 
-- descending order

USE `hbtn_0c_0`;
source temperatures.sql;

SELECT `city`, AVG(`value`) AS `average_temp` FROM `temperatures`
GROUP BY `city`
ORDER BY `average_temp` DESC;

