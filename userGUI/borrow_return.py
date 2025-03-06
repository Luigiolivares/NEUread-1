import tkinter as tk
import random
import customtkinter as ctk
from bnd import *
from datetime import datetime, timedelta
import time
rfid_data = ""
adminRFID = None
userRFID = None
initialUser = None
bookID = None
last_scan_time = 0
def Main_borrow_return_page(content, screenWidth, screenHeight, userID, main):
    global initialUser
    initialUser = userID
    frame = create_frame(content)
    tk.Label(frame, text='Books Section', font=('Arial', 24)).place(x=600, y=100)
    tk.Button(frame, text="Borrow", font=('Arial', 14), command=lambda: borrow_page(content, main)).place(x=600, y=300, width=200)
    tk.Button(frame, text="Return", font=('Arial', 14), command=lambda: return_page(content)).place(x=600, y=400, width=200)
    
    frame.tkraise()

def borrow_page(content, root):
    # Destroy any existing frames inside content to prevent overlap
    for widget in content.winfo_children():
        widget.destroy()

    # Create and place borrowFrame
    borrowFrame = tk.Frame(content, width=1720, height=1080)
    borrowFrame.place(x=0, y=0)  # This ensures it fills the entire content area

    # Title Label
    label = tk.Label(borrowFrame, text='Borrow Books', font=('Arial', 24))
    label.place(x=600, y=100)

    # Subheading Label
    subheading = tk.Label(borrowFrame, text='Please Enter The Book ID', font=('Arial', 16))
    subheading.place(x=500, y=150)

    # Search Bar (CTkEntry)
    book_id_entry = ctk.CTkEntry(borrowFrame, width=300, height=40, font=('Arial', 14))
    book_id_entry.place(x=500, y=200)

    # Function to Save Input
    def save_input():
        global bookID
        book_id = book_id_entry.get()
        search_result = searchBookID(book_id)

        if search_result:
            print(f"Book ID Entered: {search_result}", ", kukuhain na admin")
            book_id_entry.place_forget()
            bookID = search_result
            
            getAdmin(content, root)
        else: 
            print("Book not found")

    # Search Button
    search_button = ctk.CTkButton(borrowFrame, text="Search", command=save_input)
    search_button.place(x=820, y=200)

def getAdmin(content, root):
    root.bind("<Key>", lambda event: keyPressed(event, content))

def getUser(iconActive):
    print("changing icons, enter user RFID")

def completeTransaction(RFID):
    global bookID
    Date_Borrowed = datetime.now()
    Deadline = (Date_Borrowed + timedelta(days=3)).date()
    addBorrowBook(RFID, bookID, Date_Borrowed, Deadline, None)
    print("Add mo na sa database")

def is_rfid_scan():
    global last_scan_time
    current_time = time.time()
    if current_time - last_scan_time < 0.1:
        last_scan_time = current_time
        return True
    last_scan_time = current_time
    return False


def keyPressed(event, content):
    global rfid_data, adminRFID, userRFID, initialUser
    
    if not is_rfid_scan():
        return  # Ignore manual keyboard input
    print("pressed key")
    if event.keysym == "Return":
        if rfid_data and not adminRFID:
            admin = adminCheck(rfid_data)
            if admin:
                print(f"ADMIN Entered: {admin}")
                adminRFID = admin
                getUser(content)
            else:
                print("Admin not found")
            rfid_data = ""  # Reset buffer
        elif rfid_data and adminRFID:
            user = getUserInfo(rfid_data)
            if user[0][0][0] == initialUser:
                completeTransaction(rfid_data)
                print(f"User Entered: {user[0][0][1]}")
            else:
                print("Incorrect user")
    else:
        rfid_data += event.char

def return_page(content):
    frame = create_frame(content)
    
    label = tk.Label(frame, text='Return Books', font=('Arial', 24))
    label.place(x=600, y=100)
    
    subheading = tk.Label(frame, text='Please Tap Librarian ID Card on the reader', font=('Arial', 16))
    subheading.place(x=500, y=150)
    
    frame.after(2000, lambda: subheading.config(text='Please type in the Book ID'))
    frame.after(4000, lambda: subheading.config(text='Please Tap Student ID Card on the reader'))
    frame.after(6000, lambda: thank_you_page(content))
    
    frame.tkraise()

def thank_you_page(content):
    for widget in content.winfo_children():
        widget.destroy()
    
    content.configure(bg="mistyrose")
    
    canvas = tk.Canvas(content, bg="mistyrose")
    canvas.pack(fill="both", expand=True)
    
    stars = create_twinkle_stars(canvas, content)
    
    tk.Label(content, text="Transaction Successful", font=("Times New Roman", 50, "bold"), fg="green", bg="mistyrose").place(relx=0.5, rely=0.4, anchor="center")
    tk.Label(content, text="THANK YOU FOR USING NEURead!", font=("Times New Roman", 60), fg="salmon", bg="mistyrose").place(relx=0.5, rely=0.5, anchor="center")
    tk.Button(content, text="EXIT", font=("Arial", 25), bg="thistle", fg="black", command=lambda: Main_borrow_return_page(content)).place(relx=0.5, rely=0.8, anchor="center")

def create_twinkle_stars(canvas, content):
    stars = []
    for _ in range(50):
        x, y = random.randint(0, content.winfo_screenwidth()), random.randint(0, content.winfo_screenheight())
        size = random.randint(2, 5)
        star = canvas.create_oval(x, y, x + size, y + size, fill="white")
        stars.append((star, x, y, size))
    
    def twinkle():
        for star, x, y, size in stars:
            new_size = max(2, min(5, size + random.choice([-1, 0, 1])))
            canvas.coords(star, x, y, x + new_size, y + new_size)
            canvas.itemconfig(star, fill=random.choice(["white", "lightblue", "yellow"]))
        content.after(300, twinkle)
    
    twinkle()
    return stars

def create_frame(content):
    frame = tk.Frame(content)
    frame.place(x=0, y=0, width=1720, height=1080)
    return frame