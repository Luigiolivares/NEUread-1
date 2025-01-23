import tkinter as tk 

def Main_user_page(content):
    user_page = tk.Frame(content)
    user_page.place(x=0, y=0, width=1720, height=1080)
    label1 = tk.Label(user_page, text='Welcome to User Profile')
    label1.place(x=425, y=250)
    user_page.tkraise(user_page)