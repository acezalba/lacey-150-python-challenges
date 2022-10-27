from tkinter import *
from tkinter import ttk

# Create a window that will ask the user to enter a number in a text box. When
# they click on the button it will use the code variable.isdigit() to check to
# see if it is a whole number. If it is a whole number, add it to a list box,
# otherwise clear the entry box. Add another button that will clear the list.


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

whole_num_listbox = Listbox(main_frame)
whole_num_listbox.grid(column=1, row=0, rowspan=4, sticky="NSEW", padx=(4, 0))
whole_num_listbox["bg"] = "black"
whole_num_listbox["fg"] = "green"

root.mainloop()
