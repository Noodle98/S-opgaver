""" Opgave "GUI step 2":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2020.png

Genbrug din kode fra "GUI step 1".

GUI-strukturen bør være som følger:
    main window
        labelframe
            frame
                labels and entries
            frame
                buttons

Funktionalitet:
    Klik på knappen "clear entry boxes" sletter teksten i alle indtastningsfelter (entries).

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

import tkinter as tk
from tkinter import ttk


def clear_entry():
    entry_id.delete(0, tk.END)
    entry_weight.delete(0, tk.END)
    entry_destination.delete(0, tk.END)
    entry_weather.delete(0, tk.END)



window = tk.Tk()
window.title("my first GUI")
window.geometry("500x150")
label_frame = tk.LabelFrame(window, text="Container")
label_frame.grid(padx=(5, 10), pady=(10, 15))
frame1 = tk.Frame(label_frame)
frame1.grid(padx=(5, 10), pady=(10, 15))
frame2 = tk.Frame(label_frame)
frame2.grid(padx=(5, 10), pady=(0, 15))

label_id = tk.Label(frame1, text="Id")
label_weight = tk.Label(frame1, text="Weight")
label_destination = tk.Label(frame1, text="Destination")
label_weather = tk.Label(frame1, text="Weather")

label_id.grid(column=0, row=0)
label_weight.grid(column=1, row=0)
label_destination.grid(column=2, row=0)
label_weather.grid(column=3, row=0)

entry_id = tk.Entry(frame1, width=4)
entry_weight = tk.Entry(frame1, width=7)
entry_destination = tk.Entry(frame1, width=20)
entry_weather = tk.Entry(frame1, width=12)

entry_id.grid(column=0, row=1, padx=8)
entry_weight.grid(column=1, row=1, padx=8)
entry_destination.grid(column=2, row=1, padx=8)
entry_weather.grid(column=3, row=1, padx=8)

button_create = tk.Button(frame2, text="Create")
button_update = tk.Button(frame2, text="Update")
button_delete = tk.Button(frame2, text="Delete")
button_clear = tk.Button(frame2, text="Clear Entry Boxes", command=clear_entry)

button_create.grid(column=0, row=0, padx=(20, 4))
button_update.grid(column=1, row=0, padx=(5, 5))
button_delete.grid(column=2, row=0, padx=(5, 5))
button_clear.grid(column=3, row=0, padx=(5, 20))




window.mainloop()