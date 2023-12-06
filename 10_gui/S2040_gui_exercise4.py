""" Opgave "GUI step 4":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Bruge det, du har lært i GUI-eksempelfilerne, og byg den GUI, der er afbildet i images/gui_2040.png

Genbrug din kode fra "GUI step 3".

Fyld treeview'en med testdata.
Leg med farveværdierne. Find en farvekombination, som du kan lide.

Funktionalitet:
    Klik på knappen "clear entry boxes" sletter teksten i alle indtastningsfelter (entries).
    Hvis du klikker på en datarække i træoversigten, kopieres dataene i denne række til indtastningsfelterne.

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

def get_data():
    entry_id.delete(0, tk.END)
    entry_weight.delete(0, tk.END)
    entry_destination.delete(0, tk.END)

    selected = tree1.focus()
    values = tree1.item(selected, 'values')

    entry_id.insert(0, values[0])
    entry_weight.insert(0, values[1])
    entry_destination.insert(0, values[2])

def click_data(e):
    get_data()

# main window
window = tk.Tk()
window.title("my first GUI")
window.geometry("500x500")

# label frame
label_frame = tk.LabelFrame(window, text="Container")
label_frame.grid(padx=(5, 10), pady=(10, 15))

# frame for treeview
frame_tree = tk.Frame(label_frame)
frame_tree.grid(padx=(5, 10), pady=(10, 20))

rowheight = 24  # rowheight in treeview
treeview_background = "#ffa500"
treeview_foreground = "black"
treeview_selected = "#16537e"

# Configure treeview style and colors
style = ttk.Style()
style.theme_use('default')
style.configure("Treeview", background=treeview_background, foreground=treeview_foreground, rowheight=rowheight, fieldbackground=treeview_background)
style.map('Treeview', background=[('selected', treeview_selected)])

# treeview
tree_scrollbar = tk.Scrollbar(frame_tree)
tree_scrollbar.grid(row=0, column=1, sticky="ns")
tree1 = ttk.Treeview(frame_tree, columns= ("id", "weight", "destination"), yscrollcommand=tree_scrollbar.set, selectmode="browse")
tree1.grid(row=0, column=0, padx=0, pady=0, sticky=tk.N)
tree_scrollbar.config(command=tree1.yview)

# treeview columns
tree1.column('#0', width=0, stretch=tk.NO)
tree1.column('id', width=35, anchor=tk.E)
tree1.column('weight', width=75, anchor=tk.E)
tree1.column('destination', width=200, anchor=tk.W)

tree1.heading('#0', text="", anchor=tk.W)
tree1.heading("id", text="Id", anchor=tk.CENTER)
tree1.heading("weight", text="Weight", anchor=tk.CENTER)
tree1.heading('destination', text='Destination', anchor=tk.CENTER)



# frame for labels and entries
frame1 = tk.Frame(label_frame)
frame1.grid(padx=(0, 10), pady=(10, 15))

# labels
label_id = tk.Label(frame1, text="Id")
label_weight = tk.Label(frame1, text="Weight")
label_destination = tk.Label(frame1, text="Destination")
label_weather = tk.Label(frame1, text="Weather")

# labels get grid functionality
label_id.grid(column=0, row=0)
label_weight.grid(column=1, row=0)
label_destination.grid(column=2, row=0)
label_weather.grid(column=3, row=0)

# entries
entry_id = tk.Entry(frame1, width=4)
entry_weight = tk.Entry(frame1, width=7)
entry_destination = tk.Entry(frame1, width=20)
entry_weather = tk.Entry(frame1, width=12)

# entries get grid functionality
entry_id.grid(column=0, row=1, padx=8)
entry_weight.grid(column=1, row=1, padx=8)
entry_destination.grid(column=2, row=1, padx=8)
entry_weather.grid(column=3, row=1, padx=(8, 0))

# frame for buttons
frame2 = tk.Frame(label_frame)
frame2.grid(padx=(5, 10), pady=(0, 15))

# buttons
button_create = tk.Button(frame2, text="Create")
button_update = tk.Button(frame2, text="Update")
button_delete = tk.Button(frame2, text="Delete")
button_clear = tk.Button(frame2, text="Clear Entry Boxes", command=clear_entry)

# buttons get grid functionality
button_create.grid(column=0, row=0, padx=(20, 4))
button_update.grid(column=1, row=0, padx=(5, 5))
button_delete.grid(column=2, row=0, padx=(5, 5))
button_clear.grid(column=3, row=0, padx=(5, 20))


id_list = [1, 2, 3, 4]
weight_list = [1000, 2000, 3000, 4000]
destination_list = ['oslo', 'chicago', 'milano', 'amsterdam']

for x in range(len(id_list)):
    tree1.insert(parent='', index=x, values= (id_list[x], weight_list[x], destination_list[x]))


tree1.bind("<ButtonRelease-1>", click_data)

window.mainloop()