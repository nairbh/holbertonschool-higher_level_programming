--  creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.
CREATE TABLE IF NOT EXISTS second_table(
	id INT,
	score INT,
	name VARCHAR(256)
	);
INSERT INTO second_table(id, score, name)
VALUES
	(1, 10, 'Jhone'),
	(2, 3, 'Alex'),
	(3, 14, 'Bob'),
	(4, 8, 'George');
