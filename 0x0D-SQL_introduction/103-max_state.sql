-- This command lists the maximum temperature of each state from 
-- the temperatures table, ordered by state name.

SELECT `state`, MAX(`value`) AS `max_temp` FROM `temperatures`
GROUP BY `state`
ORDER BY `state`;

