'''
Created on 2018/03/20

@author: miyazawataishi
'''
import sqlite3

dbpath = "test.sqlite"
conn = sqlite3.connect(dbpath)

cur = conn.cursor()
cur.executescript("""
DROP TABLE IF EXISTS items;

CREATE TABLE items(
    item_id INTEGER PRIMARY KEY,
    name TEXT UNIQUE,
    price INTEGER
);

INSERT INTO items(name, price)VALUES('Apple', 800);
INSERT INTO items(name, price)VALUES('Meron', 200);
INSERT INTO items(name, price)VALUES('Grape', 300);
""")

conn.commit()

cur = conn.cursor()
cur.execute("SELECT item_id, name, price FROM items")
item_list = cur.fetchall()

for it in item_list:
    print(it)
