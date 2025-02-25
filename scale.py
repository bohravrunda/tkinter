import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.geometry("400x500")

def handle_scale_chamge(event):
    print(scale.get())

scale=ttk.Scale(root,orient="horizontal",from_=0,to=10,command=handle_scale_chamge)
scale.pack(fill="x")
root.mainloop()