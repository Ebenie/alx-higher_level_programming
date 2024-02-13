-- SQL query selects the score and name columns
-- from the second_table table where 
-- the score is greater than or equal to 10, 
-- and then orders the results in descending order 
-- based on the score column.
SELECT `score`, `name` FROM `second_table` WHERE `score` >= 10
 ORDER BY `score` DESC;
