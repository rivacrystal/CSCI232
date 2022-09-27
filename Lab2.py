import psycopg2

class Queries():
    """
    Please submit this file on gradescope.
    Questions will appear when you submit to gradescope, there is no pentalty for resubmitting on gradescope.
    It is advised to copy paste the question you see when you submit on gradescope under each function name in case you need the question offline
    Put your solutions on the line following the line that starts with 'return' for each question
    """

    def q1(self):
	"""We will be working with 2 different tables. Their name and schemas are as follows:
	
	crystal_employees, the columns of the table should be the following:
	id should be type integer
	first_name should be type character varying
	last_name should be type character varying
	email should be type character varying
	age should be type integer

	crystal_salaries, the columns of the table should be the following:
	employee_id should be type integer
	salary should be type real

	Generate 2 queries to create these tables (table names should be all lower case).
	All VARCHARs should be at minimum length 20.
	Primary keys and Foreign key should be included in your query."""
	
	return """
		CREATE TABLE crystal_employees (
		id SERIAL PRIMARY KEY,
		first_name VARCHAR(20),
		last_name VARCHAR(20),
		email VARCHAR(50),
		age INTEGER
		);

		CREATE TABLE crystal_salaries (
		employee_id SERIAL REFERENCES crystal_employees (id),
		salary REAL
		);
	"""

    def q2(self):
	""" Insert some rows into your tables! Restrictions:
	There should be at least 20 rows in each table!
	The employee table tuples should all be unique!
	We consider a row to be unique for all attributes besides a PK or FK!
	All rows in both tables should form a one - one connection!
	You should insert yourself as a employee! More specifically insert exactly 1 row with:
		first_name:riva
		last_name:crystal
		email:riva.crystal92@myhunter.cuny.edu"""

	return """
		INSERT INTO crystal_employees (first_name, last_name, email, age)
		VALUES ('riva', 'crystal', 'riva.crystal92@myhunter.cuny.edu', 35),
		('Luke', 'fon Fabre', 'luke.fabre@crystalindustries.com', 20),
		('Cloud', 'Strife', 'cloud.strife@crystalindustries.com', 21),
		('Yuri', 'Lowell', 'yuri.lowell@crystalindustries.com', 32),
		('Kazama', 'Kiryu', 'kazama.kiryu@crystalindustries.com', 37),
		('Zidane', 'Tribal', 'zidane.tribal@crystalindustries.com', 26),
		('M.', 'Bison', 'm.bison@crystalindustries.com', 47),
		('Galuf', 'Baldesion', 'galuf.baldesion@crystalindustries.com', 58),
		('Jade', 'Curtiss', 'jade.curtiss@crystalindustries.com', 60),
		('James', 'Sunderland', 'james.sunderland@crystalindustries.com', 29),
		('Cecil', 'Harvey', 'cecil.harvey@crystalindustries.com', 30),
		('Velvet', 'Crowe', 'velvet.crowe@crystalindustries.com', 19),
		('Heihachi', 'Mishima', 'heihachi.mishima@crystalindustries.com', 48),
		('Locke', 'Cole', 'locke.cole@crystalindustries.com', 69),
		('Stahn', 'Aileron', 'stahn.aileron@crystalindustries.com', 45),
		('Chris', 'Redfield', 'chris.redfield@crystalindustries.com', 25),
		('Claire', 'Farron', 'claire.farron@crystalindustries.com', 61),
		('Reid', 'Hershel', 'reid.hershel@crystalindustries.com', 68),
		('Aya','Brea', 'aya.brea@crystalindustries.com', 53),
		('Jude', 'Mathis', 'jude.mathis@crystalindustries.com', 56)
		;

		INSERT INTO crystal_salaries (salary)
		VALUES (100000),
		(50000),
		(25000),
		(60000),
		(65000),
		(70000),
		(80000),
		(85000),
		(20000),
		(66000),
		(78000),
		(85500),
		(92000),
		(72000),
		(90000),
		(95000),
		(71000),
		(82000),
		(89000),
		(55000)
		;
	"""

    def q3(self):
	"""While entering salary information into crystal_salaries, an employee mistakenly created false entries!
	Write a query that will return all unique values of employee_id from crystal_salaries to detect the outlier values!"""
	return """
	SELECT DISTINCT employee_id FROM crystal_salaries; 
	"""
    
    def q4(self):
	"""Write a query that gets the first and last name of employees that are older than you!"""
	return """
	SELECT first_name, last_name FROM crystal_employees
	WHERE age > 35;
	"""

    def q5(self):
	"""Generate a query that will display a column called 'new_salaries' if you where to give all employee a flat salary raise of 9."""
	return """
	SELECT (salary + 9) AS new_salaries FROM crystal_salaries;
	"""

    def q6(self):
	"""A hacker got into our systems!
	They attempted to flood our crystal_employees table!
	The IT department has discovered that the hacker has inserted rows where either the first or last name is NULL.
	An additional finding is that the emails of the rows have the value riva.crystal92@myhunter.cuny.edu
	Write a query that will return the id of every row that we did not add."""
	return """
	SELECT id FROM crystal_employees
	WHERE first_name IS NULL
	OR
	last_name IS NULL
	;
	"""

    def q7(self):
	"""The law requires that you pay your employees a minimum wage of 20345.0
	You can only afford to pay 17 employees.
	Generate a query to return the employee ids of 17 employees where they are being paid below the minimum wage!"""
	return """
	SELECT employee_id FROM crystal_salaries
	WHERE salary < 20345.0
	LIMIT 17;
	"""
