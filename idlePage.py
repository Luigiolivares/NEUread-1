import tkinter as tk
from userGUI.mainGUI import start_neuread_app
from userGUI.adminPanel import admin
import time
from bnd import *
# Create the main application window
root = tk.Tk()
root.title("Idle Page")
root.attributes('-fullscreen', True)
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight() 
last_scan_time = 0
active = False
rfid_data = "0011158817"
def create_idle_page():
    """Creates the idle page UI."""
    global idle_frame
    idle_frame = tk.Frame(root, width=500, height=300, bg="lightgray")
    idle_frame.pack(fill="both", expand=True)

    idle_label = tk.Label(idle_frame, text="Waiting...", font=("Arial", 18, "bold"), bg="lightgray")
    idle_label.place(relx=0.5, rely=0.5, anchor="center")  # Center the label

    # Bind key events to capture RFID input
    root.bind("<Key>", on_key_press)

def return_to_idle():
    global active
    """Returns the user to the idle page by clearing the screen and recreating the idle frame."""
    for widget in root.winfo_children():
        widget.destroy()
    active = False
    create_idle_page()

def on_key_press(event):
    global active
    global rfid_data
    global idle_frame
    if active:
        return
    if event.keysym == "Return":
        print("pressing")
        if rfid_data:
            if getUserInfo(rfid_data) != ([], [], []):
                try:
                    if getUserInfo(rfid_data)[0][0][2] == "Admin":
                        root.unbind("<Key>")
                        rfid_data = ""  # Reset buffer
                        admin(root, return_to_idle)
                    else:
                        active = True
                        print(f"RFID Scanned: {rfid_data}")
                        root.unbind("<Key>")
                        start_neuread_app(rfid_data, root, return_to_idle)
                        print(rfid_data)
                        rfid_data = ""  # Reset buffer
                        idle_frame.destroy()
                except Exception as e:
                    rfid_data = ""
                    return None
            else:
                rfid_data = ""
                print("no user as such")
    else:
        rfid_data += event.char
        print(rfid_data)

# Initialize the idle page at startup
create_idle_page()

# Run the application
root.mainloop()