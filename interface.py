import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Beauty Product Interface")
root.geometry("1200x700")

# Set a soft lavender background color
root.configure(bg='#E6E6FA')  # Light lavender color

def search_product():
    print(f"Searching for: {search_entry.get()}")

def exclusive_offer():
    print("Exclusive offer clicked")

# Offer Label
offer_label = tk.Button(root, text="NEW CUSTOMER? 10% OFF ON YOUR 1st ORDER", bg='lightblue', fg='black', font=("Arial", 12, "bold"))
offer_label.pack(side='top', fill='x', pady=10)

# Navigation Bar
nav_bar = tk.Frame(root, bg="#C9C3E6")
nav_bar.pack(fill="x")

web_name = tk.Label(nav_bar, text='Vruya Essence', font=("Arial", 16, "bold"), bg="#C9C3E6", fg='black')
web_name.pack(side="left", padx=10)

search_frame = tk.Frame(nav_bar, bg="#C9C3E6")
search_frame.pack(side="right", padx=10, pady=5)

search_entry = tk.Entry(search_frame, width=20, bg='white', fg='black')
search_entry.pack(side="left")

search_button = tk.Button(search_frame, text="Search", command=search_product, bg='lightgreen', fg='black')
search_button.pack(side="left", padx=5)

exclusive_offer_button = tk.Button(search_frame, text="Exclusive Offers", font=("Arial", 12), bg="orange", fg='black', command=exclusive_offer)
exclusive_offer_button.pack(side="left", padx=5)

button_frame = tk.Frame(root)
button_frame.pack(side="top", anchor="w", padx=10, pady=5)

login_button = tk.Button(button_frame, text="Login", width=20, bg="lightblue", fg='black')
login_button.pack(side="left", padx=5)

signup_button = tk.Button(button_frame, text="Sign Up", width=20, bg="lightblue", fg='black')
signup_button.pack(side="left", padx=5)

category_frame = tk.Frame(root)
category_frame.pack(side="top", fill="x", padx=10, pady=20)

makeup_button = tk.Button(category_frame, text="Makeup", width=30, bg="lightpink", fg='black')
makeup_button.pack(side="left", padx=5)

hair_button = tk.Button(category_frame, text="Hair", width=30, bg="skyblue", fg='black')
hair_button.pack(side="left", padx=5)

baby_button = tk.Button(category_frame, text="Baby", width=30, bg="lightyellow", fg='black')
baby_button.pack(side="left", padx=5)

gifts_button = tk.Button(category_frame, text="Gifts", width=30, bg="lime", fg='black')
gifts_button.pack(side="left", padx=5)

face_button = tk.Button(category_frame, text="Face", width=30, bg="#EEE8AA", fg='black')
face_button.pack(side="left", padx=5)

combos_button = tk.Button(category_frame, text="Combos", width=30, bg="#FFA07A", fg='black')
combos_button.pack(side="left", padx=5)

canvas = tk.Canvas(root, width=1500, height=800, bg='#F9F9F9')  # Keep the light grey for canvas
canvas.pack(side="left")

# Circle and rectangle setup
radius = 95
circle_rect_gap = 30
label_rect_gap = 35
button_gap = 20
slider_gap = 10
y = 100

# Track circle and product positions
circle_positions = [300, 520, 740, 960, 1180]
circle_texts = ["Trend and Products", "Lightning and Sale!!", "Summer Favourites", "Fragrances", "New Product"]
product_names = ["Product", "Hair Product", "Face Toner", "Shampoo", "New Product"]

# Load images with resizing
def load_image(image_path, size):
    try:
        image = Image.open(image_path)
        image = image.resize(size, Image.LANCZOS)
        return ImageTk.PhotoImage(image)
    except Exception as e:
        print(f"Failed to load image from {image_path}: {e}")
        return None

# Load images
product_images = {
    "Product": load_image("C:\\Users\\Lenovo\\Downloads\\tkinter.images\\download.png", (150, 200)),
    "Hair Product": load_image("C:\\Users\\Lenovo\\Downloads\\tkinter.images\\nykaa.png", (150, 200)),
    "Face Toner": load_image("C:\\Users\\Lenovo\\Downloads\\tkinter.images\\tonner.png", (150, 200)),
    "Shampoo": load_image("C:\\Users\\Lenovo\\Downloads\\tkinter.images\\shamp.png", (150, 200)),
    "New Product": load_image("C:\\Users\\Lenovo\\Downloads\\tkinter.images\\perfume.png", (150, 200)),
}

