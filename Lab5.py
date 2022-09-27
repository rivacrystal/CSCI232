import psycopg2

class Queries():
    """
    Please submit this file on gradescope.
    Questions will appear when you submit to gradescope, there is no pentalty for resubmitting on gradescope.
    It is advised to copy paste the question you see when you submit on gradescope under each function name in case you need the question offline
    Put your solutions on the line following the line that starts with 'return' for each question
    """

    def q1(self):
	"""We will be emulating a simple bank for this lab.It is highly recommended to copy these questions onto your submitting file.


	Q1: We will be working with 3 different tables. Their name and schemas are as follows:

	crystal_accounts, the columns of the table should be the following:
	id should be type integer
	first_name should be type character varying
	last_name should be type character varying
	email should be type character varying
	This table should have 10 rows.

	crystal_credit_card_transactions, the columns of the table should be the following:
	id should be type integer
	card_id should be type integer
	amount should be type real
	This table should have 20 rows.

	crystal_credit_cards, the columns of the table should be the following:
	id should be type integer
	account_id should be type integer
	card_limit should be type real
	This table should have 10 rows.

	Generate 3 queries to create these tables (table names should be all lower case).
	All VARCHARs should be at minimum length 20.
	Primary keys and Foreign keys should be included in your query.

	Insert rows into your tables!
	Restrictions:
	You should insert create an account for yourself! More specifically insert exactly 1 row with:
		first_name:riva
		last_name:crystal
		email:riva.crystal92@myhunter.cuny.edu
	Each account should be unique!
	Each card needs to have at least one transaction!

	For all other questions, submit any incorrect query to see the question.
	Note: Rows will be inserted on top of what you have inserted for Q1!"""
	return """
	CREATE TABLE crystal_accounts(
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(30),
	last_name VARCHAR(30),
	email VARCHAR(50)
	);

	INSERT INTO crystal_accounts (first_name, last_name, email)
	VALUES ('riva', 'crystal', 'riva.crystal92@myhunter.cuny.edu'),
	('Jack', 'Napier', 'jack.napier@gmail.com'),
	('Jean-Paul', 'Valley', 'jpv@sofd.org'),
	('Waylon', 'Jones', 'wjones@reptilesanctuary.org'),
	('Basil', 'Karlo', 'basil.karlo@palacetheatre.org'),
	('Edward', 'Nigma', 'edward.nigma@gmail.com'),
	('William', 'Tockman', 'william.tockman@gmail.com'),
	('Jervis', 'Tetch', 'jervis.tetch@gmail.com'),
	('Victor', 'Fries', 'victor.fries@gmail.com'),
	('Oswald', 'Cobblepot', 'oswald.cobblepot@gmail.com')
	;

	CREATE TABLE crystal_credit_cards(
	id SERIAL PRIMARY KEY,
	account_id INTEGER REFERENCES crystal_accounts (id),
	card_limit REAL
	);

	INSERT INTO crystal_credit_cards (account_id, card_limit)
	VALUES (1, 6000),
	(2, 5000),
	(3, 7000),
	(4, 5000),
	(5, 9000),
	(6, 10000),
	(7, 4000),
	(8, 2000),
	(9, 15000),
	(10, 20000)
	;

	CREATE TABLE crystal_credit_card_transactions(
	id SERIAL,
	card_id INTEGER REFERENCES crystal_credit_cards (id),
	amount REAL
	);

	INSERT INTO crystal_credit_card_transactions(card_id, amount)
	VALUES (1, 20.25),
	(1, 19.99),
	(2, 70),
	(2, 100.58),
	(3, 6),
	(3, 10.99),
	(4, 70.11),
	(4, 600.54),
	(5, 77.55),
	(5, 100.20),
	(6, 262.55),
	(6, 58.42),
	(7, 50.22),
	(7, 40.11),
	(8, 90.80),
	(8, 90.09),
	(9, 41.10),
	(9, 4),
	(10, 13.1),
	(10, 54.54)
	;
	"""

    def q2(self):
	"""Return last_name of accounts that have a credit card assoicated with them.
	Exclude yourself from the list."""
	return """
	SELECT last_name FROM crystal_accounts
	RIGHT JOIN crystal_credit_cards
	ON crystal_accounts.id = crystal_credit_cards.id
	WHERE crystal_accounts.id != 1;
	"""

    def q3(self):
	"""We want to view a overall picture of all credit cards.
	Write a query to return card_id, amount of transactions assoicated with the card.
	This should return a row only if a transaction exists for the card."""
	return """
	SELECT card_id, COUNT(amount)
	FROM crystal_credit_card_transactions
	GROUP BY card_id;

	"""
    
    def q4(self):
	"""Write a query that will return the email, card id, card limit and transactions amounts (for each transaction) for each card.
	Do not include yourself in the list!"""
	return """
	SELECT crystal_accounts.email, crystal_credit_cards.id, crystal_credit_cards.card_limit, crystal_credit_card_transactions.amount FROM crystal_accounts
	JOIN crystal_credit_cards
	ON crystal_accounts.id = crystal_credit_cards.account_id
	JOIN crystal_credit_card_transactions
	ON crystal_credit_cards.id = crystal_credit_card_transactions.card_id
	WHERE crystal_accounts.id != 1;
	"""

    def q5(self):
	"""We are not generating enough money!
	We want to get people who haven't used their card to spend more!
	Return a list of last_name,email of those who have credit cards and have not used them!"""
	return """
	SELECT crystal_accounts.last_name, crystal_accounts.email FROM crystal_accounts
	LEFT JOIN crystal_credit_cards
	ON crystal_accounts.id = crystal_credit_cards.account_id
	LEFT join crystal_credit_card_transactions
	ON crystal_credit_cards.id = crystal_credit_card_transactions.card_id
	WHERE crystal_credit_card_transactions.card_id IS NULL;
	;
	"""

