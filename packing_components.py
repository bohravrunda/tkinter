import tkinter as tk
from tkinter import ttk

root=tk.Tk()

root.geometry("600x500")
 
rec_1=tk.Label(root,text="rec 1",bg="green",fg="white")
rec_1.pack(side="left",ipadx="10" , ipady="10",fill="both",expand=True)#expand in both side 

rec_2=tk.Label(root,text="rec 2",bg="pink",fg="white")
rec_2.pack(side="top",ipadx="10" , ipady="10",fill="both",expand=True)

rec_3=tk.Label(root,text="rec 3",bg="grey",fg="white")
rec_3.pack(side="right",ipadx="10" , ipady="10",fill="both",expand=True)




root.mainloop()