import tkinter as tk
from userGUI.mainGUI import start_neuread_app
# Create the main application window
root = tk.Tk()
root.title("Idle Page")
root.attributes('-fullscreen', True)

window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight() 

active = False
rfid_data = ""
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
    """Handles RFID input and transitions to the main app."""
    print("key pressed")
    global active
    global rfid_data
    if not active:
        active = True
        start_neuread_app(75240, root, return_to_idle)
        idle_frame.destroy()

# Initialize the idle page at startup
create_idle_page()

# Run the application
root.mainloop()