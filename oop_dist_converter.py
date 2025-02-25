import tkinter as tk
import tkinter.font as font
from tkinter import ttk


class DistanceConverter(tk.Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.title("Distance Converter")
        self.frames=dict()

        container=ttk.Frame(self)
        container.grid(padx=60,pady=30,sticky="ew")

        
        metertofeet=meter_to_feet(container,self)
        metertofeet.grid(row=0,column=0,sticky="nsew")

        feettometer=feet_to_meter(container,self)
        feettometer.grid(row=0,column=0,sticky="nsew")

        self.frames[feet_to_meter]=feettometer
        self.frames[meter_to_feet]=metertofeet


        
        def show_frames(self,container):
            frame=self.frames[container]
            frame.tkraise()

class meter_to_feet(ttk.Frame):
    def __init__(self,container,controller,**kwargs):
        super().__init__(container,**kwargs)

        self.feet_value=tk.StringVar()
        self.meter_value=tk.StringVar()

        meter_label=tk.Label(self,text="Meters:")
        meters_input=ttk.Entry(self,width=10,textvariable=self.meter_value,font=("Seogoe UI",15))
        feet_label=ttk.Label(self,text="Feet:")
        feet_display=ttk.Label(self,textvariable=self.feet_value)
        calc_button=ttk.Button(self,text="Calculate",command=self.calculate)
        switch_page_button=ttk.Button(
            self,
            text="switch to feet conversion",
            command=lambda:controller.show_frames(feet_to_meter)

        )


        meter_label.grid(row=0,column=0,sticky="w")
        meters_input.grid(column=1,row=0,sticky="ew")
        meters_input.focus()

        feet_label.grid(row=1,column=0,sticky="w")
        feet_display.grid(row=1,column=1,sticky="ew")
        calc_button.grid(row=2,column=0,columnspan=2,sticky="ew")
        switch_page_button.grid(row=3,column=0,columnspan=2,sticky="ew")


        for child in self.winfo_children():
            child.grid_configure(padx=15,pady=15)

    
    def calculate(self,*args):
        try:
            meter=float(self.meter_value.get())
            feet=meter*3.28084
            #print(f"{meter} meter is = {feet:.3f} feet.") cal is shown in terminal
            self.feet_value.set(f"{feet:.3f}")#to show cal in window itself
        except ValueError:
            pass

class feet_to_meter(ttk.Frame):
    def __init__(self,container,controller,**kwargs):
        super().__init__(container,**kwargs)

        self.feet_value=tk.StringVar()
        self.meter_value=tk.StringVar()

        feet_label=tk.Label(self,text="feet:")
        feet_input=ttk.Entry(self,width=10,textvariable=self.feet_value,font=("Seogoe UI",15))
        meter_label=ttk.Label(self,text="meter:")
        meter_display=ttk.Label(self,textvariable=self.meter_value)
        calc_button=ttk.Button(self,text="Calculate",command=self.calculate)
        switch_page_button=ttk.Button(
            self,
            text="switch to feet conversion",
            command=lambda:controller.show_frames(feet_to_meter)

        )

        feet_label.grid(row=0,column=0,sticky="w")
        feet_input.grid(column=1,row=0,sticky="ew")
        feet_input.focus()

        meter_label.grid(row=1,column=0,sticky="w")
        meter_display.grid(row=1,column=1,sticky="ew")
        calc_button.grid(row=2,column=0,columnspan=2,sticky="ew",)
        switch_page_button.grid(row=3,column=0,columnspan=2,sticky="ew")
       

        for child in self.winfo_children():
            child.grid_configure(padx=15,pady=15)

    
    def calculate(self,*args):
        try:
            feet=float(self.feet_value.get())
            meter=feet/3.28084
            #print(f"{meter} meter is = {meter:.3f} meter.") cal is shown in terminal
            self.meter_value.set(f"{meter:.3f}")#to show cal in window itself
        except ValueError:
            pass




root = DistanceConverter()

root.geometry("400x500")
font.nametofont("TkDefaultFont").configure(size=15)#chnaging font of text



root.columnconfigure(0,weight=1)

















root.mainloop()