import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("500x600")

root.grid_columnconfigure(0,weight=1)
root.grid_rowconfigure(0,weight=1)
text=tk.Text(root,height=8)
text.grid(row=0,column=0,sticky="ew")
text.insert("1.0","please enter comment...")

text_scroll=ttk.Scrollbar(root,orient="vertical",command=text.yveiw)
text_scroll.grid(row=0,column=1,sticky="ns")
text["yscrollcommand"]=text_scroll.set



root.mainloop()