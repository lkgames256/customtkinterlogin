import sqlite3
import hashlib

conn = sqlite3.connect("../userdata.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS userdata(
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)
""")

[insert login data from D:/customtkinter.txt]
cur.execute("INSERT INTO userdata (username, password) VALUES (?,?)", (username1, password1))
cur.execute("INSERT INTO userdata (username, password) VALUES (?,?)", (username2, password2))
cur.execute("INSERT INTO userdata (username, password) VALUES (?,?)", (username3, password3))
cur.execute("INSERT INTO userdata (username, password) VALUES (?,?)", (username4, password4))
cur.execute("INSERT INTO userdata (username, password) VALUES (?,?)", (username5, password5))

conn.commit()
