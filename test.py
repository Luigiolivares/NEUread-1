import customtkinter as ctk
import tkinter as tk
from PIL import Image
from datetime import datetime
import pytz


root = tk.Tk()
root.title("yarr")
root.attributes('-fullscreen', True) #My laptop size configuring postion are (with is 1536, height is 864)

ww = root.winfo_screenwidth()
wh = root.winfo_screenheight() 

content = ctk.CTkFrame(root)
content.pack(fill="both", expand=True)

book = open("book_pic.png", "rb")
search = open("next_blue.png", "rb")
dot = open("dot_pic.png", "rb")
admin_profile = open("admin_pic.png", "rb")

# place here for all photo images
def borrow_books(content):
    bors = tk.Frame(content)
    bors.place(width=ww, height=wh)
    search_image = ctk.CTkImage(Image.open(search), size=((0.033 * ww), (0.06 * wh))) 
    book_pic = ctk.CTkImage(Image.open(book), size=((0.2 * ww), (0.35 * wh))) 
    dot_pic = ctk.CTkImage(Image.open(dot), size=((0.065 * ww), (0.06 * wh)))
    user_pic = ctk.CTkImage(Image.open(admin_profile), size=((0.13 * ww), (0.23 * wh))) 
    admin_pic = ctk.CTkImage(Image.open(admin_profile), size=((0.13 * ww), (0.23 * wh))) 

    time_border = ctk.CTkFrame(bors, width=(0.08 * ww), height=(0.067 * wh), fg_color="azure3", 
                corner_radius=13, border_width=15, border_color="azure3")
    time_border.place(x=(0.89 * ww), y=(0.05 * wh))

    date_border = ctk.CTkFrame(bors, width=(0.13 * ww), height=(0.069 * wh), fg_color="azure3", 
                      corner_radius=13, border_width=15, border_color="azure3")
    date_border.place(x=(0.03 * ww), y=(0.05 * wh))

    def update_date():
        ph_timezone = pytz.timezone("Asia/Manila")
        current_time = datetime.now(ph_timezone)
        formatted_date = current_time.strftime("%B %d, %Y")
        formatted_time = current_time.strftime("%I:%M %p")
        date_label.configure(text=formatted_date)
        time_label.configure(text=formatted_time)
        bors.after(1000, update_date)
    
    date_label = ctk.CTkLabel(date_border, font=("Arial", 24, 'bold'), text_color="Black")
    date_label.place(relx=0.07, rely=0.2)

    time_label = ctk.CTkLabel(time_border, font=("Arial", 24, 'bold'), text_color="Black")
    time_label.place(relx=0.07, rely=0.2)
    update_date()

    page_bg = ctk.CTkFrame(bors, width=(0.5 * ww), height=(0.14 * wh), fg_color="white", 
                      corner_radius=20)
    page_bg.place(x=(0.5 * ww), y=(0.15 * wh), anchor='n')

    page_label = ctk.CTkLabel(page_bg, text='Borrow Book', font=("Arial", 60, "bold"), text_color="blue")
    page_label.place(relx=0.246, rely=0.2)

    book_label = ctk.CTkLabel(bors, text='', image=book_pic, width=(0.05 * ww))
    book_label.place(relx=0.13, rely=0.35)

    dot1_label = ctk.CTkLabel(bors, text='', image=dot_pic, width=(0.05 * ww))
    dot1_label.place(relx=0.35, rely=0.49)

    user = ctk.CTkLabel(bors, text='', image=user_pic, width=(0.05 * ww))
    user.place(relx=0.45, rely=0.4)

    dot2_label = ctk.CTkLabel(bors, text='', image=dot_pic, width=(0.05 * ww))
    dot2_label.place(relx=0.615, rely=0.49)

    admin = ctk.CTkLabel(bors, text='', image=admin_pic, width=(0.05 * ww))
    admin.place(relx=0.72, rely=0.4)

    inst_label = ctk.CTkLabel (bors, text='Check the spine of the book for Book ID (Example: 1027)', font = ("Arial", 20), text_color="Black")
    inst_label.place (x=(0.5 * ww), y=(0.71 * wh), anchor='n')


    # Create the search bar entry inside the border
    entry_bar = ctk.CTkEntry(bors, width=750, height=70, corner_radius=50, fg_color='white',
                              text_color="black", placeholder_text="Enter Book ID", font=("Arial", 20))
    entry_bar.place(x=(0.5 * ww), y=(0.8 * wh), anchor='center')

    entry_button = ctk.CTkButton(entry_bar, text='', image=search_image, width=(0.05 * ww), fg_color='white')
    entry_button.place(relx=0.97, rely=0.5, anchor='e')

    cancel_button = ctk.CTkButton(bors, text='CANCEL', height=50, width=(0.05 * ww), fg_color='blue', font=("Arial", 25, "bold"), 
                                  text_color="White", corner_radius=20)
    cancel_button.place(x=(0.45 * ww), y=(0.90 * wh))

    


borrow_books(content)

root.mainloop()
