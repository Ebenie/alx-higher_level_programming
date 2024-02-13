-- This command uses argument as database name 
-- This command creates a table 'first_table'
-- If the table exist won't fail
USE mysql;
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
