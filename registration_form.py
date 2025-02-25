import tkinter
from tkinter import ttk
from tkinter import messagebox

import tkinter.messagebox

def enter_data():
    accepted=accept_var.get()
    if accepted=="Accepted":
        fname=name_entry.get()
        lastname=lname_entry.get()
        age=age_spinbox.get()
        gen=gen_combobox.get()
        nat=nat_combobox.get()
        add=add_entry.get()
        pin=pin_entry.get()
        em=e_entry.get()
        ph=ph_entry.get()
        terms=terms_check.get()
    else:
        tkinter.messagebox.showwarning(title="Error",message="You have not accepted terms")



root=tkinter.Tk()
frame=tkinter.Frame(root)
frame.pack()

user_info_frame=tkinter.LabelFrame(frame,text="user information")
user_info_frame.grid(row=0 ,column=0,padx=20,pady=20)



root.geometry("600x400")


root.title("student registration form")
name_label=tkinter.Label(user_info_frame,text=" First Name")
name_label.grid(row=0 ,column=0)
lname_label=tkinter.Label(user_info_frame,text="Last Name")
lname_label.grid(row=0 ,column=1)

name_entry=tkinter.Entry(user_info_frame)
lname_entry=tkinter.Entry(user_info_frame)
name_entry.grid(row=1 ,column=0)
lname_entry.grid(row=1 ,column=1)



gen_label=tkinter.Label(user_info_frame,text=" Gender")
gen_combobox=ttk.Combobox(user_info_frame,values=["","F","M"])
gen_label.grid(row=0,column=2)
gen_combobox.grid(row=1,column=2)

age_label=tkinter.Label(user_info_frame,text="Age")
age_spinbox=tkinter.Spinbox(user_info_frame,from_=18,to=30)
age_label.grid(row=2,column=0)
age_spinbox.grid(row=3,column=0)

nat_label=tkinter.Label(user_info_frame,text=" Nationality")
nat_combobox=ttk.Combobox(user_info_frame,values=["Asia", "Africa", "North America", "South America", "Antarctica", "Europe", " Australia"])
nat_label.grid(row=2,column=1)
nat_combobox.grid(row=3,column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

c_frame= tkinter.LabelFrame(frame)
c_frame.grid(row=1,column=0,sticky="news",padx=20,pady=20)

e_label=tkinter.Label(c_frame,text=" Email")
e_label.grid(row=0,column=0)
ph_label=tkinter.Label(c_frame,text="Phone No.")
ph_label.grid(row=0 ,column=1)

e_entry=tkinter.Entry(c_frame)
ph_entry=tkinter.Entry(c_frame)
e_entry.grid(row=1,column=0)
ph_entry.grid(row=1,column=1)

add_label=tkinter.Label(c_frame,text=" Address")
add_label.grid(row=0,column=2)
pin_label=tkinter.Label(c_frame,text="Pincode")
pin_label.grid(row=2,column=0)

add_entry=tkinter.Entry(c_frame)
pin_entry=tkinter.Entry(c_frame)
add_entry.grid(row=1,column=2)
pin_entry.grid(row=3,column=0)

for widget in c_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

    terms_frame=tkinter.LabelFrame(frame,text="Terms & conditions")
    terms_frame.grid(row=2 , column=0,sticky="news",padx=20,pady=20)

    accept_var=tkinter.StringVar(value="Not Accepted")
    terms_check=tkinter.Checkbutton(terms_frame,text="I accept and continue",
                                    variable=accept_var,onvalue="Accepted", offvalue="Not Accepted")
    terms_check.grid(row=0,column=0)

    button= tkinter.Button(frame,text="Enter data",command=enter_data)
    button.grid(row=3,column=0,sticky="news",padx=20,pady=20)










root.mainloop()