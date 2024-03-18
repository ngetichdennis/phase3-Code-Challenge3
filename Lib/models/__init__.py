import sqlite3

CONN = sqlite3.connect('eatery.db')
CURSOR = CONN.cursor()