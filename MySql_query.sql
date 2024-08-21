show databases;
DROP DATABASE sweetcocostore;
CREATE DATABASE sweetcocostore;
use sweetCocoStore;
-- Show all table of database
show tables;
SHOW CREATE TABLE sweetcocoweb_order;

SELECT
    CONSTRAINT_NAME,
    CONSTRAINT_TYPE,
    COLUMN_NAME,
    REFERENCED_TABLE_NAME,
    REFERENCED_COLUMN_NAME
FROM
    INFORMATION_SCHEMA.KEY_COLUMN_USAGE
WHERE
    TABLE_SCHEMA = 'sweetCocoStore' AND
    TABLE_NAME = 'sweetcocoweb_order';