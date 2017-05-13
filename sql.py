# sql.py- Script to create db and populate with data

import sqlite3

#creates a new db if it doesn't already exist

with sqlite3.connect("blog.db") as connection:

    #get a cursor obj used to execute SQL commands
    c = connection.cursor()

    #create the table
    c.execute("""CREATE TABLE posts (title TEXT, post TEXT)""")

    #insert some dummies into TABLE
    c.execute('INSERT INTO posts VALUES("Good", "I\'m good.")')
    c.execute('INSERT INTO posts VALUES("Well", "I\'m well.")')
    c.execute('INSERT INTO posts VALUES("Excellent", "I\'m excellent.")')
    c.execute('INSERT INTO posts VALUES("Okay", "I\'m okay.")')
    c.execute('INSERT INTO posts VALUES("Awesome", "I\'m awesome.")')

    
