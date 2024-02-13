-- This command lists the number of records with the same score
-- in the table second_table. The results are grouped by score
--  and ordered by the number of records in descending order.
SELECT `score`, COUNT(*) AS `number` FROM `second_table` GROUP BY `score` ORDER BY `number` DESC;
