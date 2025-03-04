import customtkinter as ctk
from datetime import datetime
from pytz import timezone
from PIL import Image
import tkinter as tk

image_cache = {}

PH_TZ = timezone("Asia/Manila")

def get_philippine_time():
    return datetime.now(PH_TZ)

def load_image(filename, size=(100, 150)):
    if filename in image_cache:
        return image_cache[filename]
    
    try:
        pil_image = Image.open(filename)
        ctk_image = ctk.CTkImage(light_image=pil_image, size=size)
        image_cache[filename] = ctk_image
        return ctk_image
    except Exception as e:
        print(f"Error loading image {filename}: {e}")
        return None

def is_penalized(due_date, returned=False):
    today = get_philippine_time().date()
    due_date_obj = datetime.strptime(due_date, "%b %d, %Y").date()
    return due_date_obj < today and not returned

def display_due_date(parent, book, returned=False):
    penalized_status = is_penalized(book['due_date'], returned)
    due_date_text = "Due: " + book['due_date']
    text_color = "red" if penalized_status else "black"

    due_date_label = ctk.CTkLabel(parent, text=due_date_text, text_color=text_color, font=("Arial", 15, "bold"))
    due_date_label.place(relx=0.4, rely=0.7, anchor="w")

    return penalized_status

def Main_user_page(content, profileInfo):
    name = profileInfo[0][0][1]
    user_page = tk.Frame(content)
    user_page.place(x=0, y=0, relwidth=1, relheight=1)

    borrowed_books = [
        {"title": "Wimpy Kid", "author": "Jeff Kinney", "borrowed_date": "Feb 23, 2025", "due_date": "Feb 26, 2025", "image": "wimpy.png"},
        {"title": "Little Women", "author": "Louisa May Alcott", "borrowed_date": "Feb 23, 2025", "due_date": "Feb 26, 2025", "image": "little women.png"}
    ]

    name_box = ctk.CTkFrame(user_page, width=1600, height=150, fg_color="white", corner_radius=20)
    name_box.place(x=50, y=70)

    name_label = ctk.CTkLabel(name_box, text=name, text_color="black", font=("Times New Roman", 50, "bold"))
    name_label.place(relx=0.02, rely=0.3, anchor="w")

    id_label = ctk.CTkLabel(name_box, text="ID: 12345678", text_color="black", font=("Times New Roman", 22))
    id_label.place(relx=0.02, rely=0.6, anchor="w")

    role_label = ctk.CTkLabel(name_box, text="Student", text_color="black", font=("Times New Roman", 22))
    role_label.place(relx=0.02, rely=0.75, anchor="w")

    info_box = ctk.CTkFrame(user_page, width=1600, height=500, fg_color="white", corner_radius=20, border_width=5, border_color="royal blue")
    info_box.place(x=50, y=250)

    borrowed_books_frame = ctk.CTkFrame(info_box, fg_color="royalblue", corner_radius=10)
    borrowed_books_frame.place(relx=0.5, rely=0.05, anchor="n")

    borrowed_books_label = ctk.CTkLabel(borrowed_books_frame, text="Current Borrowed Books", text_color="black", font=("Times New Roman", 30, "bold"))
    borrowed_books_label.place(relx=0.5, rely=0.5, anchor="center")

    container_frame = ctk.CTkFrame(info_box, fg_color="white")
    container_frame.place(relx=0.5, rely=0.3, anchor="n", relwidth=0.9, relheight=0.6)

    left_container = ctk.CTkFrame(container_frame, fg_color="white", corner_radius=20)
    left_container.place(relx=0.25, rely=0.5, anchor="center", relwidth=0.45, relheight=1)

    separator = ctk.CTkFrame(container_frame, width=2, fg_color="gray")
    separator.place(relx=0.5, rely=0, relheight=1)

    right_container = ctk.CTkFrame(container_frame, fg_color="white", corner_radius=20)
    right_container.place(relx=0.75, rely=0.5, anchor="center", relwidth=0.45, relheight=1)

    penalized = False

    for index, book in enumerate(borrowed_books):
        target_container = left_container if index % 2 == 0 else right_container
        book_frame = ctk.CTkFrame(target_container, width=350, height=180, fg_color="white", corner_radius=10)
        book_frame.place(relx=0.5, rely=0.2 + (index * 0.4), anchor="center")

        book_image = load_image("book1.jpeg")
        if book_image:
            image_label = ctk.CTkLabel(book_frame, image=book_image, text="")
            image_label.image = book_image
            image_label.place(relx=0.1, rely=0.5, anchor="w")

        title_label = ctk.CTkLabel(book_frame, text=book['title'], text_color="black", font=("Times New Roman", 20, "bold"))
        title_label.place(relx=0.4, rely=0.2, anchor="w")

        author_label = ctk.CTkLabel(book_frame, text=f"by {book['author']}", text_color="black", font=("Times New Roman", 16))
        author_label.place(relx=0.4, rely=0.4, anchor="w")

        borrowed_date_label = ctk.CTkLabel(book_frame, text=f"Borrowed: {book['borrowed_date']}", text_color="black", font=("Times New Roman", 15))
        borrowed_date_label.place(relx=0.4, rely=0.55, anchor="w")

        if display_due_date(book_frame, book, returned=False):
            penalized = True

    if penalized:
        penalized_label = ctk.CTkLabel(user_page, text="Penalized", text_color="red", font=("Arial", 16, "bold"))
        penalized_label.place(relx=0.5, rely=0.9, anchor="center")
