-- This command create table 'id_not_null' if it doesn't exist
-- with id INT DEFAULT 1 and name VARCHAR attributes 
CREATE TABLE IF NOT EXISTS `id_not_null` (
    `id` INT DEFAULT 1,
    `name` VARCHAR(256)
);

