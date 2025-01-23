# Yung mga imports na ito, para ma file naten yung functions naten na maayus
import tkinter as tk

from user_Profile import Main_user_page
from borrow_return import Main_book_page
from search import Main_search_page
from history import Main_history_page
from rules_regulation import Main_rules_page
from exit_function import Main_exit_page

# INITIAL VARIABLES AND SET UP IS FROM 12-23 HERE
root = tk.Tk()
root.attributes('-fullscreen', True) #ensures uses fullscreen for our frames
container = tk.Frame(root) #container for all frames
container.pack(fill="both", expand=True)
sidebar = tk.Frame(container, width=200, bg='gray') 
content = tk.Frame(container) #this is where the pages itself will be placed
content.pack(side='right', fill='both', expand=True)
entry_page = tk.Frame(content)
entry_page.place(x=0, y=0, width=1720, height=1080)
#this is only for the entry page, when the login button has been pressed
def open():
    Main_user_page(content)
    sidebar.pack(side='left', fill='y')
    entry_page.destroy()
#how the button of our sidebar will be placed and work
button1 = tk.Button(sidebar, text='User Profile', command= lambda: Main_user_page(content)) 
button1.pack(fill='x')
button2 = tk.Button(sidebar, text='Books', command=lambda: Main_book_page(content))
button2.pack(fill='x')
button3 = tk.Button(sidebar, text='Search', command=lambda: Main_search_page(content))
button3.pack(fill='x')
button4 = tk.Button(sidebar, text='History', command=lambda: Main_history_page(content))
button4.pack(fill='x')
button5 = tk.Button(sidebar, text='Rules', command=lambda: Main_rules_page(content))
button5.pack(fill='x')
button6 = tk.Button(sidebar, text='Exit', command=lambda: Main_exit_page(content))
button6.pack(fill="x")

#Entry Page
def Entry_Page():
    label = tk.Label(entry_page, sidebar.pack_forget(), text='Welcome to NEURead', 
                     font=('Arial', 32)) #add na lg kayu here ng variable for student
    label.place(x=425, y=250)
    button = tk.Button(entry_page, text='Login', font=('Arial', 12), 
                       command= lambda: open())
    button.place(x=600, y=300, width=100)
    entry_page.tkraise()

Entry_Page()

root.mainloop()