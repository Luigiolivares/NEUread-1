import tkinter as tk

# INITIAL VARIABLES HERE
def Main_book_page(content):
    frame = tk.Frame(content)
    frame.place(x=0, y=0, width=1720, height=1080)
    label1 = tk.Label(frame, text='Welcome to borrow and return page')
    label1.place(x=425, y=250)
    frame.tkraise(frame)