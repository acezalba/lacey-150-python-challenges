import tkinter as tk
from random import randint

# Write a program that can be used instead of
# rolling a six-sided die in a board game
# When the user clicks a button it should
# display a random whole number between 1 to 6
# (inclusive)


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("6-Die Roller")
        self.minsize(200, 200)

        self.label_text = tk.StringVar()
        self.label_text.set("    ")

        self.label = tk.Label(self, textvariable=self.label_text)
        self.label.pack(fill=tk.BOTH, expand=1, padx=48, pady=32)

        hello_button = tk.Button(self, text="Roll the die", command=self.roll_die)
        hello_button.pack(fill=tk.BOTH, expand=1, padx=8, pady=(4, 8))

    def roll_die(self):
        self.label_text.set(randint(1, 6))


if __name__ == "__main__":
    window = Window()
    window.mainloop()
