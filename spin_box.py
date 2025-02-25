import tkinter as tk


root = tk.Tk()

root.geometry("400x500")
initial_value=tk.IntVar(value=20)
spin_box = tk.Spinbox(
    root,
    #from_=0,
    #to=30,
    values=(5,10,20,25,30),
    textvariable=initial_value,
    wrap=False
)
spin_box.pack()

print(spin_box.get())

root.mainloop()