import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageDraw
from datetime import datetime

# Sample data for receipt
company_name = "Beauty Essentials"
customer_name = "Jane Doe"
product_list = [
    {"name": "Lipstick", "price": 1500.00, "quantity": 2},
    {"name": "Foundation", "price": 3000.00, "quantity": 1},
    {"name": "Mascara", "price": 1000.00, "quantity": 3},
]

# Calculate total
total_price = sum(item["price"] * item["quantity"] for item in product_list)

# Generate receipt content
receipt_content = f"{company_name}\n\n"
receipt_content += f"Customer: {customer_name}\n"
receipt_content += f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
receipt_content += "Items Purchased:\n"
for item in product_list:
    receipt_content += f"{item['name']} (x{item['quantity']}): ₹{item['price'] * item['quantity']:.2f}\n"
receipt_content += f"\nTotal: ₹{total_price:.2f}\n"

# Function to save receipt as an image
def save_receipt_as_image():
    # Use file dialog to get save location and file type
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpeg")])
    if not file_path:  # If no file is selected, return
        return
    
    # Create an image with the receipt content
    font_size = 20
    padding = 10
    width = 400
    height = padding * 2 + font_size * (len(receipt_content.splitlines()) + 1)
    
    # Create a blank image with white background
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    
    # Draw text on the image
    draw.text((padding, padding), receipt_content, fill="black")
    
    # Save the image to the selected file path
    image.save(file_path)
    messagebox.showinfo("Saved", f"Receipt saved as an image at {file_path}")

# Tkinter GUI
root = tk.Tk()
root.title("Receipt Generator")

text = tk.Text(root, height=15, width=40)
text.insert(tk.END, receipt_content)
text.config(state="disabled")  # Make text read-only
text.pack()

save_button = tk.Button(root, text="Download Receipt as Image", command=save_receipt_as_image)
save_button.pack()

root.mainloop()
