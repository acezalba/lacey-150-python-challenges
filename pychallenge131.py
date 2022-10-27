from tkinter import *
from tkinter import ttk
import csv
import os.path

# Create a program that will allow the user to create a new .csv file.
# It should ask them to enter the name and age of a person and then allow
# them to add this to the end of the file they have just created.
# This program does not handle validation


def append():
    # Retrieve filename, append .csv to filename
    fname = csv_name.get() + ".csv"

    # Retrieve name and age, store as a tuple
    temp_name = name.get()
    temp_age = age.get()
    row_to_append = [temp_name, temp_age]

    # If filename exist, writemode append
    if os.path.isfile(fname):
        with open(fname, "a", newline="") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(row_to_append)
    # If filename exists, writemode append
    else:
        with open(fname, "w", newline="") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(row_to_append)


###############################################################################

root = Tk()
root.title("Append to csv")
root.minsize(250, 100)
root.resizable(0, 0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

main_frame = ttk.Frame(root, padding=4)
main_frame.grid(column=0, row=0, sticky="NSEW")
main_frame["borderwidth"] = 4
main_frame["relief"] = "solid"
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=8)

name = StringVar()
age = IntVar()
csv_name = StringVar()

label_csv = Label(main_frame, text="Filename: ")
label_csv.grid(column=0, row=0, sticky="W")
label_name = Label(main_frame, text="Name: ")
label_name.grid(column=0, row=1, sticky="W")
label_age = Label(main_frame, text="Age: ")
label_age.grid(column=0, row=2, sticky="W")

entry_csv = Entry(main_frame, textvariable=csv_name)
entry_csv.grid(column=1, row=0, sticky="EW")
entry_name = Entry(main_frame, textvariable=name)
entry_name.grid(column=1, row=1, sticky="EW")
entry_age = Entry(main_frame, textvariable=age)
entry_age.grid(column=1, row=2, sticky="EW")

button_append = Button(main_frame, text="Append data to file", command=append)
button_append.grid(column=0, row=3, columnspan=2, sticky="NSEW")

root.mainloop()
