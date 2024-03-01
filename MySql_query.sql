-- Show all available database
show databases;

-- Create a new database
create database sweetCocoStore;

-- Switch to custom database
use sweetCocoStore;

-- Show all table of database
show tables;

-- Grant permision
GRANT ALL ON sweetCocoStore.* TO 'sweetCocoAdmin'@'%';
FLUSH PRIVILEGES;

-- Create test database
create database test_sweetcocostore;
DROP DATABASE test_sweetcocostore;