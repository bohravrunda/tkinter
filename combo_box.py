import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")

selected_weekday=tk.StringVar()
weekday=ttk.Combobox(root,textvariable=selected_weekday)
weekday["value"]=("monday","tuesday","wednesday","thusday","friday","saturday","sunday")
weekday["state"]="readonly"
weekday.pack()

def handle_selection(event):
    print("today is ",selected_weekday.get())
    print("but we gonna change it to friday")
    selected_weekday.set("friday")
    print(weekday.current())
weekday.bind("<<ComboboxSelected>>",handle_selection)
root.mainloop()

print(selected_weekday.get(),"was selected")
