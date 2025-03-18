import tkinter as tk

root = tk.Tk()
root.title ("Pop up Page")
root.attributes('-fullscreen', True)
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()

pop_up_page = tk.Frame(root, width=500, height=300, bg="dark blue")
pop_up_page.pack(fill="both", expand=True)

pop_up_label = tk.Label(pop_up_page, text="Welcome to NEURead!", fg="white", font=("Arial", 60, "bold"), bg="dark blue")
pop_up_label.place(relx=0.5, rely=0.45, anchor="center")

pop_up_label2 = tk.Label(pop_up_page, text="Please touch the screen to continue", fg="white", font=("Arial", 20, "bold"), bg="dark blue")
pop_up_label2.place(relx=0.5, rely=0.53, anchor="center")

root.mainloop()