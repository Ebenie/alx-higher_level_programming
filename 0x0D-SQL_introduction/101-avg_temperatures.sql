-- This command calculates the average temperature by city from the
-- temperatures table and orders the results by temperature in 
-- descending order

USE `hbtn_0c_0`
SELECT `city`, AVG(`value`) AS `avg_temp` FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;

