import tkinter as tk
from profilePage import *
# INITIAL VARIABLES HERE
root = tk.Tk()
root.title("Kepler 9B Heavenly Body")
root.attributes('-fullscreen', True)

container = tk.Frame(root)
container.pack(fill="both", expand=True)

sidebar = tk.Frame(container, width=200, bg='gray')

content = tk.Frame(container)
content.pack(side='right', fill='both', expand=True)

entry_page = tk.Frame(content)
user_page = tk.Frame(content)
books_page = tk.Frame(content)
search_page = tk.Frame(content)
history_page = tk.Frame(content)
rules_page = tk.Frame(content)
exit_page = tk.Frame(content)

#sizing of frames
for frame in (entry_page, user_page, books_page, search_page, history_page, rules_page, exit_page):
    frame.place(x=0, y=0, width=1720, height=1080)  

def show_frame(frame):
    frame.tkraise()

# MGA FUNCTIONS IN CALLING PAGES/FRAME
def Entry_Page():
    label = tk.Label(entry_page, text='Welcome to NEURead', 
                     font=('Arial', 32)) #add na lg kayu here ng variable for student
    label.place(x=425, y=250)
    button = tk.Button(entry_page, text='Login', font=('Arial', 12), 
                       command=lambda: [show_frame(user_page), show_sidebar()])
    button.place(x=600, y=300, width=100)
    show_frame(entry_page)
    hide_sidebar() 

def user_profile():
    label1 = tk.Label(user_page, text='Welcome to User Profile')
    label1.place(x=425, y=250)

def hide_sidebar():
    sidebar.pack_forget()

def show_sidebar():
    sidebar.pack(side='left', fill='y')

# Add buttons to the sidebar
button1 = tk.Button(sidebar, text='User Profile', command=lambda: show_frame(user_page))
button1.pack(fill='x')
button2 = tk.Button(sidebar, text='Books', command=lambda: show_frame(books_page))
button2.pack(fill='x')
button3 = tk.Button(sidebar, text='Search', command=lambda: show_frame(search_page))
button3.pack(fill='x')
button4 = tk.Button(sidebar, text='History', command=lambda: show_frame(history_page))
button4.pack(fill='x')
button5 = tk.Button(sidebar, text='Rules', command=lambda: show_frame(rules_page))
button5.pack(fill='x')
button6 = tk.Button(sidebar, text='Exit', command=lambda: show_frame(exit_page))
button6.pack(fill='x')

Entry_Page()

root.mainloop()