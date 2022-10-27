# Create a SQL database called Phonebook that contains
# a table called names with the following data: ...

import sqlite3

with sqlite3.connect("PhoneBook.db") as db:
    cursor = db.cursor()

cursor.execute(
    """ 
               CREATE TABLE IF NOT EXISTS Names(
                   id integer PRIMARY KEY,
                   first_name text NOT NULL,
                   surname text NOT NULL,
                   phone_number varchar(15)
               )
               """
)
cursor.execute(
    """
               INSERT INTO Names(id,first_name,surname,phone_number)
               VALUES
                   ("1", "Simon", "Howels", "01223349752"),
                   ("2", "Karen", "Phillips", "01954295773"),
                   ("3", "Darren", "Smith", "01583749012"),
                   ("4", "Anne", "Jones", "01323567322"),
                   ("5", "Mark", "Smith", "01223855534");
              """
)
db.commit()
db.close()
