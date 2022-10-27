# Create a new SQL database called BookInfo that will store
# a list of authors and the books they wrote. It will have two tables.
# The first one should be called Authors and contain the following
# data. The second one should be called Books and contain the following
# data.

import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

# Create table Authors
cursor.execute(
    """
                CREATE TABLE IF NOT EXISTS authors(
                    name text NOT NULL,
                    place_of_birth text NOT NULL
                )
                """
)

# Populate Authors table
cursor.execute(
    """
                INSERT INTO authors(name, place_of_birth)
                VALUES
                    ("Agatha Christie", "Torquay"),
                    ("Cecelia Ahern", "Dublin"),
                    ("J.K. Rowling", "Bristol"),
                    ("Oscar Wilde", "Dublin");
                """
)

# Create table BookInfo
cursor.execute(
    """
                CREATE TABLE IF NOT EXISTS books(
                    id integer PRIMARY KEY,
                    title text NOT NULL,
                    book_author text NOT NULL,
                    year_published integer NOT NULL
                );
                """
)

# Populate table BookInfo
cursor.execute(
    """
                INSERT INTO books(id, title, book_author, year_published)
                VALUES
                    ("1", "De Profundis", "Oscar Wilde", "1905"),
                    ("2", "Harry Potter and the Chamber of Secrets", "J.K. Rowling", "1998"),
                    ("3", "Harry Potter and the Prisoner of Azkaban", "J.K. Rowling", "1999"),
                    ("4", "Lyrebird", "Cecelia Ahern", "2017"),
                    ("5", "Murder on the Orient Express", "Agatha Christie", "1934"),
                    ("6", "Perfect", "Cecelia Ahern", "2017"),
                    ("7", "The Marble Collector", "Cecelia Ahern", "2016"),
                    ("8", "The Murder on the Links", "Agatha Christie", "1923"),
                    ("9", "The Picture of Dorian Gray", "Oscar Wilde", "1890"),
                    ("10", "The Secret Adversary", "Agatha Christie", "1921"),
                    ("11", "The Seven Dials Mystery", "Agatha Christie", "1929"),
                    ("12", "The Year I Met You", "Cecelia Ahern", "2014");
                """
)

db.commit()
db.close()
