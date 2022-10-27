# /usr/bin/env python3
"""
Times Table (GUI)
"""


def view_table():
    number = int(times_number.get())

    times_table = []
    for x in range(1, 13):
        times_table.append(f"{x} x {number} = {number*x}")

    for line in times_table:
        listbox_times_table.insert(END, line)


def clear_view():
    times_number.set(0)
    listbox_times_table.delete(0, END)
    entry_number.delete(0, END)
    entry_number.focus()


from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Times Table")
root.minsize(300, 300)
root.resizable(0, 0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

main_frame = ttk.Frame(root, padding=8)
main_frame.grid(column=0, row=0, sticky="NSEW")
main_frame.rowconfigure(1, weight=2)
main_frame["borderwidth"] = 4
main_frame["relief"] = "solid"

label_number_prompt = Label(main_frame, text="Enter a number:")
label_number_prompt.grid(column=0, row=0, sticky="W")

times_number = IntVar()
entry_number = Entry(main_frame, textvariable=times_number)
entry_number.grid(column=1, row=0, sticky="WE")
entry_number.focus()

listbox_times_table = Listbox(main_frame)
listbox_times_table.grid(column=1, row=1, sticky="NSEW")
listbox_times_table["relief"] = "solid"

button_view_table = Button(main_frame, text="View Times Table", command=view_table)
button_view_table.grid(column=2, row=0, sticky="SEW", padx=(2, 0))
button_clear = Button(main_frame, text="Clear", command=clear_view)
button_clear.grid(column=2, row=1, sticky="NWE", padx=(2, 0))

root.mainloop()
