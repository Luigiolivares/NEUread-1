import tkinter as tk
from datetime import datetime
import pytz
import customtkinter as ctk
from PIL import Image, ImageTk, ImageDraw
import io
import os

# Initialize main window
root = tk.Tk()
root.title("History")
root.attributes('-fullscreen', True)

# We'll use a CTkFrame for the history page
history_page = ctk.CTkFrame(root, fg_color="light gray")
history_page.pack(fill="both", expand=True)

# Header frame for the date and university label
header_frame = ctk.CTkFrame(history_page, fg_color="white", height=100)
header_frame.pack(fill="x")

def update_date():
    ph_timezone = pytz.timezone("Asia/Manila")
    current_time = datetime.now(ph_timezone)
    formatted_time = current_time.strftime("%B %d, %Y %I:%M %p")
    date_label.configure(text=formatted_time)
    history_page.after(1000, update_date)

date_label = ctk.CTkLabel(header_frame, font=("Arial", 20), text_color="#333333", fg_color="white")
date_label.pack(side="left", padx=30)
update_date()

university_label = ctk.CTkLabel(header_frame, text="New Era University", font=("Arial", 20), fg_color="white", text_color="black")
university_label.place(relx=0.98, rely=0.5, anchor="e")

title_label = ctk.CTkLabel(history_page, text="Book History", font=("Arial", 30, "bold"), fg_color="light gray", text_color="#014aad")
title_label.place(relx=0.5, rely=0.15, anchor="center")

# Create a frame box for the content
frame_box = ctk.CTkFrame(history_page, width=1100, height=600, fg_color="white", corner_radius=15, border_width=5, border_color="#014aad")
frame_box.place(relx=0.5, rely=0.23, anchor="n")

# --- Create Round Buttons with Icons ---
def create_round_button_1():
    # load image using PIL and convert to CTkImage
    try:
        image = Image.open("back.png")
        image = image.resize((40, 40))
        tk_image = ctk.CTkImage(light_image=image, size=(40, 40))
    except Exception as e:
        print(f"Error loading back.png: {e}")
        return

    round_button = ctk.CTkButton(frame_box, image=tk_image, text="", fg_color="white", hover_color="lightgray", width=30, height=70)
    round_button.place(relx=0.93, rely=0.1, anchor="e")
    round_button.image = tk_image

create_round_button_1()

def create_round_button_2():
    try:
        image = Image.open("next.png")
        image = image.resize((40, 40))
        tk_image = ctk.CTkImage(light_image=image, size=(40, 40))
    except Exception as e:
        print(f"Error loading next.png: {e}")
        return

    round_button = ctk.CTkButton(frame_box, image=tk_image, text="", fg_color="white", hover_color="lightgray", width=30, height=70)
    round_button.place(relx=0.99, rely=0.1, anchor="e")
    round_button.image = tk_image

create_round_button_2()

# --- Create Book Buttons with Hover Effect ---
def insert_book_buttons():
    """
    Instead of inserting plain labels for book covers,
    create CTkButtons for each book that change appearance on hover.
    """
    # List of book cover file paths
    picture_paths = [
        "book1.jpeg",
        "book2.jpeg",
        "book3.jpeg"
    ]
    
    # Loop through each book cover and create a button
    for i, path in enumerate(picture_paths):
        try:
            image = Image.open(path)
            image = image.resize((100, 150))
            # Create a CTkImage for proper scaling
            ctk_image = ctk.CTkImage(light_image=image, size=(100, 150))
        except Exception as e:
            print(f"Error loading {path}: {e}")
            continue

        # Create a CTkButton that uses the image and displays a book title (optional)
        book_button = ctk.CTkButton(history_page,
                                    text=f"Book {i+1}",
                                    image=ctk_image,
                                    compound="top",      # Display text above or below image as desired
                                    fg_color="white",
                                    hover_color="lightblue",  # Hover color change
                                    text_color="black",
                                    font=("Arial", 14, "bold"))
        # Place the button with some vertical spacing for each book
        book_button.place(relx=0.18, rely=0.38 + (i * 0.20), anchor="w")
        book_button.image = ctk_image  # Keep a reference

insert_book_buttons()

# --- Additional Labels for Book Titles, Authors, etc. ---
book_titles = [
    ("Harry Potter And The Chamber of Secrets", 0.28, 0.33),
    ("Merriam-Webster Pocket Dictionary", 0.28, 0.55),
    ("Why it works... 100 Steps for Science And How It Happens", 0.28, 0.73)
]
for text, relx, rely in book_titles:
    ctk.CTkLabel(history_page, text=text, font=("Arial", 14, "bold"), fg_color="white", text_color="black", wraplength=350, justify="left").place(relx=relx, rely=rely)

authors = [
    ("By J. K. Rowling", 0.28, 0.38),
    ("By Noah Webster", 0.28, 0.58),
    ("By Dr. Lisa Gillespie", 0.28, 0.79)
]
for text, relx, rely in authors:
    ctk.CTkLabel(history_page, text=text, font=("Arial", 14), fg_color="white", text_color="black").place(relx=relx, rely=rely)

borrowed_positions = [(0.60, 0.33), (0.60, 0.55), (0.60, 0.73)]
for relx, rely in borrowed_positions:
    ctk.CTkLabel(history_page, text="Borrowed:", font=("Arial", 13, "bold"), text_color="red", fg_color="white").place(relx=relx, rely=rely)

return_dates_positions = [(0.60, 0.36), (0.60, 0.58), (0.60, 0.76)]
for relx, rely in return_dates_positions:
    ctk.CTkLabel(history_page, text="Returned:", font=("Arial", 13, "bold"), text_color="red", fg_color="white").place(relx=relx, rely=rely)

borrowed_dates = [
    ("Date borrowed1", 0.66, 0.33),
    ("Date borrowed2", 0.66, 0.55),
    ("Date borrowed3", 0.66, 0.73)
]
for text, relx, rely in borrowed_dates:
    ctk.CTkLabel(history_page, text=text, font=("Arial", 13), fg_color="white", text_color="black").place(relx=relx, rely=rely)

returned_dates = [
    ("Date returned1", 0.66, 0.36),
    ("Date returned2", 0.66, 0.58),
    ("Date returned3", 0.66, 0.76)
]
for text, relx, rely in returned_dates:
    ctk.CTkLabel(history_page, text=text, font=("Arial", 13), fg_color="white", text_color="black").place(relx=relx, rely=rely)

# Start the main loop
root.mainloop()
