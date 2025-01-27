import tkinter as tk

# INITIAL VARIABLES HERE
def Main_book_page(content):
    frame = tk.Frame(content)
    frame.place(x=0, y=0, width=1720, height=1080)
    label = tk.Label(frame, text='Books Section', font=('Arial', 24))
    label.place(x=600, y=100)
    borrow_button = tk.Button(frame, text="Borrow", font=('Arial', 14), command=lambda: Borrow_page(content))
    borrow_button.place(x=600, y=300, width=200)
    return_button = tk.Button(frame, text="Return", font=('Arial', 14), command=lambda: Return_page(content))
    return_button.place(x=600, y=400, width=200)
    frame.tkraise()

def Borrow_page(content):
    frame = tk.Frame(content)
    frame.place(x=0, y=0, width=1720, height=1080)
    label = tk.Label(frame, text='Borrow Books', font=('Arial', 24))
    label.place(x=600, y=100)
    subheading = tk.Label(frame, text='Please Tap Librarian ID Card on the reader', font=('Arial', 16))
    subheading.place(x=500, y=150)

     # visual kinemerut kunwari tapos na mag-tap ng librarian ALSO HINDI K ALAM PAANO I CENTER HUHU
    frame.after(3000, lambda: subheading.config(text='Please type in the Book ID'))

    # after mag-type ng book ID
    frame.after(6000, lambda: subheading.config(text='Please Tap Student ID Card on the reader'))

    back_button = tk.Button(frame, text="Back", font=('Arial', 14), command=lambda: Main_book_page(content))
    back_button.place(x=600, y=600, width=200)
    frame.tkraise()

def Return_page(content):
    frame = tk.Frame(content)
    frame.place(x=0, y=0, width=1720, height=1080)
    label = tk.Label(frame, text='Return Books', font=('Arial', 24))
    label.place(x=600, y=100)
    subheading = tk.Label(frame, text='Please Tap Librarian ID Card on the reader', font=('Arial', 16))
    subheading.place(x=500, y=150)

     # for visualization only
    frame.after(3000, lambda: subheading.config(text='Please type in the Book ID'))

    # for visualization only
    frame.after(6000, lambda: subheading.config(text='Please Tap Student ID Card on the reader'))

    back_button = tk.Button(frame, text="Back", font=('Arial', 14), command=lambda: Main_book_page(content))
    back_button.place(x=600, y=600, width=200)
    frame.tkraise()