# This contains code notes for Challenges 124 to 138: Tkinter
# For the Nicola Lacey Book.

# I was frustrated how solving Lacey's exercises encourages
# bad practices, or coding style that you don't really see
# in tutorials everywhere. But looking into other books that uses
# better practices adds extra complexity to her simple exercises.

# More so reading different tutorials that uses OOP creates weird conflicts
# due to coding style.

# So to avoid suspending progress in her activities, I took down notes
# and made effort to do it close to her way while reading up on
# recommended approaches to using Tkinter.

##############################################################################

# This line must go at the beginning of the program to import the Tkinter
# library

from tkinter import *

# Creates a window that will act as the display, referred to as "window",
# adds a title and defines the size of the window

window = Tk
window.title("Window Title")
window.geometry("450 x 100")

# Adds text to the screen displaying the message shown

label = Label(text="Enter number: ")

# Creates a blank entry box. Entry boxes can be used by the user to input
# data or used to display output

entry_box = Entry(text=0)

# Creates a message box which is used to display an output

output_box = Message(text=0)

# Specifies the background colour of the object

output_box["bg"] = "red"

# Specifies the font colour of the object

output_box["fg"] = "white"

# Specifies the style of the box.
# This can be flat, raised, sunken, grooved, and ridged.

output_box["relief"] = "sunken"

# Creates a drop-down list box which can only contain strings

list_box = "Listbox"

# Specifies the justification of the text in an entry box,
# but this does not work for message boxes

entry_box["justify"] = "center"

# Creates a button that will run the subprogram "click"

button1 = Button(text="Click here", command=click)

# Specifies the position in which the object will appear in the window.
# If the position is not specified the item will not appear in the window.

label.place(x=50, y=20, width=100, height=25)

# Deletes the contents of an entry or listbox

entry_box.delete(0, END)

# saves the contents of an entry box and stores it in a variable called num.
# This does not work with message boxes.

num = entry_box.get()

# Obtains the contents of a 'message box' and stores it in a variable
# called answer. This does not work with an entry box.

answer = output_txt["text"]

# Changes the content of a message box to display the value
# of the variable total

output_txt["text"] = total

# This must be at the end of the program to make sure it keeps working

window.mainloop()

##############################################################################

# Changes the icon displayed in the title of the window

window.wm_iconbitmap("MyIcon.ico")

# Changes the background colour of the window, in this case to light green.

window.configure(background="light green")

# Display an image in a label widget. This image will not change
# while the program is running.

logo = PhotoImage(file="logo.gif")
logoimage = Label(image=logo)
logoimage.place(x=30, y=20, width=200, height=120)

# This is similar to the block above but as we want the image to change
# as we update the data we need to add the code `photobox.image = photo`
# which makes it updatable

photo = PhotoImage(file="logo.gif")
photobox = Label(Window, image=photo)
photobox.image = photo
photobox.place(x=30, y=20, width=200, height=120)

# Creates a variable called selectName which will store a string where
# the original value of the variable is "Select Name". It will then create
# a drop-down option menu which stores the value selects in the selectName
# variable and displays the values in the list: Bob, Sue, and Tim.

selectName = StringVar(window)
selectName.set("Select Name")
namesList = OptionMenu(window, selectName, "Bob", "Sue", "Tim")
namesList.place(x=30, y=250)

# In this example, when a button is clicked it will run the "clicked" program
# This will obtain the value from the selectName variable and create a message
# that will be displayed in a label. It will then check to see which option
# has been selected and change the picture to the correct image, which
# is displayed in the photovariable. If no name is selected it will simply show
# the logo.


def clicked():
    sel = selectName.get()
    mesg = "Hello " + sel
    mlabel["text"] = mesg
    if sel == "Bob":
        photo = PhotoImage(file="Bob.gif")
        photobox.image = photo
    elif sel == "Sue":
        photo = PhotoImage(file="Sue.gif")
        photobox.image = photo
    elif sel == "Sue":
        photo = PhotoImage(file="Sue.gif")
        photobox.image = photo
    else:
        photo = PhotoImage(file="logo.gif")
        photobox.image = photo
    photobox["image"] = photo
    photobox.update()
