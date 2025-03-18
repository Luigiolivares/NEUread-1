import customtkinter as ctk
import tkinter as tk
from PIL import Image
from datetime import datetime
import pytz

def penaltyPage(content):
    ww = content.winfo_screenwidth()
    wh = content.winfo_screenheight()
    borrow = tk.Frame(content)
    borrow.place(relx=0, rely=0, relwidth=1, relheight=1)

    time_border = ctk.CTkFrame(borrow, width=(0.08 * ww), height=(0.067 * wh), fg_color="azure3", 
                corner_radius=13, border_width=15, border_color="azure3")
    time_border.place(relx=0.89, rely=0.05)

    date_border = ctk.CTkFrame(borrow, width=(0.13 * ww), height=(0.069 * wh), fg_color="azure3", 
                      corner_radius=13, border_width=15, border_color="azure3")
    date_border.place(relx=0.03, rely=0.05)

    def update_date():
        ph_timezone = pytz.timezone("Asia/Manila")
        current_time = datetime.now(ph_timezone)
        formatted_date = current_time.strftime("%B %d, %Y")
        formatted_time = current_time.strftime("%I:%M %p")
        date_label.configure(text=formatted_date)
        time_label.configure(text=formatted_time)
        borrow.after(1000, update_date)
    
    date_label = ctk.CTkLabel(date_border, font=("Arial", 24, 'bold'), text_color="Black")
    date_label.place(relx=0.07, rely=0.2)

    time_label = ctk.CTkLabel(time_border, font=("Arial", 24, 'bold'), text_color="Black")
    time_label.place(relx=0.07, rely=0.2)
    update_date()

    page_bg = ctk.CTkFrame(borrow, width=(0.5 * ww), height=(0.14 * wh), fg_color="white", 
                      corner_radius=20)
    page_bg.place(relx=0.5, rely=0.15, anchor='n')

    admin_pic = ctk.CTkImage(Image.open("admin_blue_pic.png"), size=((0.23 * ww), (0.33 * wh))) 
    admin = ctk.CTkLabel(borrow, text='', image=admin_pic, width=(0.05 * ww), anchor="center")
    admin.place(relx=0.435, rely=0.4)

    ask_label = ctk.CTkLabel(borrow, text="Please ask a librarian to tap the security card.", font=("Arial", 30), text_color="Black")
    ask_label.place (relx=0.5, y=0.81, anchor='center')

    cancel_button = ctk.CTkButton(borrow, text='CANCEL', height=50, width=int(0.05 * ww), fg_color='blue', font=("Arial", 25, "bold"),
                                  text_color="White", corner_radius=20)
    cancel_button.place(relx=0.45, rely=0.90)
    
    #FOR PASSWORD INPUT
    #inst_label = ctk.CTkLabel (borrow, text='Check the spine of the book for Book ID (Example: 1027)', font = ("Arial", 20), text_color="Black")
    #inst_label.place (x=(0.5 * ww), y=(0.71 * wh), anchor='n')
    #entry_bar = ctk.CTkEntry(borrow, width=750, height=70, corner_radius=50, fg_color='white',
    #                          text_color="black", placeholder_text="Enter Book ID", font=("Arial", 20))
    #entry_bar.place(x=(0.5 * ww), y=(0.8 * wh), anchor='center')

    #entry_button = ctk.CTkButton(entry_bar, text='', image=search_pic, width=(0.05 * ww), fg_color='white')
    #entry_button.place(relx=0.97, rely=0.5, anchor='e')