import tkinter as tk
from tkinter import ttk

# INITIAL VARIABLES HERE
def Main_search_page(content):
    search_page = tk.Frame(content)
    search_page.place(x=0, y=0, width=1720, height=1080)
    label1 = tk.Label(search_page, text='Welcome to Search page')
    label1.place(x=425, y=250)
    entry = tk.Entry(search_page, width=75)
    entry.place(x = 300, y = 300)
    search_page.tkraise()
    def enter():
        x= entry.get()
        print(x)
    button1 = tk.Button(search_page, text='search buttun', command= enter) 
    button1.pack(pady = 400, padx = 250)