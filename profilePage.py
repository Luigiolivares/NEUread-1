import tkinter as tk

def user_profile(profile_page):
    profile_page.place(x=0, y=0, width=1720, height=1080)  
    label1 = tk.Label(profile_page, text='Welcome to User Profile')
    label1.place(x=425, y=250)
    print("working")