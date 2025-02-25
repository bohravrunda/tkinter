import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

class RailwayTicketBooking:
    def _init_(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.root.title("Railway Ticket Booking System")
        self.root.configure(bg="#C8A2C8")

        tk.Label(self.root, text="RAILWAY TICKET BOOKING", fg="black", font=("Arial", 16)).pack(padx=10, pady=10, fill="x")

        # Train Details with timings and corresponding stations
        self.trains = {
            "Train NAGARKOLI": {
                "available": 50, "price": 100, "time": "10:00 AM",
                "stations": [("Delhi", "Mumbai"), ("Mumbai", "Delhi")]
            },
            "Train KANYAKUMARI": {
                "available": 30, "price": 150, "time": "12:00 PM",
                "stations": [("Chennai", "Kanyakumari"), ("Kanyakumari", "Chennai")]
            },
            "Train MUMBAI EXPRESS": {
                "available": 20, "price": 200, "time": "02:00 PM",
                "stations": [("Mumbai", "Ahmedabad"), ("Ahmedabad", "Mumbai")]
            },
            "Train DANAPUR EXPRESS": {
                "available": 30, "price": 300, "time": "04:00 PM",
                "stations": [("Patna", "Kolkata"), ("Kolkata", "Patna")]
            },
            "Train DURONTO": {
                "available": 20, "price": 250, "time": "06:00 PM",
                "stations": [("Delhi", "Jaipur"), ("Jaipur", "Delhi")]
            }
        }

        # User Input Fields
        self.train_var = tk.StringVar(value=list(self.trains.keys())[0])
        self.passenger_count_var = tk.IntVar()
        self.source_var = tk.StringVar()
        self.destination_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.place(relx=0.5, rely=0.5, anchor='center')

        tk.Label(frame, text="Select Train:", bg="rosybrown", fg="white").grid(row=0, column=0, padx=10, pady=10)
        self.train_menu = tk.OptionMenu(frame, self.train_var, *self.trains.keys(), command=self.update_stations)
        self.train_menu.grid(row=0, column=1, padx=10, pady=10)

        self.train_info = tk.Label(frame, text="", fg="blue")
        self.train_info.grid(row=1, columnspan=2, pady=5)

        tk.Label(frame, text="Source:", bg="rosybrown", fg="white").grid(row=2, column=0, padx=10, pady=10)
        self.source_combo = ttk.Combobox(frame, textvariable=self.source_var)
        self.source_combo.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(frame, text="Destination:", bg="rosybrown", fg="white").grid(row=3, column=0, padx=10, pady=10)
        self.destination_combo = ttk.Combobox(frame, textvariable=self.destination_var)
        self.destination_combo.grid(row=3, column=1, padx=10, pady=10)

        tk.Label(frame, text="Number of Passengers:", bg="rosybrown", fg="white").grid(row=4, column=0, padx=10, pady=10)
        tk.Entry(frame, textvariable=self.passenger_count_var).grid(row=4, column=1, padx=10, pady=10)

        tk.Button(frame, text="Book Ticket", command=self.book_ticket, bg="rosybrown", fg="white").grid(row=5, columnspan=2, pady=20)

        self.download_button = tk.Button(frame, text="Download Receipt", command=self.download_receipt, bg="rosybrown", fg="white", state=tk.DISABLED)
        self.download_button.grid(row=6, columnspan=2, pady=5)

        tk.Button(frame, text="Reset", command=self.reset_fields, bg="rosybrown", fg="white").grid(row=7, columnspan=2, pady=5)

        self.update_stations()  # Initialize source and destination based on the default train

    def update_stations(self, *args):
        train_name = self.train_var.get()
        if train_name:
            details = self.trains[train_name]
            self.train_info.config(text=f"Price: ${details['price']}, Available: {details['available']}, Time: {details['time']}")
            # Update source and destination options based on the selected train
            stations = details['stations'][0]  # Get the first route for source and destination
            self.source_combo['values'] = [station[0] for station in details['stations']]
            self.destination_combo['values'] = [station[1] for station in details['stations']]
            self.source_var.set(stations[0])  # Set default source
            self.destination_var.set(stations[1])  # Set default destination

    def book_ticket(self):
        train_name = self.train_var.get()
        passenger_count = self.passenger_count_var.get()
        source = self.source_var.get()
        destination = self.destination_var.get()

        if not train_name or passenger_count <= 0 or not source or not destination:
            messagebox.showerror("Input Error", "Please fill in all fields correctly.")
            return

        train_details = self.trains[train_name]

        if train_details["available"] < passenger_count:
            messagebox.showerror("Booking Error", "Not enough tickets available.")
            return

        total_cost = train_details["price"] * passenger_count

        if not messagebox.askyesno("Payment Confirmation", f"Total Cost: ${total_cost}. Proceed with payment?"):
            return

        train_details["available"] -= passenger_count
        self.download_button.config(state=tk.NORMAL)

        self.receipt_image_data = self.generate_receipt(train_name, passenger_count, total_cost, source, destination)

        messagebox.showinfo("Booking Confirmed", f"Tickets booked successfully!\nTotal Cost: ${total_cost}\nRemaining Tickets: {train_details['available']}")

    def generate_receipt(self, train_name, passenger_count, total_cost, source, destination):
        width, height = 400, 300
        receipt_image = Image.new("RGB", (width, height), color="white")
        draw = ImageDraw.Draw(receipt_image)

        font = ImageFont.load_default()

        receipt_text = (
            f"Ticket Confirmation\n"
            f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"Train: {train_name}\n"
            f"Source: {source}\n"
            f"Destination: {destination}\n"
            f"Passengers: {passenger_count}\n"
            f"Total Cost: ${total_cost}\n"
            f"Thank you for booking!"
        )

        draw.multiline_text((10, 10), receipt_text, fill="black", font=font)
        return receipt_image

    def download_receipt(self):
        if hasattr(self, 'receipt_image_data'):
            file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                       filetypes=[("PNG files", ".png"), ("All files", ".*")])
            if file_path:
                self.receipt_image_data.save(file_path)
                messagebox.showinfo("Receipt Downloaded", f"Your receipt has been saved as '{file_path}'.")

    def reset_fields(self):
        self.train_var.set(list(self.trains.keys())[0])
        self.passenger_count_var.set(0)
        self.source_var.set("")
        self.destination_var.set("")
        self.train_info.config(text="")
        self.download_button.config(state=tk.DISABLED)
        self.update_stations()

if _name_ == "_main_":
    root = tk.Tk()
    app = RailwayTicketBooking(root)
    root.mainloop()