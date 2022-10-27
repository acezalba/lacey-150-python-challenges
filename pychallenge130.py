from tkinter import *
from tkinter import ttk
import csv

# Alter program 129 to add a third button that will save the list to a .csv
# file. The code tmp_list = num_list.get(0, END) can be used to save the
# contents of a list box as a tuple called tmp_list.


def add_to_list():
    value = add_whole_num.get()
    if value.isdigit():
        temp = IntVar()
        temp.set(value)
        whole_num_listbox.insert(END, temp.get())
        warning.set(" ")
    else:
        warning.set("Number not a whole digit.")


def reset():
    whole_num_listbox.delete(0, END)


def save_to_csv():
    tmp_list = list(whole_num_listbox.get(0, END))
    with open("130-TKinter-CSVList.csv", "w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(tmp_list)


###############################################################################

root = Tk()
root.title("Add whole numbers to list")
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

warning = StringVar()
warning_label = Label(main_frame, textvariable=warning)
warning_label.grid(column=0, row=0, sticky="SEW")
warning_label["fg"] = "purple"

add_whole_num = StringVar()
add_whole_num.set("Enter whole_num here")
add_whole_num_entrybox = Entry(main_frame, textvariable=add_whole_num)
add_whole_num_entrybox.grid(column=0, row=1, sticky="SEW")

add_button = Button(main_frame, text="Add Number to List", command=add_to_list)
add_button.grid(column=0, row=2, sticky="WE")
reset_button = Button(main_frame, text="Reset List", command=reset)
reset_button.grid(column=0, row=3, sticky="WE")
csv_button = Button(main_frame, text="Export to CSV", command=save_to_csv)
csv_button.grid(column=0, row=4, sticky="WE")

whole_num_listbox = Listbox(main_frame)
whole_num_listbox.grid(column=1, row=0, rowspan=5, sticky="NSEW", padx=(4, 0))
whole_num_listbox["bg"] = "black"
whole_num_listbox["fg"] = "green"

root.mainloop()
