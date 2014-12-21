import sqlite3


# Create new database symtable

with sqlite3.connect("blog.db") as connection:
	c=connection.cursor()
	c.execute(""" CREATE TABLE posts (title TEXT, post TEXT)""")
	c.execute('INSERT INTO posts VALUES("Good","I\'m good.")')
	c.execute('INSERT INTO posts VALUES("Well","I\'m good.")')
	c.execute('INSERT INTO posts VALUES("Excellent", "I\'mexcellent.")')
	c.execute('INSERT INTO posts VALUES("Okay", "I\'m okay.")')

