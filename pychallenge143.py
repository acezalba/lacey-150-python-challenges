# Using the BookInfo database, ask the user to
# enter a year and display all the books published
# after that year, sorted by the year
# they were published.

import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

year_search = int(input("Enter year to search: "))

cursor.execute(
    """
                SELECT title, year_published
                FROM books
                WHERE books.year_published>?
                ORDER BY books.year_published
                """,
    [year_search],
)

results = cursor.fetchall()

if not results:
    print(f"No books in record were published after {year_search}.")
else:
    print(f"Here are the books on record published after {year_search}:")
    for x in results:
        print(x)

db.close()
