from tkinter import *
from tkinter import ttk

# Create a window that will ask the user to enter a name in a text box.
# When they click on a button it will add it to the end of the list that
# is displayed on the screen. Create another button that will clear the list


def add():
    name_listbox.insert(END, add_name.get())


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
main_frame.columnconfigure(1, weight=1)
main_frame.rowconfigure(0, weight=1)

add_name = StringVar()
add_name.set("Enter name here")
add_name_entrybox = Entry(main_frame, textvariable=add_name).grid(
    column=0, row=0, sticky="NSEW"
)

add_button = Button(main_frame, text="Add Name to List", command=add).grid(
    column=0, row=1, sticky="WE"
)
reset_button = Button(main_frame, text="Reset List", command=reset).grid(
    column=0, row=2, sticky="WE"
)

name_listbox = Listbox(main_frame)
name_listbox.grid(column=1, row=0, rowspan=3, sticky="NSEW", padx=(4, 0))
name_listbox["bg"] = "black"
name_listbox["fg"] = "green"

root.mainloop()
