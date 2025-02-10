import tkinter as tk 
import customtkinter as ctk
def Main_user_page(content, profileInfo):
    name = profileInfo[0][0][1]
    user_page = tk.Frame(content)
    user_page.place(x=0, y=0, width=1720, height=1080)
 # Box 1 with a red background
    box1 = ctk.CTkFrame(user_page, width=1300, height=200, fg_color="red", corner_radius=20)
    box1.place(x=120, y=140)
    label1 = ctk.CTkLabel(box1, text="Box 1", text_color="white")
    label1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    # Box 2 with a green background
    box2 = ctk.CTkFrame(user_page, width=1300, height=400, fg_color="green", corner_radius=20)
    box2.place(x=120, y=400)
    label2 = ctk.CTkLabel(box2, text="Box 2", text_color="white")
    label2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    user_page.tkraise()