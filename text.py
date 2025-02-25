import tkinter as tk
from tkinter import ttk



root = tk.Tk()

root.geometry("400x600")
text=tk.Text(root,height=8)
text.pack()
text.insert("1.0","please enter comment...")
#text["state"]="disable"

print(text.get("0.1","end"))

root.mainloop()