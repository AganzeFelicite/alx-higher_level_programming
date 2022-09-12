-- this is to make a unique id ie the primary key

CREATE TABLE IF NOT EXISTS unique_id(
	id INT DEFAULT 1,
	name VARCHAR(256),
	PRIMARY KEY(id)
	);
