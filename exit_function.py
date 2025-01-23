import tkinter as tk
from tkinter import ttk
# INITIAL VARIABLES HERE
def Main_exit_page(content):
    exit_page = tk.Frame(content)
    exit_page.place(x=0, y=0, width=1720, height=1080)
    label1 = tk.Label(exit_page, text='Welcome to exit page')
    label1.place(x=425, y=250)
    exit_page.tkraise(exit_page)