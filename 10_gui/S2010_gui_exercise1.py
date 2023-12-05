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
frame = tk.Frame(window, borderwidth=1, border=10)
frame.pack(fill="both", expand=True)

label_id = tk.Label(frame, text="Id")
entry1 = tk.Entry(frame, width=5)
button_create = tk.Button(frame, text="Create")

label_id.grid()
entry1.grid()
button_create.grid()


window.mainloop()
