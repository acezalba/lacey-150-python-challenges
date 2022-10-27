# Tkinter
# The program should save the data to a SQL database called
# TestScores when the Add button is clicked
# The clear button should clear the button

from tkinter import *
from tkinter import ttk
import sqlite3


def add_to_db():
    name_stored = student_name.get()
    grade_stored = student_grade.get()
    if name_stored and grade_stored:
        cursor.execute(
            """
                    INSERT INTO grades(student_name, student_grade)
                    VALUES (?,?)
                    """,
            (name_stored, grade_stored),
        )
        db.commit()
    clear_entry()


def clear_entry():
    student_name.set("")
    student_grade.set("")
    entry_student_name.focus()


##############################################################################

with sqlite3.connect("TestScores.db") as db:
    cursor = db.cursor()

cursor.execute(
    """
               CREATE TABLE IF NOT EXISTS grades(
                   student_name text NOT NULL,
                   student_grade integer NOT NULL                   
               )  
               """
)

root = Tk()
root.title("Store student grades to database")
root.minsize(300, 100)
root.resizable(0, 0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

main_frame = ttk.Frame(root, padding=4)
main_frame.grid(column=0, row=0, sticky="NSEW")
main_frame["borderwidth"] = 4
main_frame["relief"] = "solid"
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)

prompt_student_name = StringVar()
prompt_student_name.set("Enter student's name: ")
label_student_name = Label(main_frame, textvariable=prompt_student_name)
label_student_name.grid(column=0, row=0, sticky="NSE")

prompt_student_grade = StringVar()
prompt_student_grade.set("Enter student's grade: ")
label_student_grade = Label(main_frame, textvariable=prompt_student_grade)
label_student_grade.grid(column=0, row=1, sticky="NSE")

student_name = StringVar()
entry_student_name = Entry(main_frame, textvariable=student_name)
entry_student_name.grid(column=1, row=0, sticky="NSW")

student_grade = StringVar()
entry_student_grade = Entry(main_frame, textvariable=student_grade)
entry_student_grade.grid(column=1, row=1, sticky="NSW")

button_frame = ttk.Frame(main_frame)
button_frame.grid(column=1, row=3, pady=8, sticky="NSEW")
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)

button_add = Button(button_frame, text="Add", command=add_to_db)
button_add.grid(column=0, row=0, sticky="NSEW")

button_clear_entry = Button(button_frame, text="Clear", command=clear_entry)
button_clear_entry.grid(column=1, row=0, sticky="NSEW")

root.mainloop()

db.close()
