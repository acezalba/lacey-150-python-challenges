# /usr/bin/env python3
"""
Art Gallery
"""

import sqlite3, os
from tkinter import *
from tkinter import ttk


def create_tables():
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS artists(
      artist_id integer PRIMARY KEY,
      name text NOT NULL,
      address text NOT NULL,
      town text,
      county text NOT NULL,
      postcode text NOT NULL
    )
                 """
    )

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS art_pieces(
      piece_id integer PRIMARY KEY,
      artist_id integer NOT NULL,
      title text NOT NULL,
      medium text NOT NULL,
      price integer NOT NULL,
      sold text NOT NULL
    )
                """
    )


def load_demo():
    cursor.execute(
        """
    INSERT OR REPLACE INTO artists(artist_id, name, address, town, county, postcode)
    VALUES
      ("1", "Martin Leighton", "5 Park Place", "Peterborough", "Cambridgeshire", "PE32 5LP"),
      ("2", "Eva Czarniecka", "77 Warner Close", "Chelmsford", "Essex", "CM22 5FT"),
      ("3", "Roxy Parkin", "90 Windhead Road", "", "London", "SE12 6WM"),
      ("4", "Nigel Farnworth", "41 Whitby Road", "Huntly", "Aberdeenshire", "AB54 5PN"),
      ("5", "Teresa Tanner", "70 Guild Street", "","London", "NW7 1SP")
                 """
    )

    cursor.execute(
        """
    INSERT OR REPLACE INTO art_pieces(piece_id, artist_id, title, medium, price, sold)
    VALUES
      ("1",  "5", "Woman with black Labrador", "Oil", "220", "No"),
      ("2",  "5", "Bees & thistles", "Watercolour", "85", "No"),
      ("3",  "2", "A stroll to Westminster", "Ink", "190", "No"),
      ("4",  "1", "African giant", "Oil", "800", "No"),
      ("5",  "3", "Water daemon",  "Acrylic", "1700", "No"),
      ("6",  "4", "A seagull", "Watercolour", "35", "No"),
      ("7",  "1", "Three friends", "Oil", "1800", "No"),
      ("8",  "2", "Summer breeze 1", "Acrylic", "1350", "No"),
      ("9",  "4", "Mr. Hamster", "Watercolour", "35", "No"),
      ("10", "1", "Pulpit Rock, Dorset", "Oil", "600", "No"),
      ("11", "5", "Trawler Dungeness Beach", "Oil", "195", "No"),
      ("12", "2", "Dance in the snow", "Oil", "250", "No"),
      ("13", "4", "St. Tropez Port", "Ink", "45", "No"),
      ("14", "3", "Pirate Assassin", "Acrylic", "420", "No"),
      ("15", "1", "Morning walk",  "Oil", "800", "No"),
      ("16", "4", "A baby barn swallow", "Watercolour", "35", "No"),
      ("17", "4", "The old working mills", "Ink", "395", "No")
                 """
    )
    reload_views()


def reload_views():
    db.commit()
    view_artists()
    view_art_pieces()


