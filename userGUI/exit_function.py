import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from datetime import datetime
import pytz
# INITIAL VARIABLES HERE
def Main_exit_page(content, return_to_idle):
    exit_page = tk.Frame(content)
    exit_page.place(relx=0, rely=0, relwidth=1, relheight=1)

    
    ww = exit_page.winfo_screenwidth()
    wh = exit_page.winfo_screenheight()
    time_border = ctk.CTkFrame(exit_page, width=(0.08 * ww), height=(0.067 * wh), fg_color="azure3", 
                      corner_radius=13, border_width=15, border_color="azure3")
    time_border.place(relx=0.89, rely=0.05)

    date_border = ctk.CTkFrame(exit_page, width=(0.13 * ww), height=(0.069 * wh), fg_color="azure3", 
                      corner_radius=13, border_width=15, border_color="azure3")
    date_border.place(relx=0.03, rely=0.05)

    def update_date():
        ph_timezone = pytz.timezone("Asia/Manila")
        current_time = datetime.now(ph_timezone)
        formatted_date = current_time.strftime("%B %d, %Y")
        formatted_time = current_time.strftime("%I:%M %p")
        date_label.configure(text=formatted_date)
        time_label.configure(text=formatted_time)
        content.after(1000, update_date)

    date_label = ctk.CTkLabel(date_border, font=("Arial", 24, 'bold'), text_color="Black")
    date_label.place(relx=0.07, rely=0.2)

    time_label = ctk.CTkLabel(time_border, font=("Arial", 24, 'bold'), text_color="Black")
    time_label.place(relx=0.07, rely=0.2)
    update_date()
    # Box
    frame = tk.Frame(exit_page, bg="white", bd=0)
    frame.place(relx=0.5, rely=0.5, anchor="center", width=(0.58 * ww), height=(0.65 * wh))
    
    # Text
    message = tk.Label(frame, text="Are you sure you want\nto log out?", font=("Arial", 40, "bold"), bg="white", fg="black")
    message.place(relx=0.5, rely=0.4, anchor="center")

    # Log out Button
    logout_btn = tk.Button(frame, text="LOG OUT", font=("Arial", 20, "bold"), bg="#004aad", fg="white", activebackground="gray", activeforeground="black", padx=20, pady=10, bd=0, command = return_to_idle)
    logout_btn.place(relx=0.5, rely=0.6, anchor="center")
    exit_page.tkraise(exit_page)