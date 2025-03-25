import tkinter as tk
from tkinter import Canvas
import customtkinter as ctk
from PIL import Image

root = tk.Tk()
root.title("Admin Page")
root.attributes('-fullscreen', True)
root.configure(bg="white")
ww = root.winfo_screenwidth()
wh = root.winfo_screenheight()

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

canvas = Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), bg="white")
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

title_label = tk.Label(root, text="Hello, Admin!", font=("Arial", 47, "bold"), fg="green", bg="white")
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

bookopen_no = tk.Label(root, text="15", font=("Arial", 38, "bold"), fg="white", bg="yellow green")
bookopen_no.place(x=411, y=350)

# For returned books box
returned_label= ctk.CTkFrame(root, width=int(0.02 * ww), height=int(0.01 * wh), fg_color="green")
returned_label = tk.Label(root, text="RETURNED BOOKS", wraplength="200", font=("Arial", 17, "bold"), fg="white", bg="green")
returned_label.place (x=598, y=270)

returned_no = tk.Label(root, text="6", font=("Arial", 38, "bold"), fg="white", bg="green")
returned_no.place(x=644, y=350)

# For user registered box
registered_label = ctk.CTkFrame(root, width=int(0.02 * ww), height=int(0.01 * wh), fg_color="green")
registered_label = tk.Label(root, text="USER REGISTERED", wraplength="200", font=("Arial", 17, "bold"), fg="white", bg="green")
registered_label.place (x=900, y=265)

registered_no = tk.Label(root, text="346", font=("Arial", 38, "bold"), fg="white", bg="green")
registered_no.place(x=932, y=350)

# For books in the system box
bsystem_label = ctk.CTkFrame(root, width=int(0.02 * ww), height=int(0.01 * wh), fg_color="green")
bsystem_label = tk.Label(root, text="BOOKS IN THE SYSTEM", wraplength="200", font=("Arial", 17, "bold"), fg="white", bg="green")
bsystem_label.place (x=120, y=550)

bsystem_no = tk.Label(root, text="34", font=("Arial", 38, "bold"), fg="white", bg="green")
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

bsystem_no = tk.Label(root, text="5", font=("Arial", 38, "bold"), fg="white", bg="yellow green")
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

export_button = ctk.CTkButton(canvas, text="SHOW", width=280, height=40, corner_radius=50, 
                                   bg_color="yellow green", fg_color="green", font=("Arial", 24, 'bold'), text_color="White")
export_button.place(x=1320, y=590, anchor="center")  

# For under the export button
csd_label = ctk.CTkFrame(root, width=int(0.02 * ww), height=int(0.01 * wh), fg_color="white")
csd_label = ctk.CTkLabel (root, text='*Data will be sent to CSD', font = ("Arial", 15, 'bold'), text_color="Grey")
csd_label.place (x=ww - 305, y=wh - 130)

export_button = ctk.CTkButton(canvas, text="Export", width=331, height=60, corner_radius=50, 
                                   bg_color="white", fg_color="green", font=("Arial", 24, 'bold'), text_color="White")
export_button.place(x=ww - 384, y=wh - 195)

button_img = ctk.CTkImage(
    Image.open("button.png"),
    size=(75, 75)
)
button = ctk.CTkButton(root, image=button_img, text="", fg_color="transparent", hover_color="lightgray", border_width=0, corner_radius=1000,
)

button.place(x=40, y=780)

root.mainloop()