def add_artist():
    def add_artist_db():
        cursor.execute("SELECT artist_id FROM artists ORDER BY artist_id DESC limit 1")
        temp = cursor.fetchone()
        new_id = int(temp[0])
        new_id = new_id + 1
        new_name = entry_name.get()
        new_address = entry_address.get()
        new_town = entry_town.get()
        new_county = entry_county.get()
        new_postcode = entry_postcode.get()

        cursor.execute(
            """
    INSERT INTO artists(artist_id, name, address, town, county, postcode)
    VALUES
      (?,?,?,?,?,?)
                   """,
            [new_id, new_name, new_address, new_town, new_county, new_postcode],
        )

        reload_views()

    window_add_artist = Tk()
    window_add_artist.title("Add Artist")
    window_add_artist.minsize(200, 150)
    window_add_artist.resizable(0, 0)
    window_add_artist.columnconfigure(0, weight=1)
    window_add_artist.rowconfigure(0, weight=1)

    frame_prompt = ttk.Frame(window_add_artist, padding=8)
    frame_prompt.grid(column=0, row=0, sticky="NSEW")
    window_add_artist.columnconfigure(0, weight=1)
    window_add_artist.rowconfigure(0, weight=1)
    frame_prompt["borderwidth"] = 4
    frame_prompt["relief"] = "solid"

    label_name = Label(frame_prompt, text="Name: ")
    label_name.grid(column=0, row=0)
    entry_name = Entry(frame_prompt)
    entry_name.grid(column=1, row=0, sticky="NSEW")

    label_address = Label(frame_prompt, text="Address: ")
    label_address.grid(column=0, row=1)
    entry_address = Entry(frame_prompt)
    entry_address.grid(column=1, row=1, sticky="NSEW")

    label_town = Label(frame_prompt, text="Town: ")
    label_town.grid(column=0, row=2)
    entry_town = Entry(frame_prompt)
    entry_town.grid(column=1, row=2, sticky="NSEW")

    label_county = Label(frame_prompt, text="County: ")
    label_county.grid(column=0, row=3)
    entry_county = Entry(frame_prompt)
    entry_county.grid(column=1, row=3, sticky="NSEW")

    label_postcode = Label(frame_prompt, text="Post Code: ")
    label_postcode.grid(column=0, row=4)
    entry_postcode = Entry(frame_prompt)
    entry_postcode.grid(column=1, row=4, sticky="NSEW")

    button_add = Button(frame_prompt, text="Add", command=add_artist_db)
    button_add.grid(column=0, row=5, columnspan=2, sticky="NSEW")

    window_add_artist.mainloop()


def update_artist():
    def update_artist_db():
        update_id = entry_id.get()
        update_name = entry_name.get()
        update_address = entry_address.get()
        update_town = entry_town.get()
        update_county = entry_county.get()
        update_postcode = entry_postcode.get()

        cursor.execute(
            """
    UPDATE artists
    SET
      name = ?,
      address = ?, 
      town = ?, 
      county = ?,
      postcode = ?
    WHERE
      artist_id = ?
                   """,
            [
                update_name,
                update_address,
                update_town,
                update_county,
                update_postcode,
                update_id,
            ],
        )

        reload_views()

    window_update_artist = Tk()
    window_update_artist.title("Update Artist")
    window_update_artist.minsize(200, 150)
    window_update_artist.resizable(0, 0)
    window_update_artist.columnconfigure(0, weight=1)
    window_update_artist.rowconfigure(0, weight=1)

    frame_prompt = ttk.Frame(window_update_artist, padding=8)
    frame_prompt.grid(column=0, row=0, sticky="NSEW")
    window_update_artist.columnconfigure(0, weight=1)
    window_update_artist.rowconfigure(0, weight=1)
    frame_prompt["borderwidth"] = 4
    frame_prompt["relief"] = "solid"

    label_id = Label(frame_prompt, text="ID: ")
    label_id.grid(column=0, row=0)
    entry_id = Entry(frame_prompt)
    entry_id.grid(column=1, row=0, sticky="NSEW")

    label_name = Label(frame_prompt, text="Name: ")
    label_name.grid(column=0, row=1)
    entry_name = Entry(frame_prompt)
    entry_name.grid(column=1, row=1, sticky="NSEW")

    label_name = Label(frame_prompt, text="Name: ")
    label_name.grid(column=0, row=1)
    entry_name = Entry(frame_prompt)
    entry_name.grid(column=1, row=1, sticky="NSEW")

    label_address = Label(frame_prompt, text="Address: ")
    label_address.grid(column=0, row=2)
    entry_address = Entry(frame_prompt)
    entry_address.grid(column=1, row=2, sticky="NSEW")

    label_town = Label(frame_prompt, text="Town: ")
    label_town.grid(column=0, row=3)
    entry_town = Entry(frame_prompt)
    entry_town.grid(column=1, row=3, sticky="NSEW")

    label_county = Label(frame_prompt, text="County: ")
    label_county.grid(column=0, row=4)
    entry_county = Entry(frame_prompt)
    entry_county.grid(column=1, row=4, sticky="NSEW")

    label_postcode = Label(frame_prompt, text="Post Code: ")
    label_postcode.grid(column=0, row=5)
    entry_postcode = Entry(frame_prompt)
    entry_postcode.grid(column=1, row=5, sticky="NSEW")

    button_add = Button(frame_prompt, text="Update", command=update_artist_db)
    button_add.grid(column=0, row=6, columnspan=2, sticky="NSEW")

    window_update_artist.mainloop()


