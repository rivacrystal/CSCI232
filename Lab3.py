wimport psycopg2

class Queries():
    """
    Please submit this file on gradescope.
    Questions will appear when you submit to gradescope, there is no pentalty for resubmitting on gradescope.
    It is advised to copy paste the question you see when you submit on gradescope under each function name in case you need the question offline
    Put your solutions on the line following the line that starts with 'return' for each question
    """

    def q1(self):
	"""We will be working with 2 different tables. Their name and schemas are as follows:

crystal_customers_accounts, the columns of the table should be the following:
	id should be type integer
	first_name should be type character varying
	last_name should be type character varying
	bank_account_number should be type character varying
	paypal_email should be type character varying
	venmo_email should be type character varying
	created_at should be type date
This table should have 10 rows.

crystal_stocks, the columns of the table should be the following:
	id should be type integer
	symbol should be type character
	price should be type real
	last_updated_at should be type date
This table should have 5 rows.

Generate 2 queries to create these tables (table names should be all lower case).
All VARCHARs should be at minimum length 20(Besides symbol).
Primary keys should be included in your query.

Insert rows into your tables!
Restrictions:
	There should be a minimum of two rows in the customers table where all payment options are NULL. (bank_account_number,paypal_email, venmo_email are all NULL for a given row)
	There should be a minimum of two rows in the customers table where each payment option is NOT NULL.
	You should insert yourself as a customer! More specifically insert exactly 1 row with:
		first_name:riva
		last_name:crystal
	There is at least 3 unique dates for 'last_updated_at' column in the crystal_stocks table.
	All stock symbols should be unique! Stock symbols are exactly 4 characters long!
	Example row for stocks table:
		(1,'AAPL',150.32,'2020-01-01')

For all other questions, submit any incorrect query to see the question.
Note: Rows will be inserted on top of what you have inserted for Q1!"""
	return """
	CREATE TABLE crystal_customers_accounts (
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(30),
	last_name VARCHAR(30),
	bank_account_number VARCHAR(30),
	paypal_email VARCHAR(60),
	venmo_email VARCHAR(60),
	created_at DATE
	);

	CREATE TABLE crystal_stocks (
	id SERIAL PRIMARY KEY,
	symbol CHAR(4),
	price REAL,
	last_updated_at DATE
	);

	INSERT INTO crystal_customers_accounts (first_name, last_name, bank_account_number, paypal_email, venmo_email, created_at)
	VALUES ('riva', 'crystal', 109312931, 'riva.crystal92@myhunter.cuny.edu', 'riva.crystal92@myhunter.cuny.edu', '2022-03-18'),
	('Ezio', 'Auditore', 299109312, 'ezio.auditore@gmail.com', 'ezio.auditore@gmail.com', '2022-01-14'),
	('Vito', 'Scaletta', NULL, NULL, NULL, '2021-11-02'),
	('Hubert', 'Oswell', NULL, NULL, NULL, '2019-04-17'),
	('Simon', 'Belmont', NULL, NULL, NULL, '2010-03-25'),
	('Altair', 'ibnLaahad', 857195001, 'altair.laahad@gmail.com', 'altair.laahad@gmail.com', '2012-03-21'),
	('Senel', 'Coolidge', 100023391, 'senel.coolidge@gmail.com', 'senel.coolidge@gmail.com', '2009-09-01'),
	('Cervantes', 'de Leon', 987000192, 'cervantes.deleon@gmail.com', 'cervantes.deleon@gmail.com', '2013-02-26'),
	('Haytham', 'Kenway', NULL, NULL, NULL, '2019-04-12'),
	('Zelos', 'Wilder', 748192002, 'zelos.wilder@gmail.com', 'zelos.wilder@gmail.com', '2018-12-01')
	;

	INSERT INTO crystal_stocks (symbol, price, last_updated_at)
	VALUES ('LOTR', 14.21, '2022-03-20'),
	('SDFI', 17.22, '2022-03-23'),
	('BOTW', 60.57, '2022-03-22'),
	('TOTA', 50.58, '2022-03-15'),
	('FFIX', 40.42, '2022-03-18')
	;
	"""

    def q2(self):
	"""QUESTION:
	Let us anaylze our customers!
	Write a query that will pull the first and last name of any customers meeting the following requirement:
	Their account was created before the month of Jul of any year."""
	return """
	SELECT first_name, last_name FROM crystal_customers_accounts
	WHERE EXTRACT(month from created_at) < '7';
	"""

    def q3(self):
	"""We want to figure out which stocks where active between a certain period.
	Submit a query that will display the stock symbol of 'active' stocks.
	We define an active stocks as following:
	The stock was updated within a inclusive 8 year period starting at 2022-03-15
	Example: If my period lasts 100 year starting at 1999-01-01, then the end of my period is 2999-01-01."""
	return """
	SELECT symbol FROM crystal_stocks
	WHERE last_updated_at BETWEEN '2022-03-15' AND '2122-03-15';
	"""
    
    def q4(self):
	"""The SEC has frozen stocks from being updated due to suspicious activity.
	What we know right now is that all stocks that were last updated on 2022-03-22 have been flagged.
	We want to pull a general summery of stocks that were last updated on that day.
	Query the table to pull the total market price, highest priced stock, lowest priced stock and total amount of stocks updated that day including NULL prices. (In this order)
	"""
	return """
	SELECT SUM(price), MAX(price), MIN(price), COUNT(price) FROM crystal_stocks
	WHERE last_updated_at = '2022-03-22';
	"""

    def q5(self):
	"""I'm making a trading bot that will pull data from the crystal_stocks table.
	My trading algorithm is simple.
	If the price of the stock is >= than 4141.5 then I sell (assuming i have the stock).
	If the price of the stock is < than 4141.5 then I buy.
	I need you to generate a query that will return to me a list to give to my bot.
	The query should list the stock symbol and the action I should take based on my algorithm.
	The action should be one of two values, 'BUY' or 'SELL' (case sen.)
	Example:
	AAPL, SELL
	GOOG, BUY
	This assumes that the price for AAPL was >= 4141.5.
	This assumes that the price for GOOG was < 4141.5."""
	return """
	SELECT symbol,
	CASE
	  WHEN price >= 4141.5 THEN 'SELL'
	  WHEN price < 4141.5 THEN 'BUY'
	END
	FROM crystal_stocks;
	"""

    def q6(self):
	"""We want a list of payment details for every customer.
	When signing up we do not force users to input a payment method, thus those fields are NULL.
	Can you generate a list where you display the customer's first and last name along with their payment detail. (In this order)
	You should be accepting the first payment detail based on the following precedence:
	venmo_email
	bank_account_number
	paypal_email
	If a customer has no payment method return a NULL.
	The list should also NOT have your information (exclude yourself from the generated list).
	Example row: (riva,crystal,riva.crystal92@myhunter.cuny.edu). Assume riva.crystal92@myhunter.cuny.edu is your paypal email and you do not have a bank_account_number."""
	return """
	SELECT first_name, last_name, COALESCE(venmo_email, bank_account_number, paypal_email) FROM crystal_customers_accounts
	WHERE id != 1; 
	"""
