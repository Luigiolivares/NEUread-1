import tkinter as tk
from tkinter import ttk

# INITIAL VARIABLES HERE
def Main_search_page(content):
    search_page = tk.Frame(content)
    search_page.place(x=0, y=0, width=1720, height=1080)
    label1 = tk.Label(search_page, text='Welcome to Search page')
    label1.place(x=425, y=250)
    search_page.tkraise(search_page)