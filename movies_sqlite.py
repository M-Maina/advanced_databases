import sqlite3

connection = sqlite3.connect('movies.db')

cursor = connection.cursor()

# cursor.execute("INSERT INTO Movies VALUES ('Taxi Driver', 'Martin Scorsese', 1979)")

cursor.execute("select * from Movies")

famousFilms = [('pulp Fiction', 'Quentin Tarantino', 1994),
               ('Back to the future', 'Steven Spielberg', 1985),
               ('Moonrise kingdom', 'Wes Anderson', 2012)]

print(cursor.fetchone())

connection.commit()
connection.close()