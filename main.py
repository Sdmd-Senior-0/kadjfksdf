import sqlite3

db = sqlite3.connect('main.db')

c = db.cursor()
c.execute("SELECT rowid, title FROM articles")
print(c.fetchmany(1)[0][1])

db.commit()

db.close()