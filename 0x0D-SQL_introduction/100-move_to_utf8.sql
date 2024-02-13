-- This command converts the character encoding of the database
--  hbtn_0c_0, the table first_table, and the field name to UTF-8 
-- (utf8mb4) with the collation utf8mb4_unicode_ci.
ALTER DATABASE `hbtn_0c_0` CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

ALTER TABLE `first_table` CONVERT TO CHARACTER SET
 utf8mb4 COLLATE utf8mb4_unicode_ci;
 
ALTER TABLE `first_table` MODIFY COLUMN `name` VARCHAR(256) 
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
