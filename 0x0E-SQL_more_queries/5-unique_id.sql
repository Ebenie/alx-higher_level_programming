-- This command create table 'unique'_id if it doesn't exist
-- with id INT DEFAULT 1 UNIQUE and name VARCHAR attributes 
CREATE TABLE IF NOT EXISTS `unique_id` (
    `id` INT DEFAULT 1 UNIQUE,
    `name` VARCHAR(256)
);

