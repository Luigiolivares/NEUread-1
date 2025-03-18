import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from datetime import datetime

# INITIAL VARIABLES HERE
def Main_exit_page(content, return_to_idle):
    exit_page = tk.Frame(content)
    exit_page.place(x=0, y=0, width=1720, height=1080)

    # Box
    frame = tk.Frame(exit_page, bg="white", bd=0)
    frame.place(x=245, y=95, width=1000, height=700)

    # Date
    today = datetime.today().strftime("%d %B, %Y")
    date_label = tk.Label(exit_page, text=today, font=('Arial', 18, 'bold'), bg='#f2f3f7', fg='black')
    date_label.place(x=35, y=50)

    # Time
    current_time = datetime.now().strftime("%I:%M %p")
    time_label = tk.Label(exit_page, text=current_time, font=('Arial', 18, 'bold'), bg='#9dabbe', fg='black', padx=10, pady=4)
    time_label.place(x=frame.winfo_screenwidth()-220, y=50)

    # Text
    message = tk.Label(frame, text="Are you sure you want\nto log out?", font=("Arial", 40, "bold"), bg="white", fg="black")
    message.place(relx=0.5, rely=0.4, anchor="center")

    # Log out Button
    logout_btn = tk.Button(frame, text="LOG OUT", font=("Arial", 20, "bold"), bg="#004aad", fg="white", activebackground="gray", activeforeground="black", padx=20, pady=10, bd=0, command = return_to_idle)
    logout_btn.place(relx=0.5, rely=0.6, anchor="center")
    exit_page.tkraise(exit_page)