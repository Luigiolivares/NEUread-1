import tkinter as tk
import customtkinter as ctk
from bnd import *
from datetime import datetime, timedelta
import time
from PIL import Image, ImageTk
import pytz

ww = None
wh = None
rfid_data = ""
adminRFID = False
userRFID = None
initialUser = None
bookID = None
Title = None
last_scan_time = 0
purpose = None
topLabel = None
bottomLabel = None

bookIcon = None
adminIcon = None
userIcon = None

bookPart = None
adminPart = None
userPart = None
def Main_borrow_return_page(content, userID, main):
    global initialUser, purpose, ww, wh, rfid_data, adminRFID, userRFID, bookID, Title, last_scan_time
    global topLabel, bottomLabel, bookIcon, adminIcon, userIcon, bookPart, adminPart, userPart
    
    ww = content.winfo_screenwidth()
    wh = content.winfo_screenheight()
    initialUser = userID
    purpose = None
    rfid_data = ""
    adminRFID = False
    userRFID = None
    bookID = None
    Title = None
    last_scan_time = 0
    topLabel = None
    bottomLabel = None
    
    bookIcon = None
    adminIcon = None
    userIcon = None
    
    bookPart = None
    adminPart = None
    userPart = None
    for widget in content.winfo_children():
        if isinstance(widget, tk.Frame):
            widget.destroy()
    frame = tk.Frame(content, bg='#f2f3f7')
    frame.place(relx=0, rely=0, relwidth=1, relheight=1)
    
    # Date
    today = datetime.today().strftime("%d %B, %Y")
    date_label = tk.Label(frame, text=today, font=('Arial', 18, 'bold'), bg='#f2f3f7', fg='black')
    date_label.place(x=35, y=50)
    
    # Time
    current_time = datetime.now().strftime("%I:%M %p")
    time_label = tk.Label(frame, text=current_time, font=('Arial', 18, 'bold'), bg='#9dabbe', fg='black', padx=10, pady=4)
    time_label.place(x=frame.winfo_screenwidth()-220, y=50)
    
    # Frame for buttons
    button_frame = tk.Frame(frame)
    button_frame.place(x=245, y=110)
    
    # Load Button Icons
    borrow_icon = ImageTk.PhotoImage(Image.open("borrowbtn.png").resize((280, 260)))
    return_icon = ImageTk.PhotoImage(Image.open("returnbtn.png").resize((280, 260)))
    
    # Borrow button
    borrow_btn = tk.Button(
        button_frame, text="\nBorrow", font=('Arial', 30, "bold"), bg='white', fg='black', bd=0,
        width=400, height=670, image=borrow_icon, compound='top', padx=10, pady=10,
        command=lambda: borrow_page(content, main, "Borrow")
    )
    borrow_btn.image = borrow_icon  # Keep a reference to prevent garbage collection
    borrow_btn.grid(row=0, column=0, padx=30)
    
    # Return button
    return_btn = tk.Button(
        button_frame, text="\nReturn", font=('Arial', 30, "bold"), bg='white', fg='black', bd=0,
        width=400, height=670, image=return_icon, compound='top', padx=10, pady=10,
        command=lambda: borrow_page(content, main, "Return")
    )
    return_btn.image = return_icon  # Keep a reference to prevent garbage collection
    return_btn.grid(row=0, column=1, padx=30)

search = open("next_blue.png", "rb")
dot = open("dot_pic.png", "rb")
admin_profile = open("admin_pic.png", "rb")

book = open("book_pic.png", "rb")
ON_admin_profile = open("admin_blue_pic.png", "rb")

DONE_book = open("book_done_pic.png", "rb")
DONE_admin = open("admin_done_prev_ui.png", "rb")

