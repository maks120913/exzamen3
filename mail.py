import sqlite3

connection = sqlite3.connect("itstep_DB.sl3", 5)
cur = connection.cursor()

cur.execute("INSERT INTO employees (name, position, salary) VALUES ('Діана', 'мененджер', 9500);")
cur.execute("INSERT INTO employees (name, position, salary) VALUES ('Макс', 'мененджер', 6500);")
cur.execute("INSERT INTO employees (name, position, salary) VALUES ('Надя', 'мененджер', 6000);")

connection.commit()

print(connection)
print(cur)

connection.close()
