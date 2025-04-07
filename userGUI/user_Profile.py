###########
import customtkinter as ctk
import tkinter as tk
from datetime import datetime
import pytz
from PIL import Image 
from io import BytesIO
from bnd import *
import bcrypt
from keyboard import *
def Main_user_page(content, RFID, root):
    for widget in content.winfo_children():
        if isinstance(widget, tk.Frame):
            widget.destroy()
    person = open("userGray.png", "rb")
    ww = content.winfo_screenwidth()
    wh = content.winfo_screenheight()
    profileInfo = getUserInfo(RFID)
    borrowedBooks = profileInfo[1]
    print(borrowedBooks)
    person_image = ctk.CTkImage(Image.open(person), size=((75), (75)))

    user_page = tk.Frame(content)
    user_page.place(relx=0, rely=0, relwidth=1, relheight=1)

    time_border = ctk.CTkFrame(user_page, width=(0.08 * ww), height=(0.067 * wh), fg_color="azure3", 
                      corner_radius=13, border_width=15, border_color="azure3")
    time_border.place(relx=0.89, rely=0.05)

    date_border = ctk.CTkFrame(user_page, width=(0.13 * ww), height=(0.069 * wh), fg_color="azure3", 
                      corner_radius=13, border_width=15, border_color="azure3")
    date_border.place(relx=0.03, rely=0.05)

    def update_date():
        ph_timezone = pytz.timezone("Asia/Manila")
        current_time = datetime.now(ph_timezone)
        formatted_date = current_time.strftime("%B %d, %Y")
        formatted_time = current_time.strftime("%I:%M %p")
        date_label.configure(text=formatted_date)
        time_label.configure(text=formatted_time)
        user_page.after(1000, update_date)

    date_label = ctk.CTkLabel(date_border, font=("Arial", 24, 'bold'), text_color="Black")
    date_label.place(relx=0.5, rely=0.5, anchor = "center")

    time_label = ctk.CTkLabel(time_border, font=("Arial", 24, 'bold'), text_color="Black")
    time_label.place(relx=0.5, rely=0.5, anchor = "center")
    update_date()

    profile = ctk.CTkFrame(user_page, width=(1100), height=(150), fg_color="white",
                      corner_radius=15)
    profile.place(relx=0.5, rely=0.275, anchor='center')

    profile_image = ctk.CTkLabel(profile, text='', image=person_image)
    profile_image.place(relx=0.05, rely=0.2)

    Name = ctk.CTkLabel(profile, text=profileInfo[0][0][1], font=("Arial", 32, "bold"), text_color="black")
    Name.place(relx=0.15, rely=0.1)

    IdNum = ctk.CTkLabel(profile, text=profileInfo[0][0][3], font=("Arial", 25), text_color="black")
    IdNum.place(relx=0.15, rely=0.4)

    Role = ctk.CTkLabel(profile, text='Student', font=("Arial", 25), text_color="black")
    Role.place(relx=0.1503, rely=0.6)

    current_books_container = ctk.CTkFrame(user_page, width=(1110), height=(0.46 * wh), fg_color="white", border_color='#5088FC', border_width=3,
                      corner_radius=15)
    current_books_container.place(relx=0.5, rely=0.65, anchor='center')

    current_frame = ctk.CTkFrame(current_books_container, width=(300), height=(50), fg_color="#5088FC",
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
    command= lambda: penalty1(content, root, RFID)# Function to execute on click
)
    print(profileInfo[0][0][5])
    if profileInfo[0][0][5] == 1:
        penalty_button.place(relx=0.5, rely=0.94, anchor="center")
################################################################################
################################################################################
################## PENALTY PAGE, KASI BAWAL DAW CIRCULAR IMPORT ################
################################################################################
################################################################################
lib = open("admin_pic.png", "rb") 
button = open("next.png", "rb")
rfid_data = ""
def penalty1(content, root, RFID):
    admin = ctk.CTkImage(Image.open(lib), size=((300), (300))) 
    ww = content.winfo_screenwidth() 
    wh = content.winfo_screenheight() 
    penalty1_page = tk.Frame(content) 
    penalty1_page.place(relx=0, rely=0, relwidth=1, relheight=1)

    time_border = ctk.CTkFrame(penalty1_page, width=(0.08 * ww), height=(0.067 * wh), fg_color="azure3", 
                      corner_radius=13, border_width=15, border_color="azure3")
    time_border.place(relx=0.89, rely=0.05)

    date_border = ctk.CTkFrame(penalty1_page, width=(0.13 * ww), height=(0.069 * wh), fg_color="azure3", 
                      corner_radius=13, border_width=15, border_color="azure3")
    date_border.place(relx=0.03, rely=0.05)

    def update_date():
        ph_timezone = pytz.timezone("Asia/Manila")
        current_time = datetime.now(ph_timezone)
        formatted_date = current_time.strftime("%B %d, %Y")
        formatted_time = current_time.strftime("%I:%M %p")
        date_label.configure(text=formatted_date)
        time_label.configure(text=formatted_time)
        penalty1_page.after(1000, update_date)

    date_label = ctk.CTkLabel(date_border, font=("Arial", 24, 'bold'), text_color="Black")
    date_label.place(relx=0.07, rely=0.2)

    time_label = ctk.CTkLabel(time_border, font=("Arial", 24, 'bold'), text_color="Black")
    time_label.place(relx=0.07, rely=0.2)
    update_date()
    root.bind("<Key>", lambda event: keyPressed(event, content, root, RFID))

    laman = ctk.CTkFrame(penalty1_page, width=(1100), height=(0.75 * wh), fg_color="white", corner_radius=15) 
    laman.place(relx=0.5, rely=0.5, anchor = "center") 

    admin_image = ctk.CTkLabel(laman, text='', image=admin) 
    admin_image.place(relx=0.5, rely=0.35, anchor="center") 

    request = ctk.CTkLabel(laman, text='Please ask a librarian to tap the security card.', font=("Arial", 32), text_color="black") 
    request.place(relx=0.5, rely=0.72, anchor="center")

