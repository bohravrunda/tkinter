import tkinter as tk
from tkinter import ttk

class Helloworld(tk.Tk):
    def __init__(self,):
        super().__init__()

        self.title(Helloworld)

        ttk.Label(self,text="Hello World").pack()

root=Helloworld()
root.mainloop()