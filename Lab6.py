import psycopg2

class Queries():
    """
    Please submit this file on gradescope.
    Questions will appear when you submit to gradescope, there is no pentalty for resubmitting on gradescope.
    It is advised to copy paste the question you see when you submit on gradescope under each function name in case you need the question offline
    Put your solutions on the line following the line that starts with 'return' for each question
    """

    def q1(self):
	"""We will be emulating a simple posting website for this lab.It is highly recommended to copy these questions onto your submitting file.

	Q1: We will be working with 2 different tables. Their name and schemas are as follows:

	crystal_users, the columns of the table should be the following:
	id should be type integer
	username should be type character varying
	password should be type character varying
	email should be type character varying
	This table should have 20 rows.

	crystal_posts, the columns of the table should be the following:
	id should be type integer
	user_id should be type integer
	content should be type text
	This table should have 20 rows.

	Generate 2 queries to create these tables (table names should be all lower case).
	All VARCHARs should be at minimum length 20.
	Primary keys and Foreign keys should be included in your query.

	Insert rows into your tables!
	Restrictions:
	You should insert create an account for yourself! More specifically insert exactly 1 row with:
		username:rivacrystal
		password:crystalriva
		email:riva.crystal92@myhunter.cuny.edu
	All users rows should be unique besides PK

	For all other questions, submit any incorrect query to see the question.
	Note: Rows will be inserted on top of what you have inserted for Q1!"""
	return """
	CREATE TABLE crystal_users(
	id SERIAL PRIMARY KEY,
	username VARCHAR(50),
	password VARCHAR(50),
	email VARCHAR(50)
	);

	INSERT INTO crystal_users (username, password, email)
	VALUES ('rivacrystal', 'crystalriva', 'riva.crystal92@myhunter.cuny.edu'),
	('greengoblin', 'youlosespiderman', 'norman.osborn@gmail.com'),
	('greengoblinjr', 'whypeter', 'harry.osborn@gmail.com'),
	('docock', 'spidermansux', 'otto.octavius@gmail.com'),
	('kingpin', 'illtakedownspiderman', 'wilson.fisk@gmail.com'),
	('chameleon', 'spidermansucks', 'dmitri.smerdyakov@gmail.com'),
	('rhino', 'spidermanshouldie', 'aleksei.sytsevich@gmail.com'),
	('lizard', 'killspiderman', 'curt.connors@gmail.com'),
	('vulture', 'ihatespiderman', 'adrian.toomes@gmail.com'),
	('mysterio', 'spidermanisthedevil', 'quentin.beck@gmail.com'),
	('sandman', 'nospiderman', 'flint.marko@gmail.com'),
	('electro', 'spidermanshouldgotohell', 'maxwell.dilton@gmail.com'),
	('shocker', 'illgetyouspiderman', 'herman.schultz@gmail.com'),
	('kraventhehunter', 'spidermanthetrophy', 'sergei.kravinoff@gmail.com'),
	('tombstone', 'takedownspiderman', 'lonnie.lincoln@gmail.com'),
	('venom', 'killlllll', 'venom@gmail.com'),
	('carnage', 'killlllllllllll', 'carnage@gmail.com'),
	('scorpion', 'screwyouspiderman', 'mac.gargan@gmail.com'),
	('blackcat', 'imnotacatwomanripoff', 'felicia.hardy@gmail.com'),
	('mr.negative', 'destroyspiderman', 'martin.li@gmail.com')
	;

	CREATE TABLE crystal_posts(
	id SERIAL PRIMARY KEY,
	user_id INTEGER REFERENCES crystal_users (id),
	content TEXT
	);

	INSERT INTO crystal_posts (user_id, content)
	VALUES (1, 'Try to get a 100 on the final!'),
	(2, 'Nothing keeps me down, Kingsley. Not death. Betrayal. Even the entire world against me! Every time I rise back up! Stronger than before! Every time!'),
	(3, 'After all these years of feeling so small... So helpless...I''m finally above them all! I''ve got the power to crush you--crush anyone who gets in my way! Now...at long last--I truly am the Green Goblin!!'),
	(4, 'Then I shall endeavor to exceed your expectations. Let others settle for greatness, Max. I always strive to be superior.'),
	(5, 'The underworld will now be run like a business... and the chairman of the board will be... the Kingpin!'),
	(6, 'I am invisible because I am the same thing you look at every dreadful, dull day. I am the day before you realize everything has gone horribly, horribly wrong. I am the Chameleon.'),
	(7, 'I''m Rhino. I knock things down. That''s what I do. That''s who I am.'),
	(8, 'Not... a monster. I''m Curtisss Connorsss. And I will never let the monstersss win again.'),
	(9, 'I fought Daredevil. I was in the Sinister Six. I''m faster, stronger, and smarter than a hundred men my age. No flunky with a pistol gets the drop on me.'),
	(10, 'I learned this a long time ago. Never listen to Mysterio. Not because he tends to go on and on (which is true)... He''s got illusions, the gas, but the helmet gives his speech pattern some crazy mind-bending properties.'),
	(11, 'When I saw those bad guys gone good on TV, part of me thought they were crazy. But I gotta admit, doing the right thing like this... it feels pretty damn good.'),
	(12, 'Jewels! Money! No matter how much I take, I want more--much more! And with my great power, nothing can stop me from getting it!'),
	(13, 'Tryin'' to land on top, that was always Fred''s things-- me, I always just wanted to treat this like a real job. Keep your head down, make a living, get out early. Everyone thinks that makes me a coward, but that''s fine. I don''t really care about all that. My reputation-- look at me, I wear a quilt! What kind of reputation am I gonna have? I was starting to get a little saved up, was looking at places in Hoboken--places with yards, even! But now--now this happens... Don''t even know why I took ''im in the first place.'),
	(14, 'I am not perfect, Belka, Squirrel Girl, and I will have setbacks. There will be times when others tell you to give up hope, that if he ever existed, the Kraven you knew is dead. But they are not reckoning with the persistence of a hunter. There will come a day when I stand beside you as an ally.'),
	(15, '''Cold as ice, hard as marble''... I like that, Web-Spinner. Thanks. All my life I felt like a freak. What else would you call an albino? -- A black man trapped in a white man''s skin? People looked at me, they saw a monster. But I was just a man. Now I am a monster, and I love it. Yeah: ''Cold as ice, hard as marble''... What else would you call a tombstone?'),
	(16, 'Been to many worlds, but none of them this strange. Understood feelings before, but simple feelings - like colors, bold and bright. Happy. Sad. Angry. Then... met Spider-Man. Feelings got complicated. Learned guilt. Also the first time I felt fear. Felt agony. Learned feeling: Betrayal. Learned first words they called me. Monster. Parasite. Bad.'),
	(17, 'Maybe if my host had a little more filial sentiment... a little more human love for his own daddy... some of it would have crossed over to me. As it is, I feel nothing but cold empty contempt. I hate you, daddy.'),
	(18, 'You don''t have to ask, Smythe. Killing the Spider''s always been my idea of fun. But after what he did to me--to us--we won''t leave enough of him to bury.'),
	(19, 'I''m not a hero. I''m a thief. Born a thief. Raised a thief. Will die a thief.'),
	(20, 'I always like to have reminders around that there is no good he can do... that I cannot corrupt.')
	;
	"""

    def q2(self):
	"""Return the username,password, average length of each post for all users who have generated a post
	Exclude yourself from the list."""
	return """
	SELECT crystal_users.username, crystal_users.password, AVG(CHAR_LENGTH(crystal_posts.content)) FROM crystal_users
	JOIN crystal_posts
	ON crystal_users.id = crystal_posts.user_id
	WHERE crystal_users.id != 1
	GROUP BY crystal_users.username, crystal_users.password;
	"""

    def q3(self):
	"""Our users have being hacked at a high rate!
	Write a query that returns the username,email,content for all users who have the following:
	They have posted their email in a post they have made.
	The user's emails end in .com."""
	return """
	SELECT crystal_users.username, crystal_users.email, crystal_posts.content FROM crystal_users
	JOIN crystal_posts ON crystal_users.id = crystal_posts.user_id
	WHERE crystal_posts.content LIKE CONCAT('%', crystal_users.email, '%')
	AND crystal_users.email LIKE '%.com';
	"""
    
    def q4(self):
	"""Return the username,password of users who meet the following conditions:
	Their username is exactly 11 characters long.
	The character at index 0 is r.
	The character at index 5 is r.
	Their email ends with myhunter.cuny.edu
	Note: Character is 0 index (index 0 is the first character)"""
	return """
	SELECT username, password FROM crystal_users
	WHERE LENGTH(username) = 11
	AND username LIKE 'r____r%'
	AND email LIKE '%myhunter.cuny.edu';
	"""

    def q5(self):
	"""Return a query that will return username retaining to the post that contains the following:
	The post does not contain any lowercase letters.	The post author's email does not have a @ symbol"""
	return """
	SELECT crystal_users.username FROM crystal_users
	JOIN crystal_posts ON crystal_users.id = crystal_posts.user_id
	WHERE crystal_users.email NOT LIKE '%@%'
	AND crystal_posts.content !~* '[^a-z]';
	"""

    def q6(self):
	"""We are interested in finding the users that generate post with the most words
	Write a query to return the username,email of the posts containing the highest word count
	Hint: In a sentence to count the words you count the spaces"""
	return """
	WITH temp AS (SELECT user_id, LENGTH(content) FROM crystal_posts
	WHERE LENGTH(content) = (SELECT MAX(LENGTH(content)) FROM crystal_posts))
	SELECT username, email FROM crystal_users
	WHERE id IN (SELECT user_id FROM temp);
	"""
