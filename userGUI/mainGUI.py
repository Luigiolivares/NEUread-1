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
from rules_regulation import initiateMainReg
from exit_function import Main_exit_page
import sys
import os
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
    profileInfo = getUserInfo(RFID)
    print(RFID)
    # Sidebar Buttons
 # Load Sidebar Icons
    button1_icon = ImageTk.PhotoImage(Image.open("btn1.png").resize((80,80)))
    button2_icon = ImageTk.PhotoImage(Image.open("btn2.png").resize((80,80)))
    button3_icon = ImageTk.PhotoImage(Image.open("btn3.png").resize((80,80)))
    button4_icon = ImageTk.PhotoImage(Image.open("btn4.png").resize((80,80)))
    button5_icon = ImageTk.PhotoImage(Image.open("btn5.png").resize((80,80)))
    button6_icon = ImageTk.PhotoImage(Image.open("btn6.png").resize((80,80)))
    # Track the currently active button

    button1 = tk.Button(sidebar, command=lambda: Main_user_page(content, RFID, root), image=button1_icon, compound='left', bg='#004AAD', bd=0) 
    button1.image = button1_icon
    button1.pack(fill='x', expand =True, pady=1)
    
    button2 = tk.Button(sidebar, command=lambda: Main_borrow_return_page(content, profileInfo[0][0][0], root), image=button2_icon, compound='left', bg='#004AAD', bd=0)
    button2.image = button2_icon
    button2.pack(fill='x', expand=True, pady=1)
    
    button3 = tk.Button(sidebar, command=lambda: Main_search_page(content), image=button3_icon, compound='left', bg='#004AAD', bd=0)
    button3.image = button3_icon
    button3.pack(fill='x', expand=True, pady=1)

    button4 = tk.Button(sidebar, command=lambda: Main_history_page(content, profileInfo[0][0][0]), image=button4_icon, compound='left', bg='#004AAD', bd=0)
    button4.image = button4_icon
    button4.pack(fill='x', expand=True, pady=1)

    button5 = tk.Button(sidebar, command=lambda: initiateMainReg(content), image=button5_icon, compound='left', bg='#004AAD', bd=0)
    button5.image = button5_icon
    button5.pack(fill='x', expand=True, pady=1)

    button6 = tk.Button(sidebar, command=lambda: Main_exit_page(content, return_to_idle), image=button6_icon, compound='left', bg='#004AAD', bd=0)
    button6.image = button6_icon
    button6.pack(fill="x", expand=True, pady=1)

    # Entry Page (Login Screen)
    def proceedProfile(event, popUp):
        if event.widget == popUp:
            Main_user_page(content, RFID, root)
            popUp.unbind("<Button-1>")
            popUp.destroy()

    sidebar.pack(side='left', fill='y')
    
    pop_up_page = tk.Frame(content, width=500, height=300, bg="dark blue")
    pop_up_page.pack(fill="both", expand=True)

    pop_up_label = tk.Label(pop_up_page, text="Welcome to NEURead!", fg="white", font=("Arial", 60, "bold"), bg="dark blue")
    pop_up_label.place(relx=0.5, rely=0.45, anchor="center")

    pop_up_label2 = tk.Label(pop_up_page, text="Please touch the screen to continue", fg="white", font=("Arial", 20, "bold"), bg="dark blue")
    pop_up_label2.place(relx=0.5, rely=0.80, anchor="center")

    pop_up_page.bind("<Button-1>", lambda event: proceedProfile(event, pop_up_page))