def delete_artist():
    def delete_artist_db():
        delete_id = entry_id.get()

        cursor.execute(
            """
    DELETE FROM artists
    WHERE
      artist_id = ?
                   """,
            [delete_id],
        )

        reload_views()

    window_delete_artist = Tk()
    window_delete_artist.title("Delete Artist")
    window_delete_artist.minsize(230, 50)
    window_delete_artist.resizable(0, 0)
    window_delete_artist.columnconfigure(0, weight=1)
    window_delete_artist.rowconfigure(0, weight=1)

    frame_prompt = ttk.Frame(window_delete_artist, padding=8)
    frame_prompt.grid(column=0, row=0, sticky="NSEW")
    window_delete_artist.columnconfigure(0, weight=2)
    window_delete_artist.rowconfigure(0, weight=2)
    frame_prompt["borderwidth"] = 4
    frame_prompt["relief"] = "solid"

    label_id = Label(frame_prompt, text="ID: ")
    label_id.grid(column=0, row=0)
    entry_id = Entry(frame_prompt)
    entry_id.grid(column=1, row=0, sticky="NSEW")

    button_add = Button(frame_prompt, text="Delete", command=delete_artist_db)
    button_add.grid(column=0, row=1, columnspan=2, sticky="NSEW")

    window_delete_artist.mainloop()


def add_art():
    def add_art_db():
        cursor.execute("SELECT piece_id FROM art_pieces ORDER BY piece_id DESC limit 1")
        temp = cursor.fetchone()
        new_id = int(temp[0])
        new_id = new_id + 1
        new_artist_id = entry_artist_id.get()
        new_title = entry_title.get()
        new_medium = entry_medium.get()
        new_price = entry_price.get()
        new_sold = entry_sold.get()

        cursor.execute(
            """
    INSERT INTO art_pieces(piece_id, artist_id, title, medium, price, sold)
    VALUES
      (?,?,?,?,?,?)
                   """,
            [new_id, new_artist_id, new_title, new_medium, new_price, new_sold],
        )

        reload_views()

    window_add_art = Tk()
    window_add_art.title("Add Art")
    window_add_art.minsize(200, 150)
    window_add_art.resizable(0, 0)
    window_add_art.columnconfigure(0, weight=1)
    window_add_art.rowconfigure(0, weight=1)

    frame_prompt = ttk.Frame(window_add_art, padding=8)
    frame_prompt.grid(column=0, row=0, sticky="NSEW")
    window_add_art.columnconfigure(0, weight=1)
    window_add_art.rowconfigure(0, weight=1)
    frame_prompt["borderwidth"] = 4
    frame_prompt["relief"] = "solid"

    label_artist_id = Label(frame_prompt, text="Artist ID: ")
    label_artist_id.grid(column=0, row=0)
    entry_artist_id = Entry(frame_prompt)
    entry_artist_id.grid(column=1, row=0, sticky="NSEW")

    label_title = Label(frame_prompt, text="Title: ")
    label_title.grid(column=0, row=1)
    entry_title = Entry(frame_prompt)
    entry_title.grid(column=1, row=1, sticky="NSEW")

    label_medium = Label(frame_prompt, text="Medium: ")
    label_medium.grid(column=0, row=2)
    entry_medium = Entry(frame_prompt)
    entry_medium.grid(column=1, row=2, sticky="NSEW")

    label_price = Label(frame_prompt, text="Price: ")
    label_price.grid(column=0, row=3)
    entry_price = Entry(frame_prompt)
    entry_price.grid(column=1, row=3, sticky="NSEW")

    label_sold = Label(frame_prompt, text="Sold? ")
    label_sold.grid(column=0, row=4)
    entry_sold = Entry(frame_prompt)
    entry_sold.grid(column=1, row=4, sticky="NSEW")

    button_add = Button(frame_prompt, text="Add", command=add_art_db)
    button_add.grid(column=0, row=5, columnspan=2, sticky="NSEW")

    window_add_art.mainloop()


