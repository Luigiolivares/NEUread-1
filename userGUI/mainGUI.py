# Yung mga imports na ito, para ma file naten yung functions naten na maayus
import sys
import os

# Get the directory of mainGUI.py
main_gui_path = os.path.dirname(os.path.abspath(__file__))

# Ensure userGUI/ is in sys.path
if main_gui_path not in sys.path:
    sys.path.append(main_gui_path)

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
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from bnd import *
def start_neuread_app(RFID, root, return_to_idle):
    # Main Containers
    container = tk.Frame(root)
    container.pack(fill="both", expand=True)

    sidebar = tk.Frame(container, width=300, bg='#004AAD', bd = 0) 
    content = tk.Frame(container)  # The frame where pages will be placed
    content.pack(side='right', fill='both', expand=True)
        # Load and Resize Background Image
    image_path = Image.open("bg_entry.png")
    window_width = root.winfo_screenwidth()
    window_height = root.winfo_screenheight()

    entry_page = tk.Frame(content)
    entry_page.place(x=0, y=0, width=window_width, height=window_height)

    resized_image = image_path.resize((window_width, window_height), Image.Resampling.LANCZOS)  
    image_path = ImageTk.PhotoImage(resized_image)

    # Sample Profile Information
    profileInfo = ([("0010567289", 'Kate Zayen Echalose', 'katezayen.echalose@neu.edu.ph', '23-10338-159', 1, 0)], [])

    # Function to Switch to Main User Page
    def open_main_page():
        entry_page.destroy()
        Main_user_page(content, profileInfo)
        sidebar.pack(side='left', fill='y')
        entry_page.destroy()

    # Sidebar Buttons
 # Load Sidebar Icons
    button1_icon = ImageTk.PhotoImage(Image.open("btn1.png").resize((60,60)))
    button2_icon = ImageTk.PhotoImage(Image.open("btn2.png").resize((60,60)))
    button3_icon = ImageTk.PhotoImage(Image.open("btn3.png").resize((60,60)))
    button4_icon = ImageTk.PhotoImage(Image.open("btn4.png").resize((60,60)))
    button5_icon = ImageTk.PhotoImage(Image.open("btn5.png").resize((60,60)))
    button6_icon = ImageTk.PhotoImage(Image.open("btn6.png").resize((60,60)))
    # Track the currently active button

    button1 = tk.Button(sidebar, command=lambda: Main_user_page(content, profileInfo), image=button1_icon, compound='left', bg='#004AAD', bd=0) 
    button1.image = button1_icon
    button1.pack(fill='x', expand =True, pady=5)
    
    button2 = tk.Button(sidebar, command=lambda: Main_borrow_return_page(content), image=button2_icon, compound='left', bg='#004AAD', bd=0)
    button2.image = button2_icon
    button2.pack(fill='x', expand=True, pady=5)
    
    button3 = tk.Button(sidebar, command=lambda: Main_search_page(content), image=button3_icon, compound='left', bg='#004AAD', bd=0)
    button3.image = button3_icon
    button3.pack(fill='x', expand=True, pady=5)

    button4 = tk.Button(sidebar, command=lambda: Main_history_page(content, profileInfo[0][0][0]), image=button4_icon, compound='left', bg='#004AAD', bd=0)
    button4.image = button4_icon
    button4.pack(fill='x', expand=True, pady=5)

    button5 = tk.Button(sidebar, command=lambda: Main_rules_page(content, window_width, window_height), image=button5_icon, compound='left', bg='#004AAD', bd=0)
    button5.image = button5_icon
    button5.pack(fill='x', expand=True, pady=5)

    button6 = tk.Button(sidebar, command=lambda: Main_exit_page(content, return_to_idle), image=button6_icon, compound='left', bg='#004AAD', bd=0)
    button6.image = button6_icon
    button6.pack(fill="x", expand=True, pady=5)

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
    label.place(x=(window_width * 0.26), y=(0.32 * window_height))

        # Login Button
    font_button = tkFont.Font(family="Poppins Bold", size=15)
    button = tk.Button(entry_page, text='Login', font=font_button, bg="#004AAD", fg="white", width=18, command=open_main_page)
    button.place(x=(0.40 * window_width), y=(0.46 * window_width))

    entry_page.tkraise()