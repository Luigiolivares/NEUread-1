import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk  # Import Pillow for image resizing
import bcrypt
from tkinter import Canvas
from bnd import *
from datetime import datetime
def admin(content, return_to_idle):
    passwd = "$2b$12$NhmTJ0kKyQdVdRJoIGbHBOA5kb1Bb7EB5sXY2MIprdTC5zC3Aqa2q"
    ww = content.winfo_screenwidth()
    wh = content.winfo_screenheight()
    for widget in content.winfo_children():
        if isinstance(widget, tk.Frame):
            widget.destroy()
    # Load and resize background image dynamically
    original_bg = Image.open("Admin_Interface_Design.png")# Load image
    resized_bg = original_bg.resize((ww, wh))  # Resize to screen size (ANTIALIAS is no longer needed)
    bg_image = ImageTk.PhotoImage(resized_bg)  # Convert for Tkinter

    # Set background image properly
    bg = tk.Label(content,image=bg_image)
    bg.place(relx=0, rely=0, relwidth=1, relheight=1)
    content.bg_image = bg_image

    password_frame = ctk.CTkFrame(content, width=1350, height=700, fg_color="white", border_color="grey")
    password_frame.place(relx=0.5, rely=0.5, anchor= "center")

    enter_password = ctk.CTkLabel(password_frame, text="Enter The Password\nTo Proceed", 
                                  font=("Arial", 75, 'bold'), text_color="Black")
    enter_password.place(relx=0.5, rely=0.3, anchor="center")

    password = ctk.CTkEntry(password_frame, width=650, height=65, font=("Arial", 32, 'bold'), 
                            fg_color="dark sea green", text_color="Black", corner_radius=50, border_width=0, show="•")
    password.place(relx=0.26, rely=0.5)
    def submit_password():
        user_input = password.get()
        access = bcrypt.checkpw(user_input.encode(), passwd.encode())
        if access:
            adminMain(content, return_to_idle)
    enter_option = ctk.CTkButton(password_frame, text="Enter", width=200, height=60, corner_radius=50, 
                                 bg_color="white", fg_color="green", font=("Arial", 32, 'bold'), text_color="White", command=submit_password)
    enter_option.place(relx=0.35, rely=0.67)

    cancel_option = ctk.CTkButton(password_frame, text="Cancel", width=200, height=60, corner_radius=50, 
                                  bg_color="white", border_width=5, border_color='green', fg_color="white", 
                                  font=("Arial", 24, 'bold'), text_color="Green", command= return_to_idle)
    cancel_option.place(relx=0.51, rely=0.67)

def create_rounded_rectangle(canvas, x1, y1, x2, y2, radius=25, color="white"):
    points = [
        x1 + radius, y1,
        x2 - radius, y1,
        x2, y1,
        x2, y1 + radius,
        x2, y2 - radius,
        x2, y2,
        x2 - radius, y2,
        x1 + radius, y2,
        x1, y2,
        x1, y2 - radius,
        x1, y1 + radius,
        x1, y1
    ]
    return canvas.create_polygon(points, smooth=True, fill=color, outline=color)

def adminMain(root, return_to_idle):
    innitNums = getUserAndBookNum()
    ww = root.winfo_screenwidth()
    wh = root.winfo_screenheight()
    datefrom = None
    dateTo = None
    canvas = Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    canvas.place(x=0, y=0)

#(Left, Top, Right, Bottom)
    create_rounded_rectangle(canvas, 80, 220, 80 + 725, 200 + 290, radius=50, color="yellow green")  # Borrowed Books Box
    create_rounded_rectangle(canvas, 550, 240, 550 + 225, 230 + 235, radius=50, color="green")  # Returned Books Box
    create_rounded_rectangle(canvas, 833, 220, 720 + 400, 200 + 290, radius=50, color="green")  # User Registered Box
    create_rounded_rectangle(canvas, 80, 515, 80 + 250, 400 + 350, radius=50, color="green")  # Books in System Box
    create_rounded_rectangle(canvas, 360, 515, 350 + 453, 525 + 220, radius=50, color="yellow green") # Users With Penalty Box
    create_rounded_rectangle(canvas, 1150, 220, 720 + 765, 200 + 443, radius=50, color="yellow green") # Data Shown Box

    logo = ctk.CTkImage(
    Image.open("logoo.png"),
    size=(int(0.26 * ww), int(0.21 * wh))
)
    book = ctk.CTkImage(
    Image.open("bookk.png"),
    size=(int(0.21 * ww), int(0.29 * wh))
)
    bookopen = ctk.CTkImage(
    Image.open("bookopen.png"),
    size=(int(0.16 * ww), int(0.2 * wh))
)

    person = ctk.CTkImage(
    Image.open("person.png"),
    size=(int(0.16 * ww), int(0.2 * wh))
)

    title_label = tk.Label(root, text="Hello, Admin!", font=("Arial", 47, "bold"), fg="green")
    title_label.place(x=85, y=75)

    logo_label = ctk.CTkLabel(root, image=logo, text="")
    logo_label.place(x=1040, y=13)

