-- This command creates a database hbtn_0d_2 if not
-- exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2

-- This command creates user if not exist without privilege
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- This command grants privilege on SELECT for user 'user_0d_2'
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

