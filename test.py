import customtkinter as ctk
from tkinter import filedialog
import mysql.connector
from bnd import *
# Function to open form
import tkinter.messagebox as messagebox
import customtkinter as ctk
from tkinter import filedialog

def open_book_form():
    form = ctk.CTkToplevel()
    form.geometry("700x450")
    form.title("Add Book Entry")

    entries = {}
    fields = [
        ("Book_ID", int), ("Title", str), ("Author", str), ("Description", str),
        ("Availability", int), ("Genre", str), ("Year_Publication", int), ("Book_Address", str)
    ]

    for i, (field, _) in enumerate(fields):
        label = ctk.CTkLabel(form, text=field)
        label.grid(row=i, column=0, padx=10, pady=5, sticky='e')
        entry = ctk.CTkEntry(form, width=400)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries[field] = entry

    # File selector for image
    def choose_image():
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        image_path_var.set(file_path)

    image_path_var = ctk.StringVar()
    ctk.CTkLabel(form, text="Book_Cover").grid(row=len(fields), column=0, padx=10, pady=5, sticky='e')
    ctk.CTkEntry(form, textvariable=image_path_var, width=300, state="readonly").grid(row=len(fields), column=1, padx=10, pady=5, sticky='w')
    ctk.CTkButton(form, text="Browse", command=choose_image).grid(row=len(fields), column=2, padx=5)

    # Submit button
    def submit():
        # Validate that all fields are filled and the image is selected
        for field in fields:
            field_name = field[0]
            if not entries[field_name].get():
                messagebox.showerror("Input Error", f"The {field_name} field is required!")
                return
        
        if not image_path_var.get():
            messagebox.showerror("Input Error", "Book cover image is required!")
            return

        # Proceed with submitting the form
        data = {field[0]: field[1](entries[field[0]].get()) for field in fields}
        data['Book_Cover'] = image_path_var.get()

        try:
            insert_book(data)  # Assuming insert_book is defined elsewhere
            messagebox.showinfo("Success", "Book added successfully!")
            form.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while adding the book: {str(e)}")

    submit_btn = ctk.CTkButton(form, text="Submit", command=submit)
    submit_btn.grid(row=len(fields)+1, column=1, pady=20)

    form.mainloop()



# Main window setup
root = ctk.CTk()
root.geometry("400x200")
root.title("Library System")

add_button = ctk.CTkButton(root, text="Add Book", command=open_book_form)
add_button.pack(pady=60)

root.mainloop()