# For borrowed books box
    bookopen_frame = ctk.CTkFrame(root, width=int(0.02 * ww), height=int(0.01 * wh), fg_color="yellow green")
    bookopen_frame.place(x=120, y=275)
    bookopen_label = ctk.CTkLabel(bookopen_frame, image=bookopen, text="")
    bookopen_label.pack()
    bookopen = tk.Label(root, text="BORROWED BOOKS", font=("Arial", 17, "bold"), wraplength=200, fg="white", bg="yellow green")
    bookopen.place(x=375, y=270)

    bookopen_no = tk.Label(root, text="", font=("Arial", 38, "bold"), fg="white", bg="yellow green")
    bookopen_no.place(x=411, y=350)

# For returned books box
    returned_label= ctk.CTkFrame(root, width=int(0.02 * ww), height=int(0.01 * wh), fg_color="green")
    returned_label = tk.Label(root, text="RETURNED BOOKS", wraplength="200", font=("Arial", 17, "bold"), fg="white", bg="green")
    returned_label.place (x=598, y=270)

    returned_no = tk.Label(root, text="", font=("Arial", 38, "bold"), fg="white", bg="green")
    returned_no.place(x=644, y=350)

# For user registered box
    registered_label = ctk.CTkFrame(root, width=int(0.02 * ww), height=int(0.01 * wh), fg_color="green")
    registered_label = tk.Label(root, text="USER REGISTERED", wraplength="200", font=("Arial", 17, "bold"), fg="white", bg="green")
    registered_label.place (x=900, y=265)

    registered_no = tk.Label(root, text=innitNums[0], font=("Arial", 38, "bold"), fg="white", bg="green")
    registered_no.place(x=950, y=350)

# For books in the system box
    bsystem_label = ctk.CTkFrame(root, width=int(0.02 * ww), height=int(0.01 * wh), fg_color="green")
    bsystem_label = tk.Label(root, text="BOOKS IN THE SYSTEM", wraplength="200", font=("Arial", 17, "bold"), fg="white", bg="green")
    bsystem_label.place (x=120, y=550)
    #BORROW SECTION
    bsystem_no = tk.Label(root, text=innitNums[1], font=("Arial", 38, "bold"), fg="white", bg="green")
    bsystem_no.place(x=173, y=630)

# For user with penalty box
    person_frame = ctk.CTkFrame(root, width=int(0.02 * ww), height=int(0.01 * wh), fg_color="yellow green")
    person_frame.place(x=550, y=550)
    person_label = tk.Label(root, text="USERS WITH", wraplength="200", font=("Arial", 17, "bold"), fg="white", bg="yellow green")
    person_label.place (x=395, y=550)
    person_label = tk.Label(root, text="PENALTY", wraplength="200", font=("Arial", 17, "bold"), fg="red", bg="yellow green")
    person_label.place (x=395, y=575)
    person_label = ctk.CTkLabel(person_frame, image=person, text="")
    person_label.pack()

    bsystem_no = tk.Label(root, text=innitNums[2], font=("Arial", 38, "bold"), fg="white", bg="yellow green")
    bsystem_no.place(x=430, y=630)

# For 3 books design
    book_label = ctk.CTkLabel(root, image=book, text="")
    book_label.place(x=810, y=530)

