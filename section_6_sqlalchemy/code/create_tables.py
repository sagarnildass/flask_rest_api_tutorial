import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

#INTEGER PRIMARY KEY makes it autogenerate new ids sequentially
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

#real is decimal
create_table = "CREATE TABLE IF NOT EXISTS items (name text, price real)"
cursor.execute(create_table)

#cursor.execute("INSERT INTO items VALUES ('test', 10.99)")

connection.commit()
connection.close()