# place here for all photo images
def borrow_page(content, root, pressedPurpose):
    global purpose, topLabel,bottomLabel, bookIcon, adminIcon, userIcon, ww, wh, bookPart, adminPart, userPart
    purpose = pressedPurpose
    bors = tk.Frame(content)
    bors.place(relx=0, rely=0, relwidth=1, relheight=1)
    search_image = ctk.CTkImage(Image.open(search), size=((0.033 * ww), (0.06 * wh))) 
    book_pic = ctk.CTkImage(Image.open(book), size=((0.2 * ww), (0.35 * wh))) 
    dot_pic = ctk.CTkImage(Image.open(dot), size=((0.065 * ww), (0.06 * wh)))
    user_pic = ctk.CTkImage(Image.open(admin_profile), size=((0.13 * ww), (0.23 * wh))) 
    admin_pic = ctk.CTkImage(Image.open(admin_profile), size=((0.13 * ww), (0.23 * wh))) 

    bookIcon = book_pic
    adminIcon = admin_pic
    userIcon = user_pic

    time_border = ctk.CTkFrame(bors, width=(0.08 * ww), height=(0.067 * wh), fg_color="azure3", 
                corner_radius=13, border_width=15, border_color="azure3")
    time_border.place(relx=0.89, rely=0.05)

    date_border = ctk.CTkFrame(bors, width=(0.13 * ww), height=(0.069 * wh), fg_color="azure3", 
                      corner_radius=13, border_width=15, border_color="azure3")
    date_border.place(relx=0.03, rely=0.05)

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
    page_bg.place(relx=0.5, rely=0.15, anchor='center')

    page_label = ctk.CTkLabel(page_bg, text=f'{purpose} Book', font=("Arial", 40, "bold"), text_color="blue",  wraplength= 300)
    page_label.place(relx=0.5, rely=0.2, anchor= "center")
    topLabel = page_label

    book_label = ctk.CTkLabel(bors, text='', image=book_pic, width=(0.05 * ww))
    book_label.place(relx=0.05, rely=0.4)

    dot1_label = ctk.CTkLabel(bors, text='', image=dot_pic, width=(0.05 * ww))
    dot1_label.place(relx=0.3, rely=0.49)

    user = ctk.CTkLabel(bors, text='', image=user_pic, width=(0.05 * ww))
    user.place(relx=0.435, rely=0.4)

    dot2_label = ctk.CTkLabel(bors, text='', image=dot_pic, width=(0.05 * ww))
    dot2_label.place(relx=0.635, rely=0.49)

    admin = ctk.CTkLabel(bors, text='', image=admin_pic, width=(0.05 * ww))
    admin.place(relx=0.76, rely=0.4)

    inst_label = ctk.CTkLabel (bors, text='Check the spine of the book for Book ID (Example: 1027)', font = ("Arial", 20), text_color="Black")
    inst_label.place (relx=0.5, rely=0.71, anchor='n')

    # Create the search bar entry inside the border
    book_id_entry = ctk.CTkEntry(bors, width=750, height=70, corner_radius=50, fg_color='white',
                              text_color="black", placeholder_text="Enter Book ID", font=("Arial", 20))
    book_id_entry.place(relx=0.5, rely=0.8, anchor='center')

    entry_button = ctk.CTkButton(book_id_entry, text='', image=search_image, width=(0.05 * ww), fg_color='white', command= lambda: save_input(book_id_entry, inst_label, content, root))
    entry_button.place(relx=0.97, rely=0.5, anchor='e')

    cancel_button = ctk.CTkButton(bors, text='CANCEL', height=50, width=(0.05 * ww), fg_color='blue', font=("Arial", 25, "bold"), 
                                  text_color="White", corner_radius=20)
    cancel_button.place(relx=0.45, rely=0.90)

    ask_label = ctk.CTkLabel(bors, text="Please ask a librarian to tap the security card.", font=("Arial", 30), text_color="Black")
    bottomLabel = ask_label

    bookPart = book_label
    adminPart = user
    userPart = admin

def save_input(book_id_entry, inst_label, content, root):
    global bookID, Title, ww, wh
    book_id = book_id_entry.get()
    search_result = searchBookID(book_id)
    if not search_result:
        notif = ctk.CTkLabel(content, text="Book ID doesnt exist", font=("Arial", 20), text_color="Black")
        notif.place(relx= 0.5, rely=0.5)  # Show the label
        root.after(3000, lambda: notif.place_forget())
        return
    if purpose == "Borrow" and search_result[0][3] != 1:
        notif = ctk.CTkLabel(content, text="Book is currently unavailable", font=("Arial", 20), text_color="Black")
        notif.place(relx= 0.5, rely=0.5)  # Show the label
        root.after(3000, lambda: notif.place_forget())
        return
    if (search_result[0][3] != 0 and purpose == "Return"):
        notif = ctk.CTkLabel(content, text="Book is already available", font=("Arial", 20), text_color="Black")
        notif.place(relx= 0.5, rely=0.5)  # Show the label
        root.after(3000, lambda: notif.place_forget())
        return
    
    print(f"Book ID Entered: {search_result[0][0]}", ", kukuhain na admin")
    book_id_entry.place_forget()
    inst_label.place_forget()
    bookID = book_id
    Title = search_result[0][0]
    getAdmin(content, root, search_result[0][0])

