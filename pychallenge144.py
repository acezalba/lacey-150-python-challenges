import sqlite3
import os

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

# Ask user for author to export
author_search = str(input("Enter author to export data to textfile: "))

# Query database
search_results = cursor.execute(
    """
                 SELECT books.id, books.title, books.book_author, books.year_published
                 FROM books
                 WHERE books.book_author = ?
                 """,
    [author_search],
)

if not search_results:
    print(f"{author_search} not found in records.")
else:
    # Export results to textfile
    filename = f"{author_search}.txt"
    with open(filename, "w") as f:
        for x in search_results:
            new_string = ""
            for index, value in enumerate(x):
                if index == len(x) - 1:
                    new_string = new_string + str(value) + "\n"
                else:
                    new_string = new_string + str(value) + " - "
            f.writelines(new_string)

    print(f"Results exported to {filename}.")

db.close
