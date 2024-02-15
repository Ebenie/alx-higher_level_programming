-- This command displays the top 3 cities with the highest average
-- temperature during July and August from the temperatures table, 
-- ordered by temperature in descending order

SELECT `city`, AVG(`value`) AS `avg_temp` FROM `temperatures`
WHERE month IN ('July', 'August')
GROUP BY `city`
ORDER BY `avg_temp` DESC
LIMIT 3;

