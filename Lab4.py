import psycopg2

class Queries():
    """
    """

    def q1(self):
	"""    Q1: We will be working with 3 different tables. Their name and schemas are as follows:

	crystal_customers, the columns of the table should be the following:
	id should be type integer
	first_name should be type character varying
	last_name should be type character varying
	email should be type character varying
	This table should have 10 rows.

	crystal_items, the columns of the table should be the following:
	id should be type integer
	name should be type character varying
	price should be type real
	This table should have 10 rows.

	crystal_orders, the columns of the table should be the following:
	customer_id should be type integer
	item_id should be type integer
	purchase_date should be type date
	This table should have 20 rows.

	Generate 3 queries to create these tables (table names should be all lower case).
	All VARCHARs should be at minimum length 20.
	Primary keys and Foreign keys should be included in your query.

	Insert rows into your tables!
	Restrictions:
	You should insert yourself as a customer! More specifically insert exactly 1 row with:
		first_name:riva
		last_name:crystal
		email:riva.crystal92@myhunter.cuny.edu
	Each customer and item needs to be assoicated with at least one transaction.
	All customers should be unique (all fields besides FK should be unique).
	All items should be unique (all fields besides FK and purchase_date should be unique).

	For all other questions, submit any incorrect query to see the question.
	Note: Rows will be inserted on top of what you have inserted for Q1!"""
	return """
	CREATE TABLE crystal_customers(
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(30),
	last_name VARCHAR(30),
	email VARCHAR(50)
	);

	INSERT INTO crystal_customers (first_name, last_name, email)
	VALUES ('riva', 'crystal', 'riva.crystal92@myhunter.cuny.edu'),
	('Terra', 'Branford', 'terra.branford@gmail.com'),
	('Locke', 'Cole', 'locke.cole@gmail.com'),
	('Edgar', 'Figaro', 'edgar.figaro@gmail.com'),
	('Sabin', 'Figaro', 'sabin.figaro@gmail.com'),
	('Cyan', 'Garamonde', 'cyan.garamonde@gmail.com'),
	('Gau', 'Crazy Kid', 'gau@gmail.com'),
	('Celes', 'Chere', 'celes.chere@gmail.com'),
	('Setzer', 'Gabbiani', 'setzer.gabbiani@gmail.com'),
	('Strago', 'Magus', 'strago.magus@gmail.com')
	;

	CREATE TABLE crystal_items(
	id SERIAL PRIMARY KEY,
	name VARCHAR(50),
	price REAL
	);

	INSERT INTO crystal_items(name, price)
	VALUES ('Tales of the Abyss', 50),
	('Silent Hill 2', 50),
	('Street Fighter II', 60),
	('Okami', 40),
	('Shadow of the Colossus', 50),
	('Civilization V', 20),
	('Quake', 10),
	('Final Fantasy VII', 60),
	('The Legend of Zelda: Minish Cap', 20),
	('LocoRoco 2', 15)
	;

	CREATE TABLE crystal_orders(
	customer_id INTEGER REFERENCES crystal_customers (id),
	item_id INTEGER REFERENCES crystal_items (id),
	purchase_date DATE
	);

	INSERT INTO crystal_orders
	VALUES (1, 4, '2008-11-21'),
	(2, 8, '1997-09-07'),
	(3, 2, '2018-03-02'),
	(4, 7, '1996-12-22'),
	(5, 5, '2012-12-05'),
	(6, 3, '1992-08-05'),
	(7, 10, '2009-02-10'),
	(8, 6, '2010-09-21'),
	(9, 1, '2012-02-14'),
	(10, 9, '2005-01-10'),
	(1, 1, '2012-03-07'),
	(2, 10, '2009-01-31'),
	(3, 5, '2020-06-14'),
	(4, 3, '2022-02-04'),
	(5, 5, '2001-07-27'),
	(6, 2, '2005-06-16'),
	(7, 5, '2009-06-10'),
	(8, 2, '1995-04-23'),
	(10, 7, '1999-11-06'),
	(10, 9, '2002-08-31')
	;
	"""

    def q2(self):
	"""Write a query to return the name of the item(s) that was associated with the most recent order(s)."""
	return """
	SELECT name FROM crystal_items WHERE id =
	(SELECT item_id FROM crystal_orders WHERE purchase_date =
	(SELECT MAX(purchase_date) FROM crystal_orders));
	"""

    def q3(self):
	"""We want to check how well certain items are doing in the store.
	Write a query to return the item id and the amount of times that item has been ordered!
	We only care about items_ids in the following list:
	1,2,8,3,4,5,6,7,"""
	return """
	SELECT item_id, COUNT(item_id) FROM crystal_orders
	WHERE item_id IN (1,2,8,3,4,5,6,7)
	GROUP BY item_id
	ORDER BY COUNT(item_id) DESC;
	"""
    
    def q4(self):
	"""Write a query to return the name of items that have been ordered more than 44 times."""
	return """
	WITH temp as (SELECT item_id, COUNT(item_id) FROM crystal_orders
	GROUP BY item_id
	HAVING count(item_id) > 44)
	SELECT name FROM crystal_items
	WHERE id IN (SELECT item_id FROM temp);
	"""

    def q5(self):
	"""Business could be better. Let's gather some information to see what we can do!
	We want to send out surveys to figure out what we can do better!
	Write a query that will return the email of customers that have the highest count of orders."""
	return """
 	WITH temp AS
 	(SELECT customer_id, COUNT(customer_id) FROM crystal_orders
 	GROUP BY customer_id
 	ORDER BY COUNT(customer_id) DESC LIMIT 1)
	SELECT email FROM crystal_customers
	WHERE id IN (SELECT customer_id FROM temp);
	"""

    def q6(self):
	"""We want a overall view into the crystal_orders table.
	We would like to have a list of customer_ids and the amount of purchases they have made.
	We would also like the list (based on purchase amount) to be ranked in desending order!
	The list should also NOT include your customer_id!"""
	return """
	SELECT customer_id, COUNT(customer_id) FROM crystal_orders
	WHERE customer_id != 1
	GROUP BY customer_id
	ORDER BY customer_id DESC;
	"""
