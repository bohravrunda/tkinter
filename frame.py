import tkinter as tk
from tkinter import ttk

root = tk.Tk()

main = ttk.Frame(root)
main.pack(side="left",expand=True,fill="both")

tk.Label(main,text="label top",bg="red").pack(side="top",expand=True,fill="both")
tk.Label(main,text="label top",bg="red").pack(side="top",expand=True,fill="both")

tk.Label(root,text="label left",bg="green").pack(side="left",expand=True,fill="both")

root.mainloop()