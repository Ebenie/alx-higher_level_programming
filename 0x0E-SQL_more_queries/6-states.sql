-- This command create database hbtn_0d_usa if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- This command Use database hbtn_0d_usa for the next command
USE hbtn_0d_usa;

-- This command create table states if it doesn't exist
CREATE TABLE IF NOT EXISTS `states` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(256) NOT NULL
);

