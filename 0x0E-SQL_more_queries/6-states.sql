-- this is a script to create the database,a table in the database

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
	id INT AUTO_INCREMENT NOT NULL,
	name VARCHAR(256),
	PRIMARY KEY(id)
	);
