-- This command converts the character encoding of the
-- table 'first_table'.
USE `hbtn_0c_0`
ALTER TABLE `first_table` CONVERT TO CHARACTER SET
 utf8mb4 COLLATE utf8mb4_unicode_ci;
 
-- This command converts the character encoding of the
-- the field 'name' to UTF-8 
-- (utf8mb4) with the collation utf8mb4_unicode_ci
ALTER TABLE `first_table` MODIFY COLUMN `name` VARCHAR(256) 
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

