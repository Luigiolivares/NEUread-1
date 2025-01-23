import tkinter as tk
from tkinter import ttk
# INITIAL VARIABLES HERE
def Main_rules_page(content):
    rules_page = tk.Frame(content)
    rules_page.place(x=0, y=0, width=1720, height=1080)
    label1 = tk.Label(rules_page, text='Welcome to Rules and Regulation page')
    label1.place(x=425, y=250)
    rules_page.tkraise(rules_page)