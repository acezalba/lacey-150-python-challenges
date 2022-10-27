from genericpath import isfile
from tkinter import *
from tkinter import ttk
from os import path

# Save several images in the same foler as your program and call them 1.gif,
# 2.git, etc. Make them all gif files. Display one in a window and ask the user
# to enter a number. It should use that number to choose the correct file name
# and display the correct image.


def change_file():
    new_file = f"{file_name.get()}.png"
    if path.isfile(new_file):
        new_photo = PhotoImage(file=new_file)
    else:
        new_photo = PhotoImage(file="image.png")
    picture_holder.image = new_photo
    picture_holder["image"] = new_photo
    picture_holder.update()


#############################################################################

root = Tk()
root.title("Change image")
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

file = PhotoImage(file="1.png")
picture_holder = Label(main_frame, image=file)
picture_holder.grid(column=0, row=0, columnspan=2, sticky="NEW")

instructions = Label(main_frame, text="To change image, enter 1,2 or 3: ")
instructions.grid(column=0, row=1, sticky="NSEW")

file_name = IntVar()
file_name_entry = Entry(main_frame, textvariable=file_name, justify="center")
file_name_entry.grid(column=0, row=2, sticky="NSEW")

change_file_button = Button(main_frame, text="Change image", command=change_file)
change_file_button.grid(column=0, row=3, sticky="NSEW")

root.mainloop()