# For data shown box
    data_label = ctk.CTkFrame(root, width=int(0.02 * ww), height=int(0.01 * wh), fg_color="green")
    data_label = tk.Label(root, text="DATA FROM", wraplength="150", font=("Arial", 23, "bold"), fg="white", bg="yellow green")
    data_label.place (x=1310, y=290, anchor="center")

    date1_bar = ctk.CTkEntry(root, width=220, height=70, corner_radius=0, fg_color='white',
                              text_color="dark gray", placeholder_text="YYYY-MM-DD", font=("Arial", 23))
    date1_bar.place(x=1210, y=350)

    to_label = tk.Label(root, text="TO", wraplength="200", font=("Arial", 26, "bold"), fg="white", bg="yellow green")
    to_label.place (x=1320, y=445, anchor="center")

    date2_bar = ctk.CTkEntry(root, width=220, height=70, corner_radius=0, fg_color='white',
                              text_color="dark gray", placeholder_text="YYYY-MM-DD", font=("Arial", 23))
    date2_bar.place(x=1320, y=510, anchor="center")
    def showData():
        global datefrom, dateTo
        try:
            datetime.strptime(date1_bar.get(), "%Y-%m-%d")
            datetime.strptime(date2_bar.get(), "%Y-%m-%d")
            datefrom = date1_bar.get()
            dateTo = date2_bar.get()
        except ValueError:
            notif_frame = ctk.CTkFrame(root, width=400, height=30, corner_radius=20, fg_color="light green", border_width=3, border_color="green")
            notif_frame.place(x=1320, y=650, anchor="center")  # Position the frame
    
    # Add the text label inside the frame
            notif_label = ctk.CTkLabel(notif_frame, text="Error: Date format should be YYYY-MM-DD", font=("Arial", 20), text_color="black", fg_color="light green")
            notif_label.place(relx=0.5, rely=0.5, anchor="center")  # Center text inside frame
            root.after(3000, lambda: notif_frame.place_forget())
            return
        borrow_count, return_count = BnRcount_rows(datefrom, dateTo)
        bookopen_no.config(text=borrow_count)
        returned_no.config(text=return_count)
    show_button = ctk.CTkButton(canvas, text="SHOW", width=280, height=40, corner_radius=50, 
                                   bg_color="yellow green", fg_color="green", font=("Arial", 24, 'bold'), text_color="White", command = showData)
    show_button.place(x=1320, y=590, anchor="center")  

# For under the export button
    csd_label = ctk.CTkFrame(root, width=int(0.02 * ww), height=int(0.01 * wh), fg_color="white")
    csd_label = ctk.CTkLabel (root, text='*Data will be sent to CSD', font = ("Arial", 15, 'bold'), text_color="Grey")
    csd_label.place (x=ww - 305, y=wh - 130)
    def on_frame_touch(event, frame):
        if event.widget == frame:
            frame.unbind("<Button-1>")
            return_to_idle()
    def exportData(export_button):
        global datefrom, dateTo
        print("button Interactive")
        if datefrom == None or dateTo == None:
            return
        export_button.configure(state="disabled")
        send_email_with_attachment("yourFranzkafka@gmail.com", datefrom, dateTo)
        Data_Send_page = tk.Frame(root, width=500, height=300, bg="green")
        Data_Send_page.pack(fill="both", expand=True)
        Data_Send_label = tk.Label(Data_Send_page, text='The data has been successfully emailed to CSD.' , fg="white", font=("Arial", 60, "bold"), 
                        bg="green", wraplength=1000)
        Data_Send_label.place(relx=0.5, rely=0.5, anchor="center")
        pop_up_label2 = tk.Label(Data_Send_page, text="Please touch the screen to continue", fg="white", 
                             font=("Arial", 20, "bold"), bg="green")
        pop_up_label2.place(relx=0.5, rely=0.80, anchor="center")
        Data_Send_label.bind("<Button-1>", lambda event: on_frame_touch(event, Data_Send_label))

    export_button = ctk.CTkButton(canvas, text="Export", width=331, height=60, corner_radius=50, 
                                   bg_color="white", fg_color="green", font=("Arial", 24, 'bold'), text_color="White", command = lambda: exportData(export_button))
    export_button.place(x=ww - 384, y=wh - 195)

    button_img = ctk.CTkImage(
    Image.open("button.png"),
    size=(75, 75)
)
    button = ctk.CTkButton(root, image=button_img, text="", fg_color="transparent", hover_color="lightgray", border_width=0, corner_radius=1000, command = return_to_idle)

    button.place(x=40, y=780)