def update_art():
    def update_art_db():
        update_id = entry_id.get()
        update_artist_id = entry_artist_id.get()
        update_title = entry_title.get()
        update_medium = entry_medium.get()
        update_price = entry_price.get()
        update_sold = entry_sold.get()

        cursor.execute(
            """
    UPDATE art_pieces
    SET
      artist_id = ?, 
      title = ?, 
      medium = ?,
      price = ?,
      sold = ?
    WHERE
      piece_id = ?
                   """,
            [
                update_artist_id,
                update_title,
                update_medium,
                update_price,
                update_sold,
                update_id,
            ],
        )

        reload_views()

    window_update_art = Tk()
    window_update_art.title("Update Artist")
    window_update_art.minsize(280, 180)
    window_update_art.resizable(0, 0)
    window_update_art.columnconfigure(0, weight=1)
    window_update_art.rowconfigure(0, weight=1)

    frame_prompt = ttk.Frame(window_update_art, padding=8)
    frame_prompt.grid(column=0, row=0, sticky="NSEW")
    window_update_art.columnconfigure(0, weight=1)
    window_update_art.rowconfigure(0, weight=1)
    frame_prompt["borderwidth"] = 4
    frame_prompt["relief"] = "solid"

    label_id = Label(frame_prompt, text="ID: ")
    label_id.grid(column=0, row=0)
    entry_id = Entry(frame_prompt)
    entry_id.grid(column=1, row=0, sticky="NSEW")

    label_artist_id = Label(frame_prompt, text="Artist ID: ")
    label_artist_id.grid(column=0, row=1)
    entry_artist_id = Entry(frame_prompt)
    entry_artist_id.grid(column=1, row=1, sticky="NSEW")

    label_title = Label(frame_prompt, text="Title: ")
    label_title.grid(column=0, row=2)
    entry_title = Entry(frame_prompt)
    entry_title.grid(column=1, row=2, sticky="NSEW")

    label_medium = Label(frame_prompt, text="Medium: ")
    label_medium.grid(column=0, row=3)
    entry_medium = Entry(frame_prompt)
    entry_medium.grid(column=1, row=3, sticky="NSEW")

    label_price = Label(frame_prompt, text="Price: ")
    label_price.grid(column=0, row=4)
    entry_price = Entry(frame_prompt)
    entry_price.grid(column=1, row=4, sticky="NSEW")

    label_sold = Label(frame_prompt, text="Sold? ")
    label_sold.grid(column=0, row=5)
    entry_sold = Entry(frame_prompt)
    entry_sold.grid(column=1, row=5, sticky="NSEW")

    button_update = Button(frame_prompt, text="Update", command=update_art_db)
    button_update.grid(column=0, row=6, columnspan=2, sticky="NSEW")

    window_update_art.mainloop()


def delete_art():
    def delete_art_db():
        delete_id = entry_id.get()

        cursor.execute(
            """
    DELETE FROM art_pieces
    WHERE
      piece_id = ?
                   """,
            [delete_id],
        )

        reload_views()

    window_delete_art = Tk()
    window_delete_art.title("Delete Artist")
    window_delete_art.minsize(230, 50)
    window_delete_art.resizable(0, 0)
    window_delete_art.columnconfigure(0, weight=1)
    window_delete_art.rowconfigure(0, weight=1)

    frame_prompt = ttk.Frame(window_delete_art, padding=8)
    frame_prompt.grid(column=0, row=0, sticky="NSEW")
    window_delete_art.columnconfigure(0, weight=2)
    window_delete_art.rowconfigure(0, weight=2)
    frame_prompt["borderwidth"] = 4
    frame_prompt["relief"] = "solid"

    label_id = Label(frame_prompt, text="Piece ID: ")
    label_id.grid(column=0, row=0)
    entry_id = Entry(frame_prompt)
    entry_id.grid(column=1, row=0, sticky="NSEW")

    button_delete = Button(frame_prompt, text="Delete", command=delete_art_db)
    button_delete.grid(column=0, row=1, columnspan=2, sticky="NSEW")

    window_delete_art.mainloop()


