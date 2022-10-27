from tkinter import *
from tkinter import ttk

# 1 kilometer = 0.6214 miles and one mile = 1.6093 kilometers. Using these
# figures, make a program that will allow the user to convert between miles
# and kilometers.


def mi_to_km():
    km_value.set(mi_value.get() * 1.6093)
    km_entrybox.config({"background": "#FF7F7F"})
    mi_entrybox.config({"background": "white"})


def km_to_mi():
    mi_value.set(km_value.get() * 0.6214)
    km_entrybox.config({"background": "white"})
    mi_entrybox.config({"background": "#FF7F7F"})


def reset():
    km_value.set(0)
    mi_value.set(0)
    km_entrybox.config({"background": "white"})
    mi_entrybox.config({"background": "white"})


###############################################################################

root = Tk()
root.title("Miles to KM converter")
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

mi_label = Label(main_frame, text="Miles").grid(column=0, row=0, sticky="WE")
km_label = Label(main_frame, text="Kilometers").grid(column=1, row=0, stick="WE")

mi_value = DoubleVar()
mi_value.set(0)
mi_entrybox = Entry(main_frame, textvariable=mi_value)
mi_entrybox.grid(column=0, row=1, sticky="WE")

km_value = DoubleVar()
km_value.set(0)
km_entrybox = Entry(main_frame, textvariable=km_value)
km_entrybox.grid(column=1, row=1, sticky="WE")

mi_to_km_button = Button(
    main_frame, text="Convert Miles to Kilometers", command=mi_to_km
)
mi_to_km_button.grid(column=0, row=2, sticky="WE")

km_to_mi_button = Button(
    main_frame, text="Convert Kilometers to Miles", command=km_to_mi
)
km_to_mi_button.grid(column=1, row=2, sticky="WE")

reset_button = Button(main_frame, text="Reset", command=reset)
reset_button.grid(column=0, row=3, columnspan=2, sticky="WE")

root.mainloop()
