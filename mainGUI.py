# Yung mga imports na ito, para ma file naten yung functions naten na maayus
import tkinter as tk
import customtkinter as ctk
from tkinter import *
from PIL import Image, ImageTk
import tkinter.font as tkFont
from user_Profile import Main_user_page
from borrow_return import Main_borrow_return_page
from search import Main_search_page
from history import Main_history_page
from rules_regulation import Main_rules_page
from exit_function import Main_exit_page
from bnd import *
# INITIAL VARIABLES AND SET UP IS FROM 12-23 HERE
root = tk.Tk()
root.attributes('-fullscreen', True) #ensures uses fullscreen for our frames
container = tk.Frame(root) #container for all frames
container.pack(fill="both", expand=True)
sidebar = tk.Frame(container, width=200, bg='gray') 
content = tk.Frame(container) #this is where the pages itself will be placed
content.pack(side='right', fill='both', expand=True)
entry_page = tk.Frame(content)
entry_page.place(x=0, y=0, width=1720, height=1080)
image_path= Image.open("bg_entry.png")
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()
resized_image = image_path.resize((window_width, window_height), Image.Resampling.LANCZOS)  # Resize to fit screen
image_path = ImageTk.PhotoImage(resized_image)

### ALTERNATIVE DATA
profileInfo = ([(12345, 'Juan Dela Cruz', 'jdc@gmail.com', '23-10140-256', 1, 0)], [(1, 12345, 'jdc@gmail.com', 101, (2025, 
1, 26, 14, 30), (2025, 1, 30)), (2, 12345, 'jdc@gmail.com', 402, (2025, 1, 26, 10, 30), (2025, 1, 30))])
#this is only for the entry page, when the login button has been pressed
def open():
    Main_user_page(content)
    sidebar.pack(side='left', fill='y')
    entry_page.destroy()
#how the button of our sidebar will be placed and work
button1 = tk.Button(sidebar, text='User Profile', command= lambda: Main_user_page(content, profileInfo)) 
button1.pack(fill='x')
button2 = tk.Button(sidebar, text='Books', command=lambda: Main_borrow_return_page(content))
button2.pack(fill='x')
button3 = tk.Button(sidebar, text='Search', command=lambda: Main_search_page(content))
button3.pack(fill='x')
button4 = tk.Button(sidebar, text='History', command=lambda: Main_history_page(content))
button4.pack(fill='x')
button5 = tk.Button(sidebar, text='Rules', command=lambda: Main_rules_page(content))
button5.pack(fill='x')
button6 = tk.Button(sidebar, text='Exit', command=lambda: Main_exit_page(content))
button6.pack(fill="x")

#Entry Page
def Entry_Page():
# Create a Label widget to display the image
    bg_image = tk.Label(entry_page, image = image_path)
    bg_image.place(x=0, y=0)
    font_label = tkFont.Font(family="Poppins Bold", size=50)
    introText = f"Welcome to NEURead, {profileInfo[0][0][1]}"
    label = tk.Label(entry_page, sidebar.pack_forget(), text= introText, font=font_label) #add na lg kayu here ng variable for student
    label.place(x=450, y=350)
    
    font_button = tkFont.Font(family="Poppins Bold", size=15)
    button = tk.Button(entry_page, text='Login', font=font_button, bg="#004AAD", fg="white", width=18, command= lambda: open())
    button.place(x=690, y=500)
    entry_page.tkraise()

Entry_Page()

root.mainloop()