import tkinter as tk
from tkinter import ttk

root=tk.Tk()

root.geometry("500x400")
root.resizable(False,False)

storage_variable = tk.StringVar()

option_one = ttk.Radiobutton(
    root,
    text="option one",
    variable=storage_variable,
    value="First OPtion"


)

option_two = ttk.Radiobutton(
    root,
    text="option two",
    variable=storage_variable,
    value="Second Option"


)

option_three = ttk.Radiobutton(
    root,
    text="option three",
    variable=storage_variable,
    value="Third OPtion"


)
option_one.pack()
option_two.pack()

option_three.pack()



root.mainloop()
