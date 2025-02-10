import tkinter as tk
from datetime import datetime
from tkinter import *
from bnd import *
#GLOBAL VARIABLES HERE
showBook = 0
def Main_history_page(content, RFID):
    history_page = tk.Frame(content)
    history_page.place(x=0, y=0, width=1720, height=1080)
    header_frame = tk.Frame(history_page, bg="#ffffff", height=100)
    header_frame.pack(fill="x")
    scrollbar = Scrollbar(content)
    frame_height = content.winfo_height()  # Get the frame's current height
    scrollbar.place(x=content.winfo_width() - 20, y=0, height=frame_height)
    current_time = datetime.now()
    date_label = tk.Label(header_frame, text= current_time.strftime("%d %B, %Y %I:%M %p"), font=("Arial", 20), bg="#ffffff", fg="#333333")
    date_label.pack(side="left", padx=20)
    history_page.after(1000, lambda: date_label.config(text=current_time.strftime("%d %B, %Y %I:%M %p"))) 
    def nextButtonFunction(purpose):
        print(RFID)
        global showBook
        if purpose:
            showBook += 2
        else:
            showBook -= 4
        print(showBorrowHistory(RFID, showBook + 2, showBook))
    print(showBorrowHistory(RFID, showBook + 2, showBook))
    nextButton = tk.Button(history_page, text='Next button', command = lambda: nextButtonFunction(True))
    nextButton.place(x=500, y=400)
    prevButton = tk.Button(history_page, text='Prev button', command = lambda: nextButtonFunction(False))
    prevButton.place(x=600, y=400)
    university_label = tk.Label(
        header_frame,
        text="New Era University",
        font=("Arial", 20),
        bg="#ffffff",
        fg="#333333",
    )
    showBorrowHistory(RFID, showBook, 0)
    university_label.place(relx=0.85, rely=0.5, anchor="e")  

    title_label = tk.Label(
        history_page,
        text="Book History",
        font=("Arial", 30, "bold"),
        bg="#ffffff",
        fg="#2a5599"
    )
    
    title_label.place(relx=0.43, rely=0.1, anchor="center") 
    history_page.tkraise(history_page)