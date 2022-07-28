import sqlite3

con = sqlite3.connect('scoreFile.db')
cur = con.cursor()
##creates a table called scores
cur.execute("CREATE TABLE IF NOT EXISTS scores (score INTEGER, date_posted TEXT, user TEXT)")
##inserts a score into the table
# cur.execute("INSERT INTO scores VALUES (100, '2020-12-12', 'user')")
# cur.execute("INSERT INTO scores VALUES (200, '2020-12-12', 'user2')")
# con.commit()

def get_score():
    con = sqlite3.connect('scoreFile.db')
    cur = con.cursor()
##prints the table
    for row in cur.execute("SELECT * FROM scores ORDER by score"):
        print(row)
    con.close()

def get_high_score():
    con = sqlite3.connect('scoreFile.db')
    cur = con.cursor()
    cur.execute("SELECT MAX(score) FROM scores")
    high_score = cur.fetchone()
    print(high_score)
    con.close()

def get_low_score():
    con = sqlite3.connect('scoreFile.db')
    cur = con.cursor()
    cur.execute("SELECT MIN(score) FROM scores")
    low_score = cur.fetchone()
    print(low_score)
    con.close()

def commit_a_score(score, date, user):
    con = sqlite3.connect('scoreFile.db')
    cur = con.cursor()
    cur.execute("INSERT INTO scores VALUES (?, ?, ?)", (score, str(date), user))
    con.commit()
    con.close()

def get_user_score(user):
    con = sqlite3.connect('scoreFile.db')
    cur = con.cursor()
    cur.execute("SELECT score FROM scores WHERE user = ?", (user,))
    user_score = cur.fetchone()
    print(user_score)
    con.close()

def get_score_date(date):
    con = sqlite3.connect('scoreFile.db')
    cur = con.cursor()
    cur.execute("SELECT score FROM scores WHERE date_posted = ?", (str(date),))
    date_score = cur.fetchone()
    print(date_score)
    con.close()
# def del_score(score):
#     cur.execute("DELETE FROM scores WHERE score = ?", (score,))
#     con.commit()

# def del_user(user):
#     cur.execute("DELETE FROM scores WHERE user = ?", (user,))
#     con.commit()

con.close()