def search_by_artist():
    def search_by_artist_db():
        artist_id_search = entry_artist_id.get()
        cursor.execute(
            """
      SELECT * FROM art_pieces
      WHERE
        artist_id = ?
                  """,
            artist_id_search,
        )

        search_results = cursor.fetchall()

        view_search_art_pieces(search_results)

    window_search_by_artist = Tk()
    window_search_by_artist.title("Search by Artist")
    window_search_by_artist.minsize(200, 150)
    window_search_by_artist.resizable(0, 0)
    window_search_by_artist.columnconfigure(0, weight=1)
    window_search_by_artist.rowconfigure(0, weight=1)

    frame_prompt = ttk.Frame(window_search_by_artist, padding=8)
    frame_prompt.grid(column=0, row=0, sticky="NSEW")
    window_search_by_artist.columnconfigure(0, weight=1)
    window_search_by_artist.rowconfigure(0, weight=1)
    frame_prompt["borderwidth"] = 4
    frame_prompt["relief"] = "solid"

    label_artist_id = Label(frame_prompt, text="Artist ID: ")
    label_artist_id.grid(column=0, row=0)
    entry_artist_id = Entry(frame_prompt)
    entry_artist_id.grid(column=1, row=0, sticky="NSEW")

    button_search = Button(frame_prompt, text="Search", command=search_by_artist_db)
    button_search.grid(column=0, row=1, columnspan=2, sticky="NSEW")

    window_search_by_artist.mainloop()


def search_by_medium():
    def search_by_medium_db():
        medium_search = entry_medium.get()
        cursor.execute(
            """
      SELECT * FROM art_pieces
      WHERE
        medium = ?
                  """,
            [medium_search],
        )

        search_results = cursor.fetchall()

        view_search_art_pieces(search_results)

    window_search_by_medium = Tk()
    window_search_by_medium.title("Search by Medium")
    window_search_by_medium.minsize(200, 150)
    window_search_by_medium.resizable(0, 0)
    window_search_by_medium.columnconfigure(0, weight=1)
    window_search_by_medium.rowconfigure(0, weight=1)

    frame_prompt = ttk.Frame(window_search_by_medium, padding=8)
    frame_prompt.grid(column=0, row=0, sticky="NSEW")
    window_search_by_medium.columnconfigure(0, weight=1)
    window_search_by_medium.rowconfigure(0, weight=1)
    frame_prompt["borderwidth"] = 4
    frame_prompt["relief"] = "solid"

    label_medium = Label(frame_prompt, text="Medium: ")
    label_medium.grid(column=0, row=0)
    entry_medium = Entry(frame_prompt)
    entry_medium.grid(column=1, row=0, sticky="NSEW")

    button_search = Button(frame_prompt, text="Search", command=search_by_medium_db)
    button_search.grid(column=0, row=1, columnspan=2, sticky="NSEW")

    window_search_by_medium.mainloop()


def search_by_price():
    def search_by_price_db():
        min_price_search = entry_min_price.get()
        max_price_search = entry_max_price.get()
        cursor.execute(
            """
      SELECT * FROM art_pieces
      WHERE price BETWEEN ? AND ?
      ORDER BY price ASC
                  """,
            [min_price_search, max_price_search],
        )

        search_results = cursor.fetchall()

        view_search_art_pieces(search_results)

    window_search_by_price = Tk()
    window_search_by_price.title("Search by Price")
    window_search_by_price.minsize(200, 150)
    window_search_by_price.resizable(0, 0)
    window_search_by_price.columnconfigure(0, weight=1)
    window_search_by_price.rowconfigure(0, weight=1)

    frame_prompt = ttk.Frame(window_search_by_price, padding=8)
    frame_prompt.grid(column=0, row=0, sticky="NSEW")
    window_search_by_price.columnconfigure(0, weight=1)
    window_search_by_price.rowconfigure(0, weight=1)
    frame_prompt["borderwidth"] = 4
    frame_prompt["relief"] = "solid"

    label_min_price = Label(frame_prompt, text="Min. Price: ")
    label_min_price.grid(column=0, row=0)
    entry_min_price = Entry(frame_prompt)
    entry_min_price.grid(column=1, row=0, sticky="NSEW")

    label_max_price = Label(frame_prompt, text="Max. Price: ")
    label_max_price.grid(column=0, row=1)
    entry_max_price = Entry(frame_prompt)
    entry_max_price.grid(column=1, row=1, sticky="NSEW")

    button_search = Button(frame_prompt, text="Search", command=search_by_price_db)
    button_search.grid(column=0, row=2, columnspan=2, sticky="NSEW")

    window_search_by_price.mainloop()


