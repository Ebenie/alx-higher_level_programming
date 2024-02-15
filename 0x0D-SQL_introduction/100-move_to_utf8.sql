-- This command converts `hbtn_0c_0` database to UTF8 
-- (utf8mb4, collate utf8mb4_unicode_ci) in MySQL server

--  This command uses the database `hbtn_0c_0`
USE `hbtn_0c_0`

-- This command updates the database and the tabel 'first_table' 
ALTER TABLE `first_table` CONVERT TO CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

