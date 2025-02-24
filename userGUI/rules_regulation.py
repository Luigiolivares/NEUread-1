import tkinter as tk
from tkinter import ttk
# RULES PAGE------------------------------

# ROUNDED FRAME FUNCTION
def create_rounded_frame(parent, width, height, radius=20):
    round_canvas = tk.Canvas(parent, width=width, height=height, bd=0, highlightthickness=0)
    
    # ROUNDED FRAME CODE
    round_canvas.create_arc(
        (0, 0, radius * 2, radius * 2), start=90, extent=90, outline="", fill="white")  # top-left corner
    round_canvas.create_arc(
        (width - radius * 2, 0, width, radius * 2), start=0, extent=90, outline="", fill="white")  # top-right corner
    round_canvas.create_arc(
        (0, height - radius * 2, radius * 2, height), start=180, extent=90, outline="", fill="white")  # bottom-left corner
    round_canvas.create_arc(
        (width - radius * 2, height - radius * 2, width, height), start=270, extent=90, outline="", fill="white")  # bottom-right corner
    round_canvas.create_rectangle(
        radius, 0, width - radius, height, outline="", fill="white")  # top edge
    round_canvas.create_rectangle(
        0, radius, width, height - radius, outline="", fill="white")  # right edge
    # FRAME LABEL
    label1 = tk.Label(round_canvas, text='Library Policies & Regulations', font=('Arial', 30, 'bold'), fg="navy", bg='white')
    label1.place(x=(0.0058 * width), y=(0.0058 * height))  # Top-left corner
    
    return round_canvas
    
def Main_rules_page(content, x_size, y_size):
    rules_page = tk.Frame(content)
    rules_page.place(x=0, y=0, width=x_size, height=y_size)
    label1 = tk.Label(rules_page, text='New Era University', font=('Arial', 25, 'bold'))
    label1.place(x=1050, y=50)
    # ROUNDED FRAME VARIABLE
    round_canvas = create_rounded_frame(rules_page, (0.76 * x_size), (0.56 * y_size))  # Increased width and height
    round_canvas.place(x=(0.05 * x_size), y=(0.12 * y_size))

    # POLICIES TEXT
    policies_text = """  • No school ID. No proper uniform, No Entry policy is implemented.
    • All library users are required to register by tapping validated school ID on the RFID reader or register on the statistics form upon entering the library premises.
    • Bags and other belongings are to be deposited at the Bag Counter of the library units or sections where an open-shelf system is adopted.
    • Library users should not leave any valuables at the bag counter. The library will not be held responsible for the loss of belongings.
    • Present validated school ID and Library Card in borrowing library materials.
    • Borrowing of library material/s should be done personally.
    • Library card is non-transferrable. Anybody caught using another's Library Card shall be reported to the Office of Student Discipline (5) for disciplinary action.
    • Photocopying and taking digital snapshots of theses, research works, and narrative reports are strictly prohibited.
    • No books or other library materials can be borrowed for overnight use a week prior to final examinations."""
    
    # Text Widget without border
    text_widget = tk.Text(round_canvas, wrap=tk.WORD, height=16, width=80, font=("Arial", 20, "bold"), bg='white', spacing1=15, bd=0, highlightthickness=0)  # No border
    text_widget.insert(tk.END, policies_text)
    text_widget.config(state=tk.DISABLED)  # Make text widget read-only
    text_widget.place(x=20, y=60)  # Adjust placement inside canvas
    
    rules_page.tkraise()

#BORROW RULES
#FINES
#OFFENSES
#LOST BOOK
#DECORUM