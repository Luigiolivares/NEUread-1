import tkinter as tk
import random

def Main_borrow_return_page(content):
    frame = create_frame(content)
    
    tk.Label(frame, text='Books Section', font=('Arial', 24)).place(x=600, y=100)
    
    tk.Button(frame, text="Borrow", font=('Arial', 14), command=lambda: borrow_page(content)).place(x=600, y=300, width=200)
    tk.Button(frame, text="Return", font=('Arial', 14), command=lambda: return_page(content)).place(x=600, y=400, width=200)
    
    frame.tkraise()

def borrow_page(content):
    frame = create_frame(content)
    
    label = tk.Label(frame, text='Borrow Books', font=('Arial', 24))
    label.place(x=600, y=100)
    
    subheading = tk.Label(frame, text='Please Tap Librarian ID Card on the reader', font=('Arial', 16))
    subheading.place(x=500, y=150)
    
    frame.after(3000, lambda: subheading.config(text='Please type in the Book ID'))
    frame.after(6000, lambda: subheading.config(text='Please Tap Student ID Card on the reader'))
    frame.after(9000, lambda: thank_you_page(content))
    
    frame.tkraise()

def return_page(content):
    frame = create_frame(content)
    
    label = tk.Label(frame, text='Return Books', font=('Arial', 24))
    label.place(x=600, y=100)
    
    subheading = tk.Label(frame, text='Please Tap Librarian ID Card on the reader', font=('Arial', 16))
    subheading.place(x=500, y=150)
    
    frame.after(2000, lambda: subheading.config(text='Please type in the Book ID'))
    frame.after(4000, lambda: subheading.config(text='Please Tap Student ID Card on the reader'))
    frame.after(6000, lambda: thank_you_page(content))
    
    frame.tkraise()

def thank_you_page(content):
    for widget in content.winfo_children():
        widget.destroy()
    
    content.configure(bg="mistyrose")
    
    canvas = tk.Canvas(content, bg="mistyrose")
    canvas.pack(fill="both", expand=True)
    
    stars = create_twinkle_stars(canvas, content)
    
    tk.Label(content, text="Transaction Successful", font=("Times New Roman", 50, "bold"), fg="green", bg="mistyrose").place(relx=0.5, rely=0.4, anchor="center")
    tk.Label(content, text="THANK YOU FOR USING NEURead!", font=("Times New Roman", 60), fg="salmon", bg="mistyrose").place(relx=0.5, rely=0.5, anchor="center")
    tk.Button(content, text="EXIT", font=("Arial", 25), bg="thistle", fg="black", command=lambda: Main_borrow_return_page(content)).place(relx=0.5, rely=0.8, anchor="center")

def create_twinkle_stars(canvas, content):
    stars = []
    for _ in range(50):
        x, y = random.randint(0, content.winfo_screenwidth()), random.randint(0, content.winfo_screenheight())
        size = random.randint(2, 5)
        star = canvas.create_oval(x, y, x + size, y + size, fill="white")
        stars.append((star, x, y, size))
    
    def twinkle():
        for star, x, y, size in stars:
            new_size = max(2, min(5, size + random.choice([-1, 0, 1])))
            canvas.coords(star, x, y, x + new_size, y + new_size)
            canvas.itemconfig(star, fill=random.choice(["white", "lightblue", "yellow"]))
        content.after(300, twinkle)
    
    twinkle()
    return stars

def create_frame(content):
    frame = tk.Frame(content)
    frame.place(x=0, y=0, width=1720, height=1080)
    return frame