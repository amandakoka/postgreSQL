import psycopg2

# connect to "chinook" database
connection = psycopg2.connect(
    database="chinook",
    user="postgres",
    password="1234"
)

# build a cursor object of the database
cursor = connection.cursor()

# query 1 - select all records from the "artist" table
# cursor.execute('SELECT * FROM "artist"')

# query 2 - select only the "name" column from "artist" table
# cursor.execute('SELECT "name" FROM "artist"')

# query 3 - select only "queen" from the "artist" table
# cursor.execute('SELECT * FROM "artist" WHERE "name" = %s', ["Queen"])

# query 4 - select only by "artist_id" #51 from the "artist" table
# cursor.execute('SELECT * FROM "artist" WHERE "artist_id" = %s', [51])

# query 5 - select only the albums with "artist_id" #51 on the "album" table
# cursor.execute('SELECT * FROM "album" WHERE "artist_id" = %s', [51])

# query 6 - select all tracks where the composer is "Queen" from the "track" table
cursor.execute('SELECT * FROM "track" WHERE "composer" = %s', ["Queen"])

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the result (single)
# results = cursor.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(result)
