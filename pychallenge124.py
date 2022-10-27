import tkinter as tk

# Create a window that will ask the user to
# enter their name. When they click on a button it
# should display the message "Hello" and
# their name and change the background color
# and font color of the message box.


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hello Tkinter")
        self.minsize(500, 200)

        self.label_text = tk.StringVar()
        self.label_text.set("Enter your name.")

        self.label = tk.Label(self, textvariable=self.label_text)
        self.label.pack(fill=tk.BOTH, expand=1, padx=96, pady=32)

        self.entry_box = tk.Entry(text=0)
        self.entry_box.pack(fill=tk.BOTH, expand=1, padx=8, pady=4)

        hello_button = tk.Button(self, text="Hello", command=self.say_hello)
        hello_button.pack(fill=tk.BOTH, expand=1, padx=8, pady=(4, 8))

    def say_hello(self):
        self.username = self.entry_box.get()
        self.label_text.set(f"Hello {self.username}")
        self["bg"] = "#51050F"
        self.label["bg"] = "#51050F"
        self.label["fg"] = "#F78812"


if __name__ == "__main__":
    window = Window()
    window.mainloop()