def keyPressed(event, content, root, RFID):
    
    #if not is_rfid_scan():
        #return  # Ignore manual keyboard input
    print("pressed key")
    global rfid_data
    if event.keysym == "Return":
        if rfid_data:
            string_data = str(rfid_data)
            print(adminCheck(string_data), string_data)
            if adminCheck(string_data):
                print(f"ADMIN Entered")
                root.unbind("<Key>")
                penalty2(content, RFID, root)
            else:
                print("Admin not found: ", adminCheck(string_data))
        rfid_data += event.char
    else:
        rfid_data += event.char
def penalty2(content, RFID, root):
    ww = content.winfo_screenwidth() 
    wh = content.winfo_screenheight() 
    passwd = "$2b$12$qc/cxFV9Dze05iJ4kN4FvOHi00p7oFI.cYCa3xUCKVfXTJzKGrJ3e"
    admin = ctk.CTkImage(Image.open(lib), size=((0.2 * ww), (0.35 * wh))) 
    btn = ctk.CTkImage(Image.open(button), size=((0.033 * ww), (0.06 * wh))) 

    penalty1_page = tk.Frame(content) 
    penalty1_page.place(relx=0, rely=0, relwidth=1, relheight=1)

    time_border = ctk.CTkFrame(penalty1_page, width=(0.08 * ww), height=(0.067 * wh), border_color="azure3",
                               fg_color="azure3", corner_radius=13, border_width=15) 
    time_border.place(relx=0.81, rely=0.05) 
    
    date_border = ctk.CTkFrame(penalty1_page, width=(0.13 * ww), height=(0.069 * wh), fg_color="azure3", corner_radius=13, border_width=15, border_color="azure3") 
    date_border.place(relx=0.11, rely=0.05) 
    def update_date(): 
        ph_timezone = pytz.timezone("Asia/Manila") 
        current_time = datetime.now(ph_timezone) 
        formatted_date = current_time.strftime("%B %d, %Y") 
        formatted_time = current_time.strftime("%I:%M %p") 
        date_label.configure(text=formatted_date) 
        time_label.configure(text=formatted_time) 
        penalty1_page.after(1000, update_date) 
        
    date_label = ctk.CTkLabel(date_border, font=("Arial", 24, 'bold'), text_color="Black") 
    date_label.place(relx=0.07, rely=0.2, anchor = "center") 
    
    time_label = ctk.CTkLabel(time_border, font=("Arial", 24, 'bold'), text_color="Black") 
    time_label.place(relx=0.07, rely=0.2, anchor = "center") 
    
    update_date() 

    laman = ctk.CTkFrame(penalty1_page, width=(1100), height=(0.75 * wh), fg_color="white", corner_radius=15) 
    laman.place(relx=0.5, rely=0.5, anchor = "center") 

    admin_image = ctk.CTkLabel(laman, text='', image=admin) 
    admin_image.place(relx=0.5, rely=0.35, anchor="center") 

    password = ctk.CTkEntry(laman, width=750, height=70, corner_radius=50, fg_color='white',
                              text_color="black", placeholder_text="Enter Security Password", font=("Arial", 20), show="•") 
    password.bind("<Button-1>", lambda event: open_keyboard(root, password, event))
    password.place(relx=0.5, rely=0.72, anchor="center")
    def submit_password(entry_button):
        user_input = password.get()
        access = bcrypt.checkpw(user_input.encode(), passwd.encode())
        if access:
            penalty(RFID, 0)
            close()
            entry_button.configure(state="disabled")
            pop_up_page = tk.Frame(penalty1_page, width=500, height=300, bg="89AEFF")
            pop_up_page.pack(fill="both", expand=True)
            left_border = tk.Frame(pop_up_page, width=5, height=300, bg="white")
            left_border.place(x=0, rely=0, relheight=1)
            # Bind the frame touch event, passing the frame as an argument
            pop_up_page.bind("<Button-1>", lambda event: on_frame_touch(event, pop_up_page, content, root))

            pop_up_label = tk.Label(pop_up_page, text='Penalty removed!', fg="white", font=("Arial", 55, "bold"), 
                            bg="89AEFF", wraplength=1500)
            pop_up_label.place(relx=0.5, rely=0.45, anchor="center")

            pop_up_label2 = tk.Label(pop_up_page, text="Please touch the screen to continue", fg="white", 
                             font=("Arial", 20, "bold"), bg="89AEFF")
            pop_up_label2.place(relx=0.5, rely=0.53, anchor="center")
    def on_frame_touch(event, frame, content, root):
        if event.widget == frame:
            frame.unbind("<Button-1>")
            Main_user_page(content, RFID, root)
    entry_button = ctk.CTkButton(password, text='', image=btn, width=(0.05 * ww), fg_color='white', command = lambda: submit_password(entry_button))
    entry_button.place(relx=0.97, rely=0.5, anchor='e')
    cancel_btn = ctk.CTkButton(laman, text='Cancel', font=("Arial", 32, "bold"), text_color="White", fg_color="darkblue", corner_radius=20, width=50, height=50, command= lambda: Main_user_page(content, RFID, root)) 
    cancel_btn.place(relx=0.5, rely=0.85, anchor="center")