def mark_sold():

    table_focus = table_art_pieces.focus()
    keys_focus = table_art_pieces.item(table_focus)
    art_focus = keys_focus.get("values")
    piece_id = art_focus[0]

    old_sold = art_focus[5]
    new_sold = ""

    if old_sold == "No":
        new_sold = "Yes"
    elif old_sold == "Yes":
        new_sold = "No"

    cursor.execute(
        """
    UPDATE art_pieces
    SET sold = ?
    WHERE
      piece_id = ?
              """,
        [new_sold, piece_id],
    )

    db.commit()
    view_art_pieces()


def export_to_txt():
    def export_sold_pieces():
        cursor.execute(
            """
      SELECT * FROM art_pieces
      WHERE
        sold = 'Yes'
                  """
        )

        search_results = cursor.fetchall()

        file = open("SoldArt.txt", "a+")
        for x in search_results:
            file.write("".join(str(x)) + "\n")

        file.close()

        cursor.execute(
            """
      DELETE FROM art_pieces
      WHERE
        sold = 'Yes'
                  """
        )

        reload_views()

    window_notice = Tk()
    window_notice.title("Sold Pieces Exported")
    window_notice.minsize(200, 50)
    window_notice.resizable(0, 0)
    window_notice.columnconfigure(0, weight=1)
    window_notice.rowconfigure(0, weight=1)

    frame_prompt = ttk.Frame(window_notice, padding=8)
    frame_prompt.grid(column=0, row=0, sticky="NSEW")
    window_notice.columnconfigure(0, weight=1)
    window_notice.rowconfigure(0, weight=1)
    frame_prompt["borderwidth"] = 4
    frame_prompt["relief"] = "solid"

    export_sold_pieces()

    label_notice = Label(
        frame_prompt,
        text="Sold pieces exported to SoldArt.txt and cleared from database.",
    )
    label_notice.grid(column=0, row=0)

    window_notice.mainloop()


def clear_db():
    cursor.execute("DELETE FROM artists")
    cursor.execute("DELETE FROM art_pieces")
    reload_views()


def view_artists():
    for row in table_artists.get_children():
        table_artists.delete(row)

    artists_in_record = cursor.execute("SELECT * FROM artists")
    for i, row in enumerate(artists_in_record):
        table_artists.insert("", "end", values=(row))


def view_art_pieces():
    for row in table_art_pieces.get_children():
        table_art_pieces.delete(row)
    art_pieces_in_record = cursor.execute("SELECT * FROM art_pieces")
    for i, row in enumerate(art_pieces_in_record):
        table_art_pieces.insert("", "end", values=(row))


def view_search_art_pieces(search_results):
    for row in table_art_pieces.get_children():
        table_art_pieces.delete(row)
    for i, row in enumerate(search_results):
        table_art_pieces.insert("", "end", values=(row))


################################################################

with sqlite3.connect("artists.db") as db:
    cursor = db.cursor()
create_tables()

window_main = Tk()
window_main.title("Artist's Database")
window_main.minsize(900, 500)
window_main.resizable(0, 0)
window_main.columnconfigure(0, weight=1)
window_main.rowconfigure(0, weight=1)

frame_main = ttk.Frame(window_main, padding=8)
frame_main.grid(column=0, row=0, sticky="NSEW")
window_main.columnconfigure(0, weight=1)
window_main.rowconfigure(0, weight=1)
frame_main["borderwidth"] = 4
frame_main["relief"] = "solid"

