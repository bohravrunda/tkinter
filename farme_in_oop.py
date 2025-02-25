import tkinter as tk
from tkinter import ttk


class helloworld(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Hello World!")

        UserInputFrame(self).pack()


class UserInputFrame(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)

        self.user_input=tk.StringVar()
        label=ttk.Label(self,text="Enter your name")
        entry = tk.Entry(self,textvariable=self.user_input)
        button = tk.Button(self,text="enter",command=self.greet)

        label.pack(side="left")
        entry.pack(side="left")

        button.pack(side="left")

    def greet(self):
        print(f"hello {self.user_input.get()}")





root=helloworld()



root.mainloop()