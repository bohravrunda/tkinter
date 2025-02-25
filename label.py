import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
root=tk.Tk()
root.geometry("500x600")
root.resizable(False,False)
label=ttk.Label(root,text="hello world",padding=20)
label.config(font=("Arial",20))
label.pack()

image=Image.open("hair.png")
photo=ImageTk.PhotoImage(image)
label_image=ttk.Label(root,image=photo,padding =20)
label_image.pack()

root.mainloop()