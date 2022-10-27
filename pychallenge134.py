from tkinter import *
from tkinter import ttk
from random import randint

# Create a new program that will generate two random whole numbers between
# 10 and 50. It should ask the user to add the numbers together and type in the
# answer. If they get the question correct, display a suitable image
# such as a tick; if they get the answer wrong, display another suitable image
# such as a cross. They should click on a Next button to get another question.


def eval():
    correct_mark = PhotoImage(file="correct.png")
    wrong_mark = PhotoImage(file="wrong.png")

    if answer.get() == sum.get():
        mark_image.image = correct_mark
        mark_image["image"] = correct_mark
        addend_1 = randint(10, 50)
        addend_2 = randint(10, 50)
        sum.set(int(addend_1 + addend_2))
        question.set(f"What is {addend_1} + {addend_2}?")
    else:
        mark_image.image = wrong_mark
        mark_image["image"] = wrong_mark

    mark_image.update()


################################################################################

root = Tk()
root.title("Guess the number!")
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
main_frame.rowconfigure(1, weight=4)

mark = PhotoImage(file="image.png")
mark_image = Label(main_frame, image=mark)
mark_image.grid(column=0, row=0, sticky="NEW")

addend_1 = randint(10, 50)
addend_2 = randint(10, 50)
sum = IntVar()
sum.set(int(addend_1 + addend_2))

question = StringVar()
question.set(f"What is {addend_1} + {addend_2}?")
question_entrybox = Entry(main_frame, textvariable=question, justify="center")
question_entrybox.grid(column=0, row=1, columnspan=2, pady=8, sticky="NSEW")
question_entrybox["bg"] = "black"
question_entrybox["fg"] = "green"

answer_guide_label = Label(
    main_frame, text="Enter your answer below: ", justify="center"
)
answer_guide_label.grid(column=0, row=2, sticky="NSEW")

answer = IntVar()
answer_entrybox = Entry(main_frame, textvariable=answer, justify="center")
answer_entrybox.grid(column=0, row=3, sticky="NSEW")

check_button = Button(main_frame, text="Check Answer", command=eval)
check_button.grid(column=0, row=4, pady=8, sticky="NSEW")
check_button["bg"] = "#006400"
check_button["fg"] = "white"

root.mainloop()
