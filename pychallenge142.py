# Using the BookInfo database from program 141,
# display the list of authors and their place of birth.
# Ask the user to enter a place of birth and then show
# the title, date published and author's name for all the
# books by authors who were born in the location they
# selected.

import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

cursor.execute("SELECT * FROM authors")

# Show contents of Author table
print("Here are the Authors currently recorded: ")
author_contents = cursor.fetchall()
for x in author_contents:
    print(x)

# Have user search a location
place_search = str(input("\nEnter location to search: "))

cursor.execute(
    """
                SELECT books.title, books.book_author, books.year_published
                FROM authors,books
                WHERE books.book_author = authors.name
                AND authors.place_of_birth = ?
                """,
    [place_search],
)

place_search_results = cursor.fetchall()

if not place_search_results:
    print(f"{place_search} not found in records.")
else:
    print(f"Here are books published by authors born in {place_search}: \n")
    for x in place_search_results:
        print(x)

cursor.close()
db.close()
