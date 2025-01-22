import tkinter as tk
# INITIAL VARIABLES HERE
root = tk.Tk()
root.title("Kepler 9B Heavenly Body")
root.attributes('-fullscreen', True)

container = tk.Frame(root)
container.pack(fill="both", expand=True)

sidebar = tk.Frame(container, width=200, bg='gray')

content = tk.Frame(container)
content.pack(side='right', fill='both', expand=True)

#initializing the variables of each frames(pages)
entry_frame = tk.Frame(content)
user_frame = tk.Frame(content)
books_frame = tk.Frame(content)
search_frame = tk.Frame(content)
history_frame = tk.Frame(content)
rules_frame = tk.Frame(content)
exit_frame = tk.Frame(content)

#sizing of frames
for frame in (entry_frame, user_frame, books_frame, search_frame, history_frame, rules_frame, exit_frame):
    frame.place(x=0, y=0, width=1720, height=1080)  

def show_frame(frame):
    frame.tkraise()

# MGA FUNCTIONS IN CALLING PAGES/FRAME
def Entry_Page():
    label = tk.Label(entry_frame, text='Welcome to NEURead', 
                     font=('Arial', 32)) #add na lg kayu here ng variable for student
    label.place(x=425, y=250)
    button = tk.Button(entry_frame, text='Login', font=('Arial', 12), 
                       command=lambda: [show_frame(user_frame), show_sidebar()])
    button.place(x=600, y=300, width=100)
    show_frame(entry_frame)
    hide_sidebar() 

def user_profile():
    label1 = tk.Label(user_frame, text='Welcome to User Profile')
    label1.place(x=425, y=250)

def hide_sidebar():
    sidebar.pack_forget()

def show_sidebar():
    sidebar.pack(side='left', fill='y')

# Add buttons to the sidebar
button1 = tk.Button(sidebar, text='User Profile', command=lambda: show_frame(user_frame))
button1.pack(fill='x')
button2 = tk.Button(sidebar, text='Books', command=lambda: show_frame(books_frame))
button2.pack(fill='x')
button3 = tk.Button(sidebar, text='Search', command=lambda: show_frame(search_frame))
button3.pack(fill='x')
button4 = tk.Button(sidebar, text='History', command=lambda: show_frame(history_frame))
button4.pack(fill='x')
button5 = tk.Button(sidebar, text='Rules', command=lambda: show_frame(rules_frame))
button5.pack(fill='x')
button6 = tk.Button(sidebar, text='Exit', command=lambda: show_frame(exit_frame))
button6.pack(fill='x')

Entry_Page()
user_profile()

root.mainloop()