import tkinter as tk
import tkinter.font as font
from tkinter import ttk


root = tk.Tk()
root.title("Distance Converter")

root.geometry("400x500")
font.nametofont("TkDefaultFont").configure(size=15)#chnaging font of text



root.columnconfigure(0,weight=1)

main=ttk.Frame(root,padding=(30,15))
main.grid()

meter_value=tk.StringVar()
feet_value=tk.StringVar(value="Feet shown here:")

def calculate(*args):
    try:
        meter=float(meter_value.get())
        feet=meter*3.28084
        #print(f"{meter} meter is = {feet:.3f} feet.") cal is shown in terminal
        feet_value.set(f"{feet:.3f}")#to show cal in window itself
    except ValueError:
        pass



meter_label=tk.Label(main,text="Meters:")
meters_input=ttk.Entry(main,width=10,textvariable=meter_value,font=("Seogoe UI",15))
feet_label=ttk.Label(main,text="Feet:")
feet_display=ttk.Label(main,textvariable=feet_value)
calc_button=ttk.Button(main,text="Calculate",command=calculate)

meter_label.grid(row=0,column=0,sticky="w")
meters_input.grid(column=1,row=0,sticky="ew")
meters_input.focus()

feet_label.grid(row=1,column=0,sticky="w")
feet_display.grid(row=1,column=1,sticky="ew")
calc_button.grid(row=2,column=0,columnspan=2,sticky="ew",)

for child in main.winfo_children():
    child.grid_configure(padx=15,pady=15)


root.bind("<Return>",calculate)
root.bind("<KP_Enter>",calculate)#it calcutale by pressing enter directly





root.mainloop()