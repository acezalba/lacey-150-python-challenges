from tkinter import *
from tkinter import ttk

# Create a program that will ask the user to enter
# a number in a box. When they click on a button
# it will add that number to a total and display it
# in another box. This can be repeated as many times
# as many times as they want and keep adding to the
# total. There should be another button that resets
# the total back to 0 and empties the original text
# box, ready for them to start again.


def add():
    sum_value.set(sum_value.get() + addend_value.get())


def reset():
    # TODO
    sum_value.set(0)


##############################################################################

root = Tk()
root.title("Keep on adding!")
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

sum_value = IntVar()
sum_value.set(0)
sum_label = Label(main_frame, textvariable=sum_value).grid(
    column=0, row=0, columnspan=2, sticky="WE"
)

addend_value = IntVar()
addend_value.set(0)
addend_entrybox = Entry(main_frame, textvariable=addend_value).grid(
    column=0, row=1, columnspan=2, sticky="WE"
)

add_button = Button(main_frame, text="Add", command=add).grid(
    column=0, row=2, sticky="WE"
)
reset_button = Button(main_frame, text="Reset", command=reset).grid(
    column=1, row=2, sticky="WE"
)

root.mainloop()