# Create and store circle and rectangle objects
circles = []
texts = []
rectangles = []
buttons = []

# Function to create circles and rectangles dynamically
def create_circles_and_rectangles():
    canvas.delete("all")  # Clear the canvas before re-drawing
    for i, x in enumerate(circle_positions):
        # Create circles
        circle = canvas.create_oval(x - radius, y - radius, x + radius, y + radius, outline="#C7B8EA", width=2, fill="#C7B8EA")
        circles.append(circle)
        text = canvas.create_text(x, y, text=circle_texts[i], fill="black", font=("Arial", 12, "bold"))
        texts.append(text)

    # Position for the label
    label_y_position = y + radius + circle_rect_gap

    # New Launches Label
    canvas.create_text((circle_positions[0] + circle_positions[-1]) / 2, label_y_position,
                       text="New Launches !!", fill="black", font=("Arial", 16, "bold"))

    for i, x in enumerate(circle_positions):
        # Create product rectangles
        rect_x = x + 15
        img = product_images.get(product_names[i])

        if img:
            rect_width = img.width()
            rect_height = img.height()

            rectangle = canvas.create_rectangle(rect_x - rect_width // 2, label_y_position + label_rect_gap,
                                                rect_x + rect_width // 2, label_y_position + label_rect_gap + rect_height,
                                                fill="lightgrey", outline="black", width=1)
            rectangles.append(rectangle)

            # Center image in the rectangle
            canvas.create_image(rect_x, label_y_position + label_rect_gap + rect_height / 2, image=img, anchor='center')

            # Create "Add to Cart" button
            add_to_cart_button = tk.Button(root, text="Add to Cart", bg="lightblue", fg='black',
                                           command=lambda name=product_names[i]: print(f"Added {name} to Cart"))
            button_window = canvas.create_window(rect_x, label_y_position + label_rect_gap + rect_height + button_gap,
                                                 window=add_to_cart_button)
            buttons.append(button_window)

    # Position sliders next to the first and last circles
    left_circle_slider = tk.Button(root, text="◀", command=slide_left_circles, width=3, height=2, bg="orange", fg='black')
    canvas.create_window(circle_positions[0] - radius - 40, y, window=left_circle_slider)

    right_circle_slider = tk.Button(root, text="▶", command=slide_right_circles, width=3, height=2, bg="orange", fg='black')
    canvas.create_window(circle_positions[-1] + radius + 40, y, window=right_circle_slider)

    # Position sliders below the rectangles, offset further left and right
    left_rect_slider = tk.Button(root, text="◀", command=slide_left_rectangles, width=3, height=2, bg="orange", fg='black')
    canvas.create_window(circle_positions[0] + 15 - 110, label_y_position + label_rect_gap + 50, window=left_rect_slider)

    right_rect_slider = tk.Button(root, text="▶", command=slide_right_rectangles, width=3, height=2, bg="orange", fg='black')
    canvas.create_window(circle_positions[-1] + 15 + 110, label_y_position + label_rect_gap + 50, window=right_rect_slider)

# Update circle positions when sliding
def slide_left_circles():
    for i in range(len(circle_positions)):
        circle_positions[i] -= 240  # Shift circles to the left
    create_circles_and_rectangles()

def slide_right_circles():
    for i in range(len(circle_positions)):
        circle_positions[i] += 240  # Shift circles to the right
    create_circles_and_rectangles()

# Update rectangle positions when sliding
def slide_left_rectangles():
    for i in range(len(circle_positions)):
        circle_positions[i] -= 240  # Shift rectangles to the left
    create_circles_and_rectangles()

def slide_right_rectangles():
    for i in range(len(circle_positions)):
        circle_positions[i] += 240  # Shift rectangles to the right
    create_circles_and_rectangles()

# Initial creation of circles and rectangles
create_circles_and_rectangles()

root.mainloop()