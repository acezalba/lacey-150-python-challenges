from tkinter import *
from tkinter import ttk

# Create your own icon that consists of several vertical multicolored lines.
# Create a logo which measures 200x150. Create the following window:...
# When the user enters their name and clicks on the Press Me button it should
# display "Hello" and their name in the second text box.

# Notes: create the image sizes in advance. 200x150 or 200x200.
# Tkinter does not support moving gifs. You have to create your own images,
# at least png works.


def say_greeting():
    greeting.set("Hello, " + name.get() + "!!!")


###############################################################################

root = Tk()
root.title("Greet you!")
root.call("wm", "iconphoto", root._w, PhotoImage(file="icon.png"))
root.minsize(100, 300)
root.resizable(0, 0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

main_frame = ttk.Frame(root, padding=4)
main_frame.grid(column=0, row=0, sticky="NSEW")
main_frame["borderwidth"] = 4
main_frame["relief"] = "solid"
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=3)
main_frame.rowconfigure(1, weight=2)

logo = PhotoImage(file="image.png")
logo_image = Label(main_frame, image=logo)
logo_image.grid(column=0, row=0, columnspan=2, sticky="NEW")

greeting = StringVar()
greeting.set("What is your name?")
greeting_entrybox = Entry(main_frame, textvariable=greeting, justify="center")
greeting_entrybox.grid(column=0, row=1, columnspan=2, pady=6, sticky="NSEW")
greeting_entrybox["bg"] = "black"
greeting_entrybox["fg"] = "green"

name_label = Label(main_frame, text="Name")
name_label.grid(column=0, row=2, sticky="W")

name = StringVar()
name_entrybox = Entry(main_frame, textvariable=name)
name_entrybox.grid(column=1, row=2, sticky="W")

greeting_button = Button(main_frame, text="Press Me", command=say_greeting)
greeting_button.grid(column=0, row=3, columnspan=2, stick="EW")


root.mainloop()
