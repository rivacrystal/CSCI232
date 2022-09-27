import psycopg2

class Queries():
    """
    Please submit this file on gradescope.
    Questions will appear when you submit to gradescope, there is no pentalty for resubmitting on gradescope.
    It is advised to copy paste the question you see when you submit on gradescope under each function name in case you need the question offline
    Put your solutions on the line following the line that starts with 'return' for each question
    """

    def q1(self):
	"""Q1: We will be working with 3 different tables. Their name and schemas are as follows:

	crystal_employees, the columns of the table should be the following:
	id should be type integer
	first_name should be type character varying
	last_name should be type character varying
	email should be type character varying
	join_date should be type date
	manager_id should be type integer
	department_id should be type integer
	This table should have 5 rows.

crystal_salaries, the columns of the table should be the following:
	employee_id should be type integer
	salary should be type real
This table should have 5 rows.

crystal_department, the columns of the table should be the following:
	id should be type integer
	name should be type character varying
	address should be type character varying
This table should have 3 rows.

Note: Treat manager_id as a FK to employees(id). DO NOT form a FK on this pairing.Generate 3 queries to create these tables (table names should be all lower case).
All VARCHARs should be at minimum length 20.
Primary keys and Foreign keys should be included in your query.

Insert rows into your tables!
Restrictions:
	You should insert yourself as a customer! More specifically insert exactly 1 row with:
		first_name: riva
		last_name: crystal
		email: riva.crystal92@myhunter.cuny.edu
		join_date: Today's date in form yyyy-mm-dd

For all other questions, submit any incorrect query to see the question.
Note: Rows will be inserted on top of what you have inserted for Q1!"""
	return """
	CREATE TABLE crystal_department(
	id SERIAL PRIMARY KEY,
	name VARCHAR (60),
	address VARCHAR(70)
	);

	INSERT INTO crystal_department (name, address)
	VALUES ('Executive', '890 Fifth Avenue'),
	('Engineering', '177A Bleecker Street'),
	('Public Relations', '1007 Mountain Drive');

	CREATE TABLE crystal_employees(
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(30),
	last_name VARCHAR(30),
	email VARCHAR(70),
	join_date DATE,
	manager_id INTEGER,
	department_id INTEGER REFERENCES crystal_department (id)
	);

	INSERT INTO crystal_employees (first_name, last_name, email, join_date, manager_id, department_id)
	VALUES ('riva', 'crystal', 'riva.crystal92@myhunter.cuny.edu', '2022-04-15', 11, 1),
	('Kazuma', 'Kiryu', 'kazuma.kiryu@industries.com', '2022-04-12', 22, 1),
	('James', 'Sunderland', 'james.sunderland@industries.com', '2022-04-11', 33, 2),
	('Cloud', 'Strife', 'cloud.strife@industries.com', '2022-04-10', NULL, 3),
	('Bruce', 'Wayne', 'bruce.wayne@industries.com', '2022-04-09', 55, 1);

	CREATE TABLE crystal_salaries(
	employee_id SERIAL REFERENCES crystal_employees (id),
	salary REAL
	);

	INSERT INTO crystal_salaries (salary)
	VALUES (100000),
	(50000),
	(40000),
	(150000),
	(120000);
	"""

    def q2(self):
	"""The higher ups have approved a salary update for certain employees!
	Display the resulting salary from the salaries table to deduct all salaries by 420 of those who make more than 92000!"""
	return """
	SELECT (salary - 420) FROM crystal_salaries
	WHERE salary > 92000;
	"""

    def q3(self):
	"""Write a query to return the email of employees that joined after 2022-02-17."""
	return """
	SELECT email FROM crystal_employees
	WHERE join_date > '2022-02-17';
	"""
    
    def q4(self):
	"""Write a query to return first_name,last_name for those who do not have an manager.
	We only care about people who joined between 2022-02-17 and 2022-05-30.
	"""
	return """
	SELECT first_name, last_name FROM crystal_employees
	WHERE join_date BETWEEN '2022-02-17' AND '2022-05-30'
	AND manager_id IS NULL;
	"""

    def q5(self):
	"""Find the first_name, last_name of the employee(s) that are paid the most that also doesn't have a manager!"""
	return """
	WITH temp AS
 	(SELECT employee_id, MAX(salary) FROM crystal_salaries
 	GROUP BY employee_id
 	ORDER BY MAX(salary) DESC LIMIT 1)
	SELECT first_name, last_name FROM crystal_employees
	WHERE id IN (SELECT employee_id FROM temp) AND manager_id IS NULL;
	"""

    def q6(self):
	"""Generate a list of salary where we see the top 5 salaries ordered from top to bottom!"""
	return """
	SELECT salary FROM crystal_salaries
	ORDER BY salary DESC
	LIMIT 5;
	"""

    def q7(self):
	"""Pull the first_name, email of employees where they belong to a interesting department.
	We define a interesting department of having > 5 employees assigned to that department.
	"""
	return """
	WITH temp AS
	(SELECT department_id FROM crystal_employees
	GROUP BY department_id
	HAVING COUNT(department_id) > 5)
	SELECT first_name, email FROM crystal_employees
	WHERE department_id IN
	(SELECT department_id FROM temp);
	"""

    def q8(self):
	"""Return the id,name,address of your department."""
	return """
	SELECT id, name, address FROM crystal_department
	WHERE id = (SELECT department_id FROM crystal_employees
	WHERE first_name = 'riva');
	"""

    def q9(self):
	"""Return a list of last_name, email,<manager email> for each employee.Where <manager email> is the manager's email.
	If employee doesn't have a manager return 'NO MANAGER' (case sen.).
	Do not include yourself in the list!
	Hint: To get manager's email, run a subquery. Aliasing might be required."""
	return """
	SELECT last_name, email,
	CASE
		WHEN
			manager_id IS NULL THEN 'NO MANAGER'
		ELSE
			(SELECT email FROM crystal_employees a
			WHERE b.manager_id = a.id)
	END "<manager email>"
	FROM crystal_employees b
	WHERE id != 1;
	"""