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
def start_neuread_app(RFID, root):
    # Main Containers
    container = tk.Frame(root)
    container.pack(fill="both", expand=True)

    sidebar = tk.Frame(container, width=200, bg='gray') 
    content = tk.Frame(container)  # The frame where pages will be placed
    content.pack(side='right', fill='both', expand=True)

    entry_page = tk.Frame(content)
    entry_page.place(x=0, y=0, width=1720, height=1080)

    # Load and Resize Background Image
    image_path = Image.open("bg_entry.png")
    window_width = root.winfo_screenwidth()
    window_height = root.winfo_screenheight()
    resized_image = image_path.resize((window_width, window_height), Image.Resampling.LANCZOS)  
    image_path = ImageTk.PhotoImage(resized_image)

    # Sample Profile Information
    profileInfo = ([(75240, 'Althe Moldez', 'AlthMldz@gmail.com', '-10626', 1, 0)], [])

    # Function to Switch to Main User Page
    def open_main_page():
        entry_page.destroy()
        Main_user_page(content, profileInfo)
        sidebar.pack(side='left', fill='y')
        entry_page.destroy()

    # Sidebar Buttons
    button1 = tk.Button(sidebar, text='User Profile', command=lambda: Main_user_page(content, profileInfo)) 
    button1.pack(fill='x')
    
    button2 = tk.Button(sidebar, text='Books', command=lambda: Main_borrow_return_page(content))
    button2.pack(fill='x')

    button3 = tk.Button(sidebar, text='Search', command=lambda: Main_search_page(content))
    button3.pack(fill='x')

    button4 = tk.Button(sidebar, text='History', command=lambda: Main_history_page(content, profileInfo[0][0][0]))
    button4.pack(fill='x')

    button5 = tk.Button(sidebar, text='Rules', command=lambda: Main_rules_page(content))
    button5.pack(fill='x')

    button6 = tk.Button(sidebar, text='Exit', command=lambda: Main_exit_page(content))
    button6.pack(fill="x")

    # Entry Page (Login Screen)
    #def entry_page_screen():
        # Background Image
    entry_page.image_path = image_path
    bg_image = tk.Label(entry_page, image = image_path)
    bg_image.place(x=0, y=0)

        # Welcome Text
    font_label = tkFont.Font(family="Poppins Bold", size=50)
    introText = f"Welcome to NEURead,\n {profileInfo[0][0][1]}"
    label = tk.Label(entry_page, text=introText, font=font_label, bg="white")
    label.place(x=450, y=350)

        # Login Button
    font_button = tkFont.Font(family="Poppins Bold", size=15)
    button = tk.Button(entry_page, text='Login', font=font_button, bg="#004AAD", fg="white", width=18, command=open_main_page)
    button.place(x=690, y=500)

    entry_page.tkraise()