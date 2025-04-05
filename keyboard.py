import customtkinter as ctk
import tkinter as tk

class CTkOnScreenKeyboard:
    instance = None
    keyboard_closed_once = False  # Flag to prevent auto-popup after close

    def __init__(self, master, entry):
        if CTkOnScreenKeyboard.instance:
            CTkOnScreenKeyboard.instance.top.lift()
            return

        # If the keyboard was closed before, ignore future auto-opens
        if CTkOnScreenKeyboard.keyboard_closed_once:
            return

        self.entry = entry
        self.master = master

        self.top = ctk.CTkToplevel(master)
        self.top.title("Keyboard")
        self.top.geometry("600x250")
        self.top.attributes('-topmost', True)
        self.top.resizable(False, False)
        self.top.wm_attributes('-toolwindow', True)

        self.top.protocol("WM_DELETE_WINDOW", self.on_close)

        CTkOnScreenKeyboard.instance = self
        self.keyboard_frame = ctk.CTkFrame(self.top, fg_color="transparent")
        self.keyboard_frame.place(relx=0.5, rely=0.5, anchor="center")
        self.create_keys()
        
    def create_keys(self):
        keys = [
            ['1','2','3','4','5','6','7','8','9','0','-'],
            ['q','w','e','r','t','y','u','i','o','p'],
            ['a','s','d','f','g','h','j','k','l'],
            ['z','x','c','v','b','n','m','Back'],
            ['Space']
        ]
        
        for r, row in enumerate(keys):
            for c, key in enumerate(row):
                if key == "Space":
                    btn = ctk.CTkButton(self.keyboard_frame, text="␣", width=400, command=lambda: self.insert_char(" "))
                    btn.grid(row=r, column=0, columnspan=10, pady=4)
                elif key == "Back":
                    btn = ctk.CTkButton(self.keyboard_frame, text="⌫", width=50, command=self.backspace)
                    btn.grid(row=r, column=c, padx=1, pady=4)
                else:
                    btn = ctk.CTkButton(self.keyboard_frame, text=key, width=50,
                                        command=lambda k=key: self.insert_char(k))
                    btn.grid(row=r, column=c, padx=2, pady=4)


    def insert_char(self, char):
        self.entry.insert("end", char)

    def backspace(self):
        current = self.entry.get()
        self.entry.delete(0, "end")
        self.entry.insert(0, current[:-1])

    def on_close(self):
        CTkOnScreenKeyboard.instance = None
        CTkOnScreenKeyboard.keyboard_closed_once = True  # prevent auto-reopen
        self.top.destroy()

def open_keyboard(root, entry, event):
    CTkOnScreenKeyboard.keyboard_closed_once = False
    CTkOnScreenKeyboard(root, entry)
def close():
    if CTkOnScreenKeyboard.instance:
        CTkOnScreenKeyboard.instance.on_close()