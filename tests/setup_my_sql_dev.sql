-- Prepares a MYSQL server for project
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create a new user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

GRANT  ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
-- Grant SELECT on performance schema.

GRANT SELECT  ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
