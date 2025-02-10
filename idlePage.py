import tkinter as tk
from mainGUI import *

# Create the main application window
root = tk.Tk()
root.title("Idle Page")
root.attributes('-fullscreen', True)
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()

active= False
# Create a frame to hold the idle page content
idle_frame = tk.Frame(root, width=500, height=300, bg="lightgray")
idle_frame.pack(fill="both", expand=True)

# Display an idle message
idle_label = tk.Label(idle_frame, text="Waiting...", font=("Arial", 18, "bold"), bg="lightgray")
idle_label.place(relx=0.5, rely=0.5, anchor="center")  # Center the label

#RFID scanned
rfid_data = ""

def on_key_press(event):
    global active
    global rfid_data
    if not active:
        active = True
        start_neuread_app(75240, root)
        idle_frame.destroy()
# Bind key events to capture RFID input
root.bind("<Key>", on_key_press)
# Run the application
root.mainloop()

#    if event.keysym == "Return":  # RFID scanners usually send data followed by "Enter"
#       print(rfid_data)
#        start_neuread_app(rfid_data, root) # Call your main function with RFID data
#        idle_frame.destroy()
#        rfid_data = ""  # Reset for the next scan
#    else:
#        rfid_data += event.char  # Capture the RFID input