notebook_main = ttk.Notebook(frame_main, padding=2)
notebook_main.grid(column=0, row=0, columnspan=3, sticky="NSEW")

page_view_artists = ttk.Frame(notebook_main, padding=2)
page_view_artists.grid(column=0, row=0, sticky="NSEW")
page_view_artpieces = ttk.Frame(notebook_main, padding=2)
page_view_artpieces.grid(column=0, row=0, sticky="NSEW")

notebook_main.add(page_view_artists, text="Artists")
notebook_main.add(page_view_artpieces, text="Art Pieces")

table_artists = ttk.Treeview(page_view_artists)
table_artists.grid(column=0, row=0, columnspan=3, sticky="NSEW")
table_artists["columns"] = ["ID", "Name", "Address", "Town", "County", "Postcode"]

table_artists.column("#0", width=0, stretch=NO)

for i in table_artists["columns"]:
    table_artists.column(i, anchor=CENTER, width=150)
    table_artists.heading(i, text=f"{i}", anchor=CENTER)

table_art_pieces = ttk.Treeview(page_view_artpieces)
table_art_pieces.grid(column=0, row=0, columnspan=3, sticky="NSEW")
table_art_pieces["columns"] = [
    "Piece ID",
    "Artist ID",
    "Title",
    "Medium",
    "Price",
    "Sold",
]

table_art_pieces.column("#0", width=0, stretch=NO)

for i in table_art_pieces["columns"]:
    table_art_pieces.column(i, anchor=CENTER, width=150)
    table_art_pieces.heading(i, text=f"{i}", anchor=CENTER)

button_add_artist = Button(
    page_view_artists, text="Add Artist Profile", command=add_artist
)
button_add_artist.grid(column=0, row=1, rowspan=2, sticky="WE")

button_update_artist = Button(
    page_view_artists, text="Update Artist Profile", command=update_artist
)
button_update_artist.grid(column=1, row=1, sticky="WE")

button_delete_artist = Button(
    page_view_artists, text="Delete Artist Profile", command=delete_artist
)
button_delete_artist.grid(column=2, row=1, sticky="WE")

button_add_art = Button(page_view_artpieces, text="Add New Art", command=add_art)
button_add_art.grid(column=0, row=1, sticky="NSEW")

button_update_art = Button(page_view_artpieces, text="Update Art", command=update_art)
button_update_art.grid(column=1, row=1, sticky="NSEW")

button_delete_art = Button(page_view_artpieces, text="Delete Art", command=delete_art)
button_delete_art.grid(column=2, row=1, sticky="NSEW")

button_mark_sold = Button(
    page_view_artpieces, text="Mark/Unmark Art as Sold", command=mark_sold
)
button_mark_sold.grid(column=0, row=2, columnspan=3, sticky="NSEW")

button_search_by_artist = Button(
    page_view_artpieces, text="Search Art by Artist", command=search_by_artist
)
button_search_by_artist.grid(column=0, row=3, sticky="NSEW")

button_search_by_medium = Button(
    page_view_artpieces, text="Search Art by Medium", command=search_by_medium
)
button_search_by_medium.grid(column=1, row=3, sticky="NSEW")

button_search_by_price = Button(
    page_view_artpieces, text="Search Art by Price", command=search_by_price
)
button_search_by_price.grid(column=2, row=3, sticky="NSEW")

button_export_sold = Button(frame_main, text="Export sold art", command=export_to_txt)
button_export_sold.grid(column=0, row=1, columnspan=3, sticky="NSEW")

button_demo_data = Button(frame_main, text="Generate demo data", command=load_demo)
button_demo_data.grid(column=0, row=2, columnspan=3, sticky="NSEW")

button_clear_db = Button(frame_main, text="Clear database", command=clear_db)
button_clear_db.grid(column=0, row=3, columnspan=3, sticky="NSEW")

button_refresh_tables = Button(frame_main, text="Refresh tables", command=reload_views)
button_refresh_tables.grid(column=0, row=4, columnspan=3, sticky="NSEW")

window_main.mainloop()
db.close()
