from tkinter import *
from tkinter import ttk
import os

# Change program 136 so that when a new name and gender is added to the list
# box it is also written to a text file. Add another button that will display
# the entire text file in the main Python shell window.


def add():
    row = f"{add_name.get()},{clicked.get()}"
    name_listbox.insert(END, row)
    file = open("name-gender.txt", "a")
    file.write(row + "\n")
    file.close()


def show():
    file = open("name-gender.txt", "r+")
    file.seek(0, 0)
    print(file.read())
    file.close()


def reset():
    name_listbox.delete(0, END)


############################################################################

root = Tk()
root.title("Keep on adding to the list")
root.minsize(500, 100)
root.resizable(0, 0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

main_frame = ttk.Frame(root, padding=4)
main_frame.grid(column=0, row=0, sticky="NSEW")
main_frame["borderwidth"] = 4
main_frame["relief"] = "solid"
main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure(0, weight=0)

add_name = StringVar()
add_name.set("Enter name here")
add_name_entrybox = Entry(main_frame, textvariable=add_name)
add_name_entrybox.grid(column=0, row=0, sticky="NSEW")

gender_frame = ttk.Frame(main_frame)
gender_frame.grid(column=0, row=1, sticky="NSEW", pady=8)
gender_frame.columnconfigure(1, weight=1)

gender_label = Label(gender_frame, text="Choose Gender: ")
gender_label.grid(column=0, row=0, sticky="E")

gender = ["Male", "Female", "Other", "Undisclosed"]
clicked = StringVar()
clicked.set("Undisclosed")
gender_dropdown = OptionMenu(gender_frame, clicked, *gender)
gender_dropdown.grid(column=1, row=0, sticky="W")

add_button = Button(main_frame, text="Add to List", command=add)
add_button.grid(column=0, row=2, sticky="NSEW")
reset_button = Button(main_frame, text="Reset List", command=reset)
reset_button.grid(column=0, row=3, sticky="NSEW")
show_button = Button(main_frame, text="Show file in console", command=show)
show_button.grid(column=0, row=4, sticky="NSEW")

name_listbox = Listbox(main_frame)
name_listbox.grid(column=1, row=0, rowspan=5, sticky="NSEW", padx=(4, 0))
name_listbox["bg"] = "black"
name_listbox["fg"] = "green"

root.mainloop()
