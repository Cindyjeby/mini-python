# creates a table empd which contains employee details

USE employee_db;
CREATE TABLE empd(
	id INT PRIMARY KEY,
	name VARCHAR(255),
	post VARCHAR(255),
	salary INT
);
