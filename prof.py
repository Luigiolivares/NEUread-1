import tkinter as tk
import customtkinter as ctk
from datetime import datetime

# Initialize main window
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.attributes('-zoomed', True)

content = ctk.CTkFrame(root)
content.pack(fill="both", expand=True)

def calculate_penalty(due_date):
    today = datetime.today().date()
    due_date = datetime.strptime(due_date, "%b %d, %Y").date()
    overdue_days = (today - due_date).days
    return max(0, overdue_days * 10)  

def display_due_date(parent, book):
    due_date_label = ctk.CTkLabel(parent, text=f"Due: {book['due_date']}", text_color="black", font=("Arial", 20))
    due_date_label.place(relx=0.5, rely=0.8, anchor="ne") #Beside the book and author

def display_due_date(parent, book):
    due_date_label = ctk.CTkLabel(parent, text=f"Due: {book['due_date']}", text_color="red", font=("Arial", 20))
    due_date_label.place(relx=0.95, rely=0.6, anchor="e")  # Positioned beside the author

def display_borrowed_books(parent, borrowed_books):
    books_container = ctk.CTkFrame(parent, width=500, height=400, fg_color="white")
    books_container.place(relx=0.25, rely=0.2, anchor="n")  # Centered below "Current Borrowed Books"

    for book in borrowed_books:
        book_frame = ctk.CTkFrame(books_container, width=400, height=100, fg_color="lightgray", corner_radius=10)
        book_frame.pack(pady=10, padx=10, anchor="center")

        title_label = ctk.CTkLabel(book_frame, text=book['title'], text_color="black", font=("Arial", 25, "bold"))
        title_label.place(relx=0.05, rely=0.3, anchor="w")

        author_label = ctk.CTkLabel(book_frame, text=f"by {book['author']}", text_color="black", font=("Arial", 20))
        author_label.place(relx=0.05, rely=0.6, anchor="w")

        display_due_date(book_frame, book)  # Due date aligns beside the author

def display_penalties(parent, borrowed_books):
    penalties_container = ctk.CTkFrame(parent, width=500, height=400, fg_color="white")
    penalties_container.place(relx=0.75, rely=0.2, anchor="n")  # Centered below "Penalty"

    for book in borrowed_books:
        penalty_amount = calculate_penalty(book["due_date"])
        if penalty_amount > 0:
            penalty_frame = ctk.CTkFrame(penalties_container, width=400, height=100, fg_color="lightgray", corner_radius=10)
            penalty_frame.pack(pady=10, padx=10, anchor="center")

            title_label = ctk.CTkLabel(penalty_frame, text=book["title"], text_color="black", font=("Arial", 25, "bold"))
            title_label.place(relx=0.05, rely=0.5, anchor="w")

            amount_label = ctk.CTkLabel(penalty_frame, text=f"Penalty: ₱{penalty_amount}", text_color="red", font=("Arial", 20))
            amount_label.place(relx=0.95, rely=0.5, anchor="e")  # Right-aligned beside the title

def Main_user_page(content, profileInfo, borrowed_books):
    name = profileInfo[0][0][1]
    user_role = "Student"

    user_page = ctk.CTkFrame(content)
    user_page.pack(fill="both", expand=True)

    name_box = ctk.CTkFrame(user_page, width=1600, height=150, fg_color="white", corner_radius=20)
    name_box.pack(pady=70, padx=50)

    name_label = ctk.CTkLabel(name_box, text=name, text_color="black", font=("Times New Roman", 50, "bold"))
    name_label.place(relx=0.02, rely=0.35, anchor="w")

    role_label = ctk.CTkLabel(name_box, text=user_role, text_color="black", font=("Arial", 35))
    role_label.place(relx=0.02, rely=0.7, anchor="w")

    info_box = ctk.CTkFrame(user_page, width=1300, height=500, fg_color="white", corner_radius=20, border_width=5, border_color="royal blue")
    info_box.pack(pady=20, padx=50)

    borrowed_books_box = ctk.CTkFrame(info_box, width=400, height=50, fg_color="royal blue", corner_radius=15)
    borrowed_books_box.place(relx=0.25, rely=0.05, anchor="n")

    borrowed_books_label = ctk.CTkLabel(borrowed_books_box, text="Current Borrowed Books", text_color="white", font=("Times New Roman", 30))
    borrowed_books_label.place(relx=0.5, rely=0.5, anchor="center")

    penalty_box = ctk.CTkFrame(info_box, width=200, height=50, fg_color="royal blue", corner_radius=15)
    penalty_box.place(relx=0.75, rely=0.05, anchor="n")

    penalty_label = ctk.CTkLabel(penalty_box, text="Penalty", text_color="white", font=("Times New Roman", 30))
    penalty_label.place(relx=0.5, rely=0.5, anchor="center")

    # ADDING A SEPARATOR LINE
    separator = ctk.CTkFrame(info_box, width=5, height=300, fg_color="gray")
    separator.place(relx=0.5, rely=0.2, anchor="n")  # Placed in the center between the two sections

    display_borrowed_books(info_box, borrowed_books)
    display_penalties(info_box, borrowed_books)

    user_page.tkraise()

profileInfo = [[["User", "Tyler The Creator"]]]

borrowed_books = [
    {
        "title": "Marilag",
        "author": "Kuya Will",
        "due_date": "Feb 10, 2025"
    },
    {
        "title": "Ka Dick",
        "author": "Dick Gordon",
        "due_date": "Jan 31, 2025"
    }
]

Main_user_page(content, profileInfo, borrowed_books)
root.mainloop()