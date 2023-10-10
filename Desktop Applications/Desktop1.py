from tkinter import *
from tkinter import ttk

root = Tk()
root.minsize(300, 300)  
root.maxsize(300, 300)  

frame = ttk.Frame(root, padding=100)
frame.grid()


frame.columnconfigure(0, weight=1)
frame.columnconfigure(2, weight=1)

label = ttk.Label(frame, text="First WEB project task")
label.grid(column=1, row=0, pady=(0, 10))

button = ttk.Button(frame, text="Change picture")
button.grid(column=1, row=1, pady=10)
exit_button = ttk.Button(frame, text="Exit", command=root.destroy)
exit_button.grid(column=1, row=2, pady=(10, 0))

style = ttk.Style()
style.configure("TButton", foreground="blue", font=("Helvetica", 12))

root.mainloop()