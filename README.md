# Relational database - PostgreSQL

## What I have learnt
1. [PostgreSQL](#postgresql)
   - [Postgresql from command line](#postgresql-from-command-line)
2. [Psycopg2](#psycopg2)
3. [SQlAlchemy](#sqlalchemy)
   - [Middle abstraction layer](#middle-abstraction-layer)
   - [Highest abstraction layer](#highest-abstraction-layer)
4. [Code along CRUD](#code-along---crud)

# PostgreSQL 

PostgreSQL is a free, open source relational database managment system that has powerful features and acts as a primary database for many web/mobile apllications. PostgreSQL is an object-relational database, offering features like table inheritance and function overloading. The postgreSQL server runs as a service and can be used from the command line, through graphical clients, or directly from your own applications.

### [Download PostgreSQL on my mac](https://www.postgresql.org/download/)

## Commands used:

### Download the Chinook PostgreSql database
- `wget https://raw.githubusercontent.com/lerocha/chinook-database/master/ChinookDatabase/DataSources/Chinook_PostgreSql.sql`

### Access the Postgres CLI
- `psql`

### Create the new "chinook" database
- `CREATE DATABASE chinook;`

### View existing tables on the database
- `\l`

### Switch between databases
- `\c postgres` (switch to the database called "postgres")
- `\c chinook` (switch to the database called "chinook")

### Install / Initialize the downloaded Chinook SQL database
- `\i Chinook_PostgreSql.sql`

- - - 

## Postgresql from command line 

### Quit the entire Postgres CLI
- `\q`

### Display all tables on the "chinook" database
- `\dt`

### Quit the query / return back to CLI after a query
- `q`

### Retrieve all data from the "Artist" table
- `SELECT * FROM "Artist";`

### Retrieve only the "Name" column from the "Artist" table
- `SELECT "Name" FROM "Artist";`

### Retrieve only "Queen" from the "Artist" table
- `SELECT * FROM "Artist" WHERE "Name" = 'Queen';`

### Retrieve only "Queen" from the "Artist" table, but using the "ArtistId" of '51'
- `SELECT * FROM "Artist" WHERE "ArtistId" = 51;`

### Retrieve all albums from the "Album" table, using the "ArtistId" of '51'
- `SELECT * FROM "Album" WHERE "ArtistId" = 51;`

### Retrieve all tracks from the "Track" table, using the "Composer" of 'Queen'
- `SELECT * FROM "Track" WHERE "Composer" = 'Queen';`

- - - 

# Psycopg2

Psycopg2 is a python package and data adapter where you can run Postgres commands from Python code, instead of the CLI - Use the psycopg2 library and it's inbuilt methods.

### Install the "psycopg2" Python package
- `pip3 install psycopg2`

- - - 

# SQlAlchemy

SQLAlchemy is an object-relational mapper, it bridges the gap between python objects and postgres tables - Query and manipulate a database using Python, instead of raw SQL commands.

### Install the "SQLAlchemy" Python package
- `pip3 install SQLAlchemy`
- `pip3 install sqlalchemy==1.4.46`

- - - 

## Middle abstraction layer

Running basic queries- SQLAlchemy's middle abstraction layer, the Expression Language, simplifies queries to the database using tables - connect Python and the SQLAlchemy library to the database, using cleaner code.

### Query 1 - select all records from the "Artist" table
- `select_query = artist_table.select()`

### Query 2 - select only the "Name" column from the "Artist" table
- `select_query = artist_table.select().with_only_columns([artist_table.c.Name])`

### Query 3 - select only 'Queen' from the "Artist" table
- `select_query = artist_table.select().where(artist_table.c.Name == "Queen")`

### Query 4 - select only by 'ArtistId' #51 from the "Artist" table
- `select_query = artist_table.select().where(artist_table.c.ArtistId == 51)`

### Query 5 - select only the albums with 'ArtistId' #51 on the "Album" table
- `select_query = album_table.select().where(album_table.c.ArtistId == 51)`

### Query 6 - select all tracks where the composer is 'Queen' from the "Track" table
- `select_query = track_table.select().where(track_table.c.Composer == "Queen")`

- - - 

## Highest abstraction layer

Introducing class-based models- SQLAlchemy's highest abstraction layer, the ORM - Simplifies queries to the database using class-based objects - Connect Python and the SQLAlchemy library to the database, using cleaner code.

Class - collection of methods that serve a common purpose, with each method having its own purpose.

.connect .select .execute - methods have specific duty. 
Using class-based models - can reuse methods throughout application without repeating yourself.

### Query 1 - select all records from the "Artist" table
```python
artists = session.query(Artist)
for artist in artists:
    print(artist.ArtistId, artist.Name, sep=" | ")
```

### Query 2 - select only the "Name" column from the "Artist" table
```python
artists = session.query(Artist)
for artist in artists:
    print(artist.Name)
```

### Query 3 - select only "Queen" from the "Artist" table
```python
artist = session.query(Artist).filter_by(Name="Queen").first()
print(artist.ArtistId, artist.Name, sep=" | ")
```

### Query 4 - select only by "ArtistId" #51 from the "Artist" table
```python
artist = session.query(Artist).filter_by(ArtistId=51).first()
print(artist.ArtistId, artist.Name, sep=" | ")
```

### Query 5 - select only the albums with "ArtistId" #51 on the "Album" table
```python
albums = session.query(Album).filter_by(ArtistId=51)
for album in albums:
    print(album.AlbumId, album.Title, album.ArtistId, sep=" | ")
```

### Query 6 - select all tracks where the composer is "Queen" from the "Track" table
```python
tracks = session.query(Track).filter_by(Composer="Queen")
for track in tracks:
    print(
        track.TrackId,
        track.Name,
        track.AlbumId,
        track.MediaTypeId,
        track.GenreId,
        track.Composer,
        track.Milliseconds,
        track.Bytes,
        track.UnitPrice,
        sep=" | "
    )
```

- - - 

# Code along - CRUD 

- C - CREATE 
- R - READ 
- U - UPDATE
- D - DELETE

## Code-along 1: Create and read
Building class-based models to Create and Read data on your Postgres Database. Allows us to define custom tables to add and retrieve records using the ORM. Extending the ORM declarative_base to generate new tables and records.

## Code-Along 2: Update and Delete
Using class-based models to Update and Delete data on your Postgres Database. Allows us to retrieve records in order to make necessary updates, or entirely delete them from the database. Securely accessing our database to properly manipulate data, or to delete data.

