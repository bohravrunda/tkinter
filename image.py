import tkinter as tk
from PIL import Image, ImageTk
from dashboard import open_dashboard  # Ensure this function exists in dashboard.py

def open_dashboard_window():
    root.destroy()  # Close the current window
    open_dashboard()  # Open the dashboard

root = tk.Tk()
root.title("Timetable Generator")
root.geometry("1200x700")
root.configure(bg="#F5F5F5")

nav_bar = tk.Frame(root, bg="lightblue", height=80)
nav_bar.pack(fill="x")

nav_label = tk.Label(nav_bar, text="TimeTablet", bg="#3C8DAD", font=("Arial", 24, "bold"), fg="#FFFFFF")
nav_label.pack(side="left", padx=20, pady=20)

home_button = tk.Button(nav_bar, text="Home", bg="#5AB3E1", fg="#FFFFFF", relief="raised", font=("Arial", 12))
home_button.pack(side="right", padx=10, pady=20)

login_button = tk.Button(nav_bar, text="Login", bg="#FFA07A", fg="#FFFFFF", relief="raised", font=("Arial", 12))
login_button.pack(side="right", padx=10, pady=20)

try:
    image_path = r"/home/bohra/Desktop/timetable/dbmsy.png"
    image = Image.open(image_path)
    new_width = 1200
    new_height = int(image.height * (new_width / image.width))
    image = image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)

    image_frame = tk.Frame(root)
    image_frame.pack(pady=20)

    image_label = tk.Label(image_frame, image=photo)
    image_label.pack(fill="both")

    # Modify the start button to open the dashboard
    start_button = tk.Button(image_frame, text="Start", bg="#FF8C00", fg="#FFFFFF", width=10, font=("Arial", 14, "bold"), command=open_dashboard_window)
    start_button.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

    image_label.image = photo

except Exception as e:
    print(f"Error loading image: {e}")

root.mainloop()