def getAdmin(content, root, Title):
    global topLabel, bookIcon, adminIcon, ww, wh, bookPart, adminPart, bottomLabel
    new_bookImage = ctk.CTkImage(
        light_image=Image.open(DONE_book),
        size=((0.13 * ww), (0.23 * wh))
    )
    new_adminImage = ctk.CTkImage(
        light_image=Image.open(ON_admin_profile),
        size=((0.2 * ww), (0.35 * wh))
    )

    bookPart.configure(image = new_bookImage)
    adminPart.configure(image = new_adminImage)
    topLabel.configure(text=f"You are borrowing '{Title}'")
    bottomLabel.place (relx=0.5, rely=0.81, anchor='n')

    root.bind("<Key>", lambda event: keyPressed(event, content, root))

def getUser():
    global topLabel, userIcon, adminIcon, ww, wh, adminPart, userPart, bottomLabel, DONE_admin

    new_adminImage = ctk.CTkImage(
        light_image=Image.open(DONE_admin),
        size=((0.13 * ww), (0.23 * wh))
    )
    new_userImage = ctk.CTkImage(
        light_image=Image.open(ON_admin_profile),
        size=((0.2 * ww), (0.35 * wh))
    )
    adminPart.configure(image = new_adminImage)
    userPart.configure(image = new_userImage)
    bottomLabel.configure(text="Please tap your library card to confirm.")


def completeTransaction(RFID, content, root):
    global bookID, purpose, Title, ww, wh, userRFID

    pop_up_page = tk.Frame(content, width=500, height=300, bg="dark blue")
    pop_up_page.pack(fill="both", expand=True)

    # Bind the frame touch event, passing the frame as an argument
    pop_up_page.bind("<Button-1>", lambda event: on_frame_touch(event, pop_up_page, content, ww, wh, userRFID, root))

    pop_up_label = tk.Label(pop_up_page, text=f'"{Title}"', fg="white", font=("Arial", 55, "bold"), 
                            bg="dark blue", wraplength=1500)
    pop_up_label.place(relx=0.5, rely=0.45, anchor="center")

    pop_up_label2 = tk.Label(pop_up_page, text="Please touch the screen to continue", fg="white", 
                             font=("Arial", 20, "bold"), bg="dark blue")
    pop_up_label2.place(relx=0.5, rely=0.90, anchor="center")

    if purpose == "Borrow":
        Date_Borrowed = datetime.now()
        Deadline = (Date_Borrowed + timedelta(days=3)).date()
        addBorrowBook(RFID, bookID, Date_Borrowed, Deadline, None)

        pop_up_label3 = tk.Label(pop_up_page, text=f'Please return the book on or before {Deadline} to avoid being penalized.', 
                                 fg="white", font=("Arial", 30), bg="dark blue", wraplength=2000)
        pop_up_label3.place(relx=0.5, rely=0.60, anchor="center")

        pop_up_label4 = tk.Label(pop_up_page, text='You borrowed', fg="white", font=("Arial", 55, "bold"), 
                                 bg="dark blue")
        pop_up_label4.place(relx=0.5, rely=0.30, anchor="center")

        print("Added to the database")
    
    elif purpose == "Return":
        Date_Returned = datetime.now()
        returnBook(RFID, bookID, Date_Returned)

        pop_up_label5 = tk.Label(pop_up_page, text='You returned', fg="white", font=("Arial", 55, "bold"), 
                                 bg="dark blue")
        pop_up_label5.place(relx=0.5, rely=0.30, anchor="center")

def on_frame_touch(event, frame, content, screenWidth, screenHeight, userID, main):
    if event.widget == frame:
        Main_borrow_return_page(content, screenWidth, screenHeight, userID, main)
def is_rfid_scan():
    global last_scan_time
    current_time = time.time()
    if current_time - last_scan_time < 1:
        last_scan_time = current_time
        return True
    last_scan_time = current_time
    return False


def keyPressed(event, content, root):
    global rfid_data, adminRFID, userRFID, initialUser
    
    #if not is_rfid_scan():
        #return  # Ignore manual keyboard input
    print("pressed key")
    if event.keysym == "Return":
        if rfid_data and not adminRFID:
            string_data = str(rfid_data)
            print(adminCheck(string_data), string_data)
            if adminCheck(string_data):
                print(f"ADMIN Entered")
                adminRFID = True
                getUser()
            else:
                print("Admin not found")
            rfid_data = ""  # Reset buffer
        elif rfid_data and adminRFID:
            user = getUserInfo(rfid_data)
            if user[0][0][0] == initialUser:
                completeTransaction(rfid_data, content, root)
                root.unbind("<Key>")
                print(f"User Entered: {user[0][0][1]}")
            else:
                print(rfid_data)
                rfid_data = ""
                print("Incorrect user")
    else:
        rfid_data += event.char