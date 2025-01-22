# Yung mga imports na ito, para ma file naten yung functions naten na maayus
import tkinter as tk
from User_Profile import user_page
from BorrowNReturn import books_page
from Search import search_page
from History import history_page
from RulesNRegulation import rules_page
from Exit_Function import exit_page

# INITIAL VARIABLES HERE
root = tk.Tk()
root.title("Kepler 9B Heavenly Body")
root.attributes('-fullscreen', True)
#ya ngl, idk why am I even leaving the root attributes there, container pack does the same thing, 
# but eh, Ima keep it as setimental value
container = tk.Frame(root)
container.pack(fill="both", expand=True)
#purpose of these 2 lines of codes is para makita ng user yung mga buttons easier, and also for me 
# para makita mas maayus, pero pag design nyo edit nyo na lg yung parameters
sidebar = tk.Frame(container, width=200, bg='gray')
sidebar.pack(side='left', fill='y')
#I know what you're thinking (naybe), bat need pa ba ng content if my container?
#it's cuz the container is the overall frame, sidebar san nakalagay yung buttons
#and the content is where, well, the content is
content = tk.Frame(container)
content.pack(side='right', fill='both', expand=True)
#ginawa ko lg tong range na to para more neat and more efficient ang pag run ng 
#program naten, literally the same lg sya sa ginawa kong na mahaba na code
#for the each individual frame
frames = [tk.Frame(content) for _ in range(6)]
user_page, books_page, search_page, history_page, rules_page, exit_page = frames
#ano lg to, pang ensure na when we switch frames, the frames the user clicked on will be shown
#para ensure na lahat na frames sa taas are parameters
for frame in frames:
    frame.place(x=0, y=0, width=1720, height=1080)
#this is where the magic happens, this is where the frames are switched man :))))
def show_frame(frame):
    frame.tkraise()
#pang hide lg to sa side bar ng entry page naten
def hide_sidebar():
    sidebar.pack_forget()
#para may pang balik sa side bar after hidden sya
def show_sidebar():
    sidebar.pack(side='left', fill='y')
#command function naten para ma show yung frame na gusto naten
def switch_wee_woo(frame):
    def show():
        show_frame(frame)
    return show
#This is just where lang naman kung san buttons would be created and placed, and the commands would be 
#assigned to them
def create_sidebar_button(text, frame):
    button = tk.Button(sidebar, text=text, command=switch_wee_woo(frame))    
    button.pack(fill='x')
#pang assignment lg ng future files naten bout sa pages naten, their buttons and their functions
def create_sidebar_buttons():
    buttons_info = [
        ('User Profile', user_page),
        ('Books', books_page),
        ('Search', search_page),
        ('History', history_page),
        ('Rules', rules_page),
        ('Exit', exit_page)
    ]

    for text, frame in buttons_info:
        create_sidebar_button(text, frame)

#ito, just for the entry message lg naten talaga, ngl, dito ko amp nairita, akala ko dapat seperate page
#ren to, pero dito lg ren sya pala sa main, paulut ulit pa naman nag kakaroon na circular import error
#na sayamg ko amp 1-2 hrs ko here trying to make a seperate page for this work, but eh, nvm:((((((()
entry_page = tk.Frame(content)
entry_page.place(x=0, y=0, width=1720, height=1080)

label = tk.Label(entry_page, text='Welcome to NEURead', font=('Arial', 32))
label.place(x=425, y=250)

def open():
    show_frame(user_page)
    show_sidebar()
#edit mo to future me, galit ka lg amp
thefucku_button = tk.Button(entry_page, text='Login', font=('Arial', 12), 
                            command=open)
thefucku_button.place(x=600, 
                      y=300, width=100)
#ito para make sure na after entry page, pupunta na sya sa main functions nya and also to start the program
if __name__ == "__main__":
    create_sidebar_buttons()
    hide_sidebar()
    show_frame(entry_page)
    root.mainloop()
