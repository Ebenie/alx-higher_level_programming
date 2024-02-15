-- This command converts the character encoding of the database
--  hbtn_0c_0, the table first_table, and the field name to UTF-8 
-- (utf8mb4) with the collation utf8mb4_unicode_ci.

USE`hbtn_0c_0` 
ALTER TABLE `first_table` CONVERT TO CHARACTER SET
 utf8mb4 COLLATE utf8mb4_unicode_ci;

