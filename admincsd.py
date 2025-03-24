import tkinter as tk

root = tk.Tk()
root.title ("Data Send")
root.attributes('-fullscreen', True)
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()

Data_Send_page = tk.Frame(root, width=500, height=300, bg="green")
Data_Send_page.pack(fill="both", expand=True)

Data_Send_label = tk.Label(Data_Send_page, text='The data has been successfully emailed to CSD.' , fg="white", font=("Arial", 60, "bold"), 
                        bg="green", wraplength=1000)
Data_Send_label.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()