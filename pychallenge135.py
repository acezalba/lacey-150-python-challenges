from tkinter import *
from tkinter import ttk

# Create a simple program that shows a drop-down list containing several colours
# and a Click Me button. When the user selects a colour from the list and clicks
# the button it should change the background of the window to that colour. For
# an extra challenge, try to avoid using an if statement to do this.


def change_bg():
    if color_listbox.curselection() != ():
        s.configure(
            "My.TFrame", background=color_listbox.get(color_listbox.curselection())
        )
        main_frame["style"] = "My.TFrame"


#################################################################################

root = Tk()
root.title("Change the background!")
root.call("wm", "iconphoto", root._w, PhotoImage(file="icon.png"))
root.minsize(500, 200)
root.resizable(0, 0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

s = ttk.Style()
s.configure("My.TFrame", background="grey")

main_frame = ttk.Frame(root, padding=32, style="My.TFrame")
main_frame.grid(column=0, row=0, sticky="NSEW")
main_frame["borderwidth"] = 4
main_frame["relief"] = "solid"

color_listbox = Listbox(main_frame)
color_listbox.grid(column=0, row=0, pady=12, sticky="NSEW")
color_listbox["bg"] = "white"

color_list = ["black", "red", "green", "blue", "cyan", "yellow", "magenta"]
for place, color in enumerate(color_list):
    color_listbox.insert(END, color)
    color_listbox.itemconfig(place, {"fg": color})

change_bg_button = Button(
    main_frame, text="Change background to color", command=change_bg
)
change_bg_button.grid(column=0, row=1, pady=12, sticky="NSEW")

root.mainloop()
