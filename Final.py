import psycopg2

class Queries():
    """
    Please submit this file on gradescope.
    Questions will appear when you submit to gradescope, there is no pentalty for resubmitting on gradescope.
    It is advised to copy paste the question you see when you submit on gradescope under each function name in case you need the question offline
    Put your solutions on the line following the line that starts with 'return' for each question
    """

    def q1(self):
	"""Q1: We will be working with 4 different tables. Their name and schemas are as follows:

crystal_channel, the columns of the table should be the following:
	id should be type integer
	username should be type character varying
	password should be type character varying
	email should be type character varying
	join_date should be type date
This table should have 5 rows.

crystal_videos, the columns of the table should be the following:
	id should be type integer
	title should be type character varying
	channel_id should be type integer
This table should have 5 rows.

crystal_comments, the columns of the table should be the following:
	id should be type integer
	video_id should be type integer
	comment should be type text
This table should have 5 rows.

crystal_likes, the columns of the table should be the following:
	video_id should be type integer
	liked should be type boolean
This table should have 5 rows.

Note: Treat manager_id as a FK to employees(id). DO NOT form a FK on this pairing.Generate 4 queries to create these tables (table names should be all lower case).
All VARCHARs should be at minimum length 20.
Primary keys and Foreign keys should be included in your query.


Detail on crystal_likes's liked field: This should be TRUE if the video was liked, otherwise False to indicate a dislike.
Insert rows into your tables!
Restrictions:
	Create a channel for yourself! More specifically insert exactly 1 row with:
		first_name: riva
		last_name: crystal
		email: riva.crystal92@myhunter.cuny.edu
		join_date: Today's date in form yyyy-mm-dd

For all other questions, submit any incorrect query to see the question.
Note: Rows will be inserted on top of what you have inserted for Q1!"""
	return """
	create table crystal_channel(
	id serial primary key,
	username varchar(50),
	password varchar(50),
	email varchar(50),
	join_date date
	);

	insert into crystal_channel (username, password, email, join_date)
	values ('riva', 'crystal', 'riva.crystal92@myhunter.cuny.edu', '2022-05-18'),
	('sdfsda', 'afewoj', 'woefjo@gmail.com', '2022-05-17'),
	('SWFLJLASF', 'WOEFJOJIASFD', 'AOSDFIJA', '2022-05-16'),
	('sdfojas', 'owejfjddas', 'woefijoas@gmail.com', '2022-05-15'),
	('sdfdsa', 'sofijoa', 'asodfo@gmail.com', '2022-05-14')
	;

	create table crystal_videos(
	id serial primary key,
	title varchar(50),
	channel_id integer references crystal_channel (id)
	);

	insert into crystal_videos (title, channel_id)
	values ('asdfjosja', 1),
	('sadfioa', 2),
	('ASDFLA', 3),
	('aoalsfda', 4),
	('asldfjoa', 5)
	;

	create table crystal_comments(
	id serial primary key,
	video_id integer references crystal_videos (id),
	comment text
	);

	insert into crystal_comments (video_id, comment)
	values (1, 'asolfjoa'),
	(2, 'adsofjoa'),
	(3, 'ASDFAS'),
	(4, 'asdfjoa'),
	(5, 'saldfjoldsa')
	;

	create table crystal_likes(
	video_id integer references crystal_videos (id),
	liked boolean
	);

	insert into crystal_likes (video_id, liked)
	values (1, true),
	(2, true),
	(3, true),
	(4, true),
	(5, false)
	;
	"""

    def q2(self):
	"""Lets pull some simple historical data.
	Write a query that will return a list of join date months and the amount of channels joined on that month.
	NOTE: Provide the month number!
	Example row: (1, 10) -> 10 people joined in Jan."""
	return """
	SELECT EXTRACT(month FROM join_date), COUNT(join_date) FROM crystal_channel GROUP BY EXTRACT(month from join_date);
	"""

    def q3(self):
	"""Get the email,username of channels that have at least 1 video with between 1 - 6 likes."""
	return """
with temp as (select video_id, count(case when liked then 1 end), coalesce(video_id) from crystal_likes group by video_id having count(case when liked then 1 end) between 1 and 6) select email, username from crystal_channel join crystal_videos on crystal_channel.id = crystal_videos.channel_id where crystal_videos.id in (select video_id from temp);
	"""
    
    def q4(self):
	"""Write a query to pull the username of any channel that has NOT uploaded a video.
	We only want to consider users where their password is exactly 6 characters long."""
	return """
	SELECT username FROM crystal_channel
	JOIN crystal_videos on crystal_channel.id = crystal_videos.channel_id
	WHERE crystal_videos.id IS NULL AND crystal_channel.password like '______';
	"""

    def q5(self):
	"""Generate a list of username,password,email,join_date where the password meets the following criteria:
	The password is exactly 32 characters long.
	The character at index 8 of password is s
	The character at index 0 of password is r
	The character at index 0 of password is r
	The channel's id is even
	The channel has just joined today!
	Note: Indexes start at 0! (Index 0 is the first character)
	Hint: A number is even if you modulo(%) that number and it returns 0, otherwise it produces a 1 and is odd.
	"""
	return """
	SELECT username, password, email, join_date from crystal_channel
	where length(password) = 32
	and password like 'r_______r'
	and id % 2 = 1
	and join_date = '2022-05-18';
	"""

    def q6(self):
	"""We have seen a lot of 'click bait titles' for videos.
	We want to gather some more information on what's the most popular title.
	Generate a list of phrase,amount of titles that use the same phrase within {}.
	NOTE:Phrases (strings within the {}) must be length of 16.
	Example: {apple} -> The phrase here is apple.
	Only consider titles where you can find a pair of {}.
	Note: Assume there will only be one pair of {} in a title."""
	return """
	"""

    def q7(self):
	"""QUESTION:
	Return the title,and the length of the shortest comment attached to that video."""
	return """
	SELECT title, length(comment) from crystal_videos
    join crystal_comments on crystal_comments.video_id = crystal_videos.id
    where length(comment) = (select min(length(comment)) from crystal_comments);
	"""

    def q8(self):
	"""Return a list of email,title,liked with the following conditions:
	There should be a row for each individual instance of a like.
	If there is no likes print the text 'MISSING LIKE' (case sen.).
	The liked value should be printed out as a string.
	If there is no associated video for a channel, the video attributes should be NULL.
	You can cast a boolean value to a string by doing the follow:
	CAST(<attribute> AS text)
	Example: SELECT CAST(true AS text); Will produce 'true'.
	"""
	return """
	select email, title, cast(liked as text),
	case when liked is null then 'MISSING LIKE' end
	from crystal_channel
	join crystal_videos on crystal_channel.id = crystal_videos.channel_id
	join crystal_likes on crystal_videos.id = crystal_likes.video_id;
	"""

    def q9(self):
	"""Return a list of the amount of videos, and the id of channels that have posted the least videos.
	Do not include any channels that did not post any videos.
	Sort and reduce the list to size 1.
	"""
	return """
	SELECT count(crystal_videos.id), crystal_channel.id from crystal_videos
	join crystal_channel on crystal_videos.channel_id = crystal_channel.id
	group by crystal_channel.id
	order by count(crystal_videos.id) limit 2;
	"""