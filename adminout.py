import customtkinter as ctk
import tkinter as tk
from PIL import Image
from pywinstyles import set_opacity

root = tk.Tk()
root.title("borrow")
root.attributes('-fullscreen', True)

ww = root.winfo_screenwidth()
wh = root.winfo_screenheight()

content = ctk.CTkFrame(root)
content.pack(fill="both", expand=True)

bg_image = tk.PhotoImage(file = 'Admin_Interface_Design.png')

def admin_logout():
    frame = tk.Frame(content)
    frame.place(width=ww, height=wh)

    bg = tk.Label(frame, image=bg_image)
    bg.place(width=ww, height=wh)

    log_out = ctk.CTkFrame(frame, width=1350 , height=700, bg_color="grey", fg_color="white")
    log_out.place(relx=0.5, rely=0.5, anchor= "center")

    set_opacity(log_out, value=0.8)

    question = ctk.CTkLabel(log_out, text="Are You Sure You Want\nTo Log Out?", font=("Arial", 60, 'bold'), text_color="Black")
    question.place(relx=0.5, rely=0.45, anchor="center")

    log_out_option = ctk.CTkButton(log_out, text="Log Out", width=200, height=60, corner_radius=50, 
                                   bg_color="white", fg_color="green", font=("Arial", 24, 'bold'), text_color="White")
    log_out_option.place(relx=0.35, rely=0.6)

    cancel_option = ctk.CTkButton(log_out, text="Cancel", width=200, height=60, corner_radius=50, bg_color="white", border_width=5, border_color='green', fg_color="white", font=("Arial", 24, 'bold'), text_color="Green")
    cancel_option.place(relx=0.51, rely=0.6)

admin_logout()

root.mainloop()