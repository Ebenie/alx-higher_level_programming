-- This display the full description of the table first_table
-- The database name will be passed as an argument so ?
USE information_schema;

SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_KEY, COLUMN_DEFAULT, EXTRA
FROM COLUMNS
WHERE TABLE_SCHEMA = ?
AND TABLE_NAME = 'first_table';
