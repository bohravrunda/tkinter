import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("500x600")

root.grid_columnconfigure(0,weight=1)
root.grid_rowconfigure(0,weight=1)

ttk.Label(root,text="hello",padding=20).pack()

ttk.Separator(root,orient="horizontal").pack(fill="x")

ttk.Label(root,text="hello",padding=20).pack()




root.mainloop()