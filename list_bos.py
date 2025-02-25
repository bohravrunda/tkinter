import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")

lang=("c","c++","python","perl")

langs=tk.StringVar(value=lang)
langs_select = tk.Listbox(root,listvariable=langs,height=6)
langs_select["selectmode"] = "extended"
langs_select.pack()

def handle_selection_change(event):
    selected_indices = langs_select.curselection()
    for i in selected_indices:
        print(langs_select.get(i))

langs_select.bind("<<ListboxSelect>>",handle_selection_change)

root.mainloop()
