###########
import customtkinter as ctk
import tkinter as tk
from datetime import datetime
import pytz
from PIL import Image 
from io import BytesIO
from penaltyRemoved import *
from bnd import *
def Main_user_page(content, RFID):
    person = open("admin_pic.png", "rb")
    ww = content.winfo_screenwidth()
    wh = content.winfo_screenheight()
    profileInfo = getUserInfo(RFID)
    borrowedBooks = profileInfo[1]
    print(borrowedBooks)
    person_image = ctk.CTkImage(Image.open(person), size=((75), (75)))

    user_page = tk.Frame(content)
    user_page.place(width=ww, height=wh)

    time_border = ctk.CTkFrame(user_page, width=(0.08 * ww), height=(0.067 * wh), fg_color="azure3", 
                      corner_radius=13, border_width=15, border_color="azure3")
    time_border.place(x=(0.81 * ww), y=(0.05 * wh))

    date_border = ctk.CTkFrame(user_page, width=(0.13 * ww), height=(0.069 * wh), fg_color="azure3", 
                      corner_radius=13, border_width=15, border_color="azure3")
    date_border.place(x=(0.11 * ww), y=(0.05 * wh))

    def update_date():
        ph_timezone = pytz.timezone("Asia/Manila")
        current_time = datetime.now(ph_timezone)
        formatted_date = current_time.strftime("%B %d, %Y")
        formatted_time = current_time.strftime("%I:%M %p")
        date_label.configure(text=formatted_date)
        time_label.configure(text=formatted_time)
        user_page.after(1000, update_date)

    date_label = ctk.CTkLabel(date_border, font=("Arial", 24, 'bold'), text_color="Black")
    date_label.place(relx=0.07, rely=0.2)

    time_label = ctk.CTkLabel(time_border, font=("Arial", 24, 'bold'), text_color="Black")
    time_label.place(relx=0.07, rely=0.2)
    update_date()

    profile = ctk.CTkFrame(user_page, width=(1100), height=(150), fg_color="white",
                      corner_radius=15)
    profile.place(x=(0.15 * ww), y=(0.2 * wh))

    profile_image = ctk.CTkLabel(profile, text='', image=person_image)
    profile_image.place(relx=0.05, rely=0.2)

    Name = ctk.CTkLabel(profile, text=profileInfo[0][0][1], font=("Arial", 32, "bold"), text_color="black")
    Name.place(relx=0.15, rely=0.1)

    IdNum = ctk.CTkLabel(profile, text=profileInfo[0][0][3], font=("Arial", 25), text_color="black")
    IdNum.place(relx=0.15, rely=0.4)

    Role = ctk.CTkLabel(profile, text='Student', font=("Arial", 25), text_color="black")
    Role.place(relx=0.1503, rely=0.6)

    current_books_container = ctk.CTkFrame(user_page, width=(1110), height=(0.46 * wh), fg_color="white", border_color='royal blue', border_width=10,
                      corner_radius=15)
    current_books_container.place(x=(0.51 * ww), y=(0.65 * wh), anchor='center')

    current_frame = ctk.CTkFrame(current_books_container, width=(300), height=(50), fg_color="blue",
                      corner_radius=20)
    current_frame.place(relx=0.5, rely=0.03, anchor='n')

    current_books_label = ctk.CTkLabel(current_frame, text='Current Borrowed Books', font=("Arial", 20, "bold"), text_color="black")
    current_books_label.place(relx=0.5, rely=0.5, anchor='center')

    divisor = ctk.CTkFrame(current_books_container, width=5, height=275, fg_color="light gray", corner_radius=5)
    divisor.place(relx=0.5, rely=0.55, anchor='center')
    if len(profileInfo[2]) > 0:  # Check if at least one book exists
        book_image1 = ctk.CTkImage(Image.open(BytesIO(profileInfo[2][0][2])), size=(100, 150))
        book_cover_left = ctk.CTkLabel(current_books_container, text='', image=book_image1)
        book_cover_left.place(relx=0.1, rely=0.3)

        book_author_left = ctk.CTkLabel(current_books_container, text=f'By {profileInfo[2][0][1]}', font=("Arial", 18), text_color="black")
        book_author_left.place(relx=0.2, rely=0.45)

        book_title_left = ctk.CTkLabel(current_books_container, text=profileInfo[2][0][0], font=("Arial", 24, "bold"), text_color="black", wraplength=300)
        book_title_left.place(relx=0.2, rely=0.30)

        borrowed_date_left = ctk.CTkLabel(current_books_container, text=f'Borrowed: {profileInfo[1][0][1]}', font=("Arial", 18), text_color="black")
        borrowed_date_left.place(relx=0.2, rely=0.8)

    if len(profileInfo[2]) > 1:  # Check if a second book exists
        book_image2 = ctk.CTkImage(Image.open(BytesIO(profileInfo[2][1][2])), size=(100, 150))
        book_cover_right = ctk.CTkLabel(current_books_container, text='', image=book_image2)
        book_cover_right.place(relx=0.6, rely=0.3)

        book_title_right = ctk.CTkLabel(current_books_container, text=profileInfo[2][1][0], font=("Arial", 24, "bold"), text_color="black", wraplength=300)
        book_title_right.place(relx=0.7, rely=0.30)

        book_author_right = ctk.CTkLabel(current_books_container, text=f'By {profileInfo[2][1][1]}', font=("Arial", 18), text_color="black")
        book_author_right.place(relx=0.7, rely=0.45)

        borrowed_date_right = ctk.CTkLabel(current_books_container, text=f'Borrowed: {profileInfo[1][1][1]}', font=("Arial", 18), text_color="black")    
        borrowed_date_right.place(relx=0.7, rely=0.8)

    penalty_button = ctk.CTkButton(
    user_page, 
    text="PENALTY",
    font=("Arial", 24, "bold"), 
    text_color="white",
    fg_color="red",  # Background color
    hover_color="darkred",  # Hover effect
    corner_radius=20,
    border_width=15,
    border_color="red",
    width=int(0.2 * ww),
    height=int(0.05 * wh),
    command= lambda: penaltyPage(content)  # Function to execute on click
)

# Place the button at the same position
    penalty_button.place(x=(0.5 * ww), y=(0.91 * wh), anchor="center")
