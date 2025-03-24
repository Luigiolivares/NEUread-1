import tkinter as tk
import customtkinter as ctk
from pywinstyles import set_opacity
from PIL import Image, ImageTk  # Import Pillow for image resizing

# Create main window
root = tk.Tk()
root.title("Password Bar Admin")
root.attributes("-fullscreen", True)

ww = root.winfo_screenwidth()
wh = root.winfo_screenheight()

# Load and resize background image dynamically
original_bg = Image.open("Admin Interface Design.png")  # Load image
resized_bg = original_bg.resize((ww, wh))  # Resize to screen size (ANTIALIAS is no longer needed)
bg_image = ImageTk.PhotoImage(resized_bg)  # Convert for Tkinter

content = ctk.CTkFrame(root)
content.pack(fill="both", expand=True)

def admin(content):
    frame = tk.Frame(content)
    frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Set background image properly
    bg = tk.Label(frame, image=bg_image)
    bg.place(relx=0, rely=0, relwidth=1, relheight=1)

    password_frame = ctk.CTkFrame(frame, width=1350, height=700, fg_color="white", border_color="grey")
    password_frame.place(relx=0.5, rely=0.5, anchor= "center")

    set_opacity(password_frame, value=0.8)

    enter_password = ctk.CTkLabel(password_frame, text="Enter The Password\nTo Proceed", 
                                  font=("Arial", 75, 'bold'), text_color="Black")
    enter_password.place(relx=0.5, rely=0.3, anchor="center")

    password = ctk.CTkEntry(password_frame, width=650, height=65, font=("Arial", 32, 'bold'), 
                            fg_color="dark sea green", text_color="Black", corner_radius=50, border_width=0)
    password.place(relx=0.26, rely=0.5)

    enter_option = ctk.CTkButton(password_frame, text="Log Out", width=200, height=60, corner_radius=50, 
                                 bg_color="white", fg_color="green", font=("Arial", 32, 'bold'), text_color="White")
    enter_option.place(relx=0.35, rely=0.67)

    cancel_option = ctk.CTkButton(password_frame, text="Cancel", width=200, height=60, corner_radius=50, 
                                  bg_color="white", border_width=5, border_color='green', fg_color="white", 
                                  font=("Arial", 24, 'bold'), text_color="Green")
    cancel_option.place(relx=0.51, rely=0.67)

admin(content)
root.mainloop()