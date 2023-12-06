"""
Opgave "GUI step 1":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2010.png

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

import tkinter as tk
from tkinter import ttk


class Main_window(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_title("my first GUI")
        my_frame = tk.Frame(self, bd=1, relief="solid")
        button1 = tk.Button(my_frame, text="Create")
        my_frame.grid()
        button1.pack()


window = tk.Tk()
window.title("my first GUI")
window.geometry("150x200")
label_frame = tk.LabelFrame(window, text="Container")
# frame.pack(fill="both", expand=True)
label_frame.grid(padx=(5, 10), pady=(10, 15))

frame = tk.Frame(label_frame)
frame.grid(padx=15, pady=8)
label_id = tk.Label(frame, text="Id")
entry1 = tk.Entry(frame, width=5)
button_create = tk.Button(frame, text="Create")

# tree1 = tk.ttk.Treeview(window)
# tree1.grid(row=0, column=0, columnspan=3, sticky="nsew")

label_id.grid(padx=(30, 30), pady=(15, 5))
entry1.grid(pady=(2, 5))
button_create.grid(pady=(5, 5))

# label_id.pack()
# entry1.pack()
# button_create.pack()

window.mainloop()
