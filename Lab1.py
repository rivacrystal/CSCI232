import psycopg2

class Queries():
    """Please submit this file on gradescope.
    Questions will appear when you submit to gradescope, there is no pentalty for resubmitting on gradescope.
    It is advised to copy paste the question you see when you submit on gradescope under each function name in case you need the question offline
    Put your solutions on the line following the line that starts with return for each question
"""

    def q1(self):
    	"""Q1: Create a table to store information about 'students'.
You should name your table 'students' (all lower case).
The columns of the table should be the following:
	student_id as a INTEGER (PRIMARY KEY)
	first_name as a VARCHAR(N) (N can be any value)
	last_name as a VARCHAR(N) (N can be any value)
	gpa as a real"""
    	
	return """
            CREATE TABLE students(
            student_id INTEGER PRIMARY KEY,
            first_name VARCHAR(20),
            last_name VARCHAR(20),
            gpa REAL
            );
	"""


    def q2(self):
	"""Create another table to store information about 'homeworks'.
You should name your table 'homeworks' (all lower case).
The columns of the table should be the following:
	homework_id as a INTEGER (PRIMARY KEY)
	student_id as a INTEGER (FOREIGN KEY)
	grade as a INTEGER"""
	
	return """
        CREATE TABLE homeworks(
        homework_id INTEGER PRIMARY KEY,
        student_id INTEGER REFERENCES students (student_id),
        grade INTEGER
        );
	"""


    def q3(self):
	"""A table without data is useless, so let us insert some rows for the 'students' table.
        Requirements:
	You must insert at least 20 rows.
	You can only submit 1 query.
	Enter exactly one row with 
		first name = Riva
		and
		last name = Crystal
	with any GPA."""
	
	return """
        INSERT INTO students (student_id, first_name, last_name, gpa)
        VALUES (1, 'Riva', 'Crystal', 4.0),
        (2, 'Paul', 'Maitland-McKinley', 3.9),
        (3, 'Jason', 'Greene', 3.9),
        (4, 'Mohammed', 'Ahmed', 3.7),
        (5, 'Harlan', 'Crystal', 4.0),
        (6, 'Robert', 'Landrito', 3.2),
        (7, 'Manuel', 'Lagdamen', 3.1),
        (8, 'Jason', 'Kilkenny', 3.8),
        (9, 'Vernon-Preston', 'Rogers', 3.1),
        (10, 'Stanley', 'Adecla', 3.7),
        (11, 'Devin', 'Sewell', 3.5),
        (12, 'Jane', 'Nam', 3.4),
        (13, 'Audrey', 'Nakao', 4.0),
        (14, 'Barry', 'Polinsky', 3.7),
        (15, 'Tameka', 'Howe', 3.8),
        (16, 'Joshua', 'Tanzer', 3.6),
        (17, 'Kevin', 'Tang', 3.7),
        (18, 'Anthony', 'Lemme', 3.3),
        (19, 'Colin', 'Tan', 3.6),
        (20, 'Julian', 'Gonzalez', 3.9)
        ;
	"""


    def q4(self):
	"""Let us emulate a homework assignment, insert rows into the 'homeworks' table.
Requirements:
	There must be a row assoicated with each existing student.
	At least one student must get lower than 18.
	One of the homeword_ids should be 5."""
	return """
		INSERT INTO homeworks (homework_id, student_id, grade)
		VALUES (1, 1, 105),
		(2, 2, 98),
		(3, 3, 87),
		(4, 4, 91),
		(5, 5, 90),
		(6, 6, 98),
		(7, 7, 87),
		(8, 8, 95),
		(9, 9, 67),
		(10, 10, 10),
		(11, 11, 75),
		(12, 12, 86),
		(13, 13, 86),
		(14, 14, 90),
		(15, 15, 82),
		(16, 16, 77),
		(17, 17, 23),
		(18, 18, 89),
		(19, 19, 75),
		(20, 20, 97)
		;
	"""


    def q5(self):
	"""I have decided the minimum grade for homeworks is 23.
	Update all homework rows where their grade is < minimum grade to the minimum grade"""
	return """
		UPDATE homeworks
		SET grade = 23
		WHERE grade < 23;
	"""

    def q6(self):
	"""I just discovered devilous student(s) cheated on my homework!
	I want you to delete the illegitimate homework from the table!
	Delete the row from the 'homeworks' table with a homework_id of 5
	NOTE: You must make sure this homework_id exists!"""
	return """
		DELETE FROM homeworks
		WHERE homework_id = 5;
	"""


    def q7(self):
	""" It's the end of the semseter!
	For privacy reasons we need to delete all the data that we've generated!
	Remove all both tables students and homeworks from the database!"""
	return """
        DROP TABLE students, homeworks;
	"""
