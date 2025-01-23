import tkinter as tk
from tkinter import ttk
# INITIAL VARIABLES HERE
def Main_history_page(content):
    history_page = tk.Frame(content)
    history_page.place(x=0, y=0, width=1720, height=1080)
    label1 = tk.Label(history_page, text='Welcome to History page')
    label1.place(x=425, y=250)
    history_page.tkraise(history_page)