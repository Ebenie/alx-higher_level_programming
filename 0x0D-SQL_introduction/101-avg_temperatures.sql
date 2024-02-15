-- This command calculates the average temperature by city from the
-- temperatures table and orders the results by temperature in 
-- descending order

SELECT `city`, AVG(`value`) AS `average_temp` FROM `temperatures`
GROUP BY `city`
ORDER BY `average_temp` DESC;

