-- This command lists all records from the table second_table 
-- where the name is not NULL. The results display the score and name,
-- ordered by score in descending order.
SELECT `score`, `name` FROM `second_table` WHERE `name` IS NOT NULL ORDER BY `score` DESC;
