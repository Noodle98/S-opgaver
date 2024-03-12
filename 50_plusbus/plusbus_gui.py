import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import plusbus_data as pbd
import plusbus_sql as pbsql
import plusbus_func as pbf
from datetime import date


# region common functions
def read_table(tree, class_):  # fill tree from database
    count = 0  # Used to keep track of odd and even rows, because these will be colored differently.
    result = pbsql.select_all(class_)  # Read all containers from database
    for record in result:
        if record.valid():  # this condition excludes soft deleted records from being shown in the data table
            if count % 2 == 0:  # even
                tree.insert(parent='', index='end', iid=str(count), text='', values=record.convert_to_tuple(), tags=('evenrow',))  # Insert one row into the data table
            else:  # odd
                tree.insert(parent='', index='end', iid=str(count), text='', values=record.convert_to_tuple(), tags=('oddrow',))  # Insert one row into the data table
            count += 1

def empty_treeview(tree):  # Clear treeview table
    tree.delete(*tree.get_children())

def refresh_treeview(tree, class_):  # Refresh treeview table
    empty_treeview(tree)  # Clear treeview table
    read_table(tree, class_)

# endregion common functions


# region kunder functions
def clear_kunder_entries():
    entry_kunder_id.delete(0, tk.END)
    entry_kunder_efternavn.delete(0, tk.END)
    entry_kunder_kontakt.delete(0, tk.END)


def get_data_to_entries_kunder():
    entry_kunder_id.delete(0, tk.END)
    entry_kunder_efternavn.delete(0, tk.END)
    entry_kunder_kontakt.delete(0, tk.END)

    selected = tree_kunder.focus()
    values = tree_kunder.item(selected, 'values')

    entry_kunder_id.insert(0, values[0])
    entry_kunder_efternavn.insert(0, values[1])
    entry_kunder_kontakt.insert(0, values[2])


def click_data_kunder(e):
    get_data_to_entries_kunder()

def read_kunder_entries():  # read content of entry boxes
    return entry_kunder_id.get(), entry_kunder_efternavn.get(), entry_kunder_kontakt.get()


def create_kunder(tree, record):  # add new tuple to database
    kunder = pbd.Kunder.convert_from_tuple(record)  # convert tuple to Kunder
    pbsql.create_record(kunder)  # update database
    clear_kunder_entries()  # clear entry boxes
    refresh_treeview(tree, pbd.Kunder)  # refresh treeview table


def update_kunder(tree, record):  # update tuple in database
    kunder = pbd.Kunder.convert_from_tuple(record)  # convert tuple to Kunder
    pbsql.update_kunder(kunder)  # update database
    clear_kunder_entries()  # clear entry boxes
    refresh_treeview(tree, pbd.Kunder)  # refresh treeview table


def delete_kunder(tree, record):  # delete tuple in database
    kunder = pbd.Kunder.convert_from_tuple(record)   # convert tuple to Kunder
    pbsql.delete_soft_kunder(kunder)  # update database
    clear_kunder_entries()  # clear entry boxes
    refresh_treeview(tree, pbd.Kunder)  # refresh treeview table

# endregion kunder functions

# region rejser functions
def clear_rejser_entries():
    entry_rejser_id.delete(0, tk.END)
    entry_rejser_rute.delete(0, tk.END)
    entry_rejser_dato.delete(0, tk.END)
    entry_rejser_pladskapacitet.delete(0, tk.END)


def get_data_to_entries_rejser():
    entry_kunder_id.delete(0, tk.END)
    entry_rejser_rute.delete(0, tk.END)
    entry_rejser_dato.delete(0, tk.END)
    entry_rejser_pladskapacitet.delete(0, tk.END)

    selected = tree_rejser.focus()
    values = tree_rejser.item(selected, 'values')

    entry_rejser_id.insert(0, values[0])
    entry_rejser_rute.insert(0, values[1])
    entry_rejser_dato.insert(0, values[2])
    entry_rejser_pladskapacitet.insert(0, values[3])


def click_data_rejser(e):
    get_data_to_entries_rejser()

def read_rejser_entries():  # read content of entry boxes
    splitted_date = entry_rejser_dato.get().split('-')
    new_date = date(day=int(splitted_date[2]), month=int(splitted_date[1]), year=int(splitted_date[0]))

    return entry_rejser_id.get(), entry_rejser_rute.get(), new_date, entry_rejser_pladskapacitet.get()


def create_rejser(tree, record):  # add new tuple to database
    rejser = pbd.Rejser.convert_from_tuple(record)  # convert tuple to Rejser
    pbsql.create_record(rejser)  # update database
    clear_rejser_entries()  # clear entry boxes
    refresh_treeview(tree, pbd.Rejser)  # refresh treeview table


def update_rejser(tree, record):  # update tuple in database
    rejser = pbd.Rejser.convert_from_tuple(record)  # convert tuple to Rejser
    pbsql.update_rejser(rejser)  # update database
    clear_rejser_entries()  # clear entry boxes
    refresh_treeview(tree, pbd.Rejser)  # refresh treeview table


def delete_rejser(tree, record):  # delete tuple in database
    rejser = pbd.Rejser.convert_from_tuple(record)   # convert tuple to Rejser
    pbsql.delete_soft_rejser(rejser)  # update database
    clear_rejser_entries()  # clear entry boxes
    refresh_treeview(tree, pbd.Rejser)  # refresh treeview table


# endregion rejser functions

# region bookinger functions
def clear_bookinger_entries():
    entry_bookinger_id.delete(0, tk.END)
    entry_bookinger_kunde_id.delete(0, tk.END)
    entry_bookinger_rejse_id.delete(0, tk.END)
    entry_bookinger_pladser.delete(0, tk.END)


def get_data_to_entries_bookinger():
    entry_bookinger_id.delete(0, tk.END)
    entry_bookinger_kunde_id.delete(0, tk.END)
    entry_bookinger_rejse_id.delete(0, tk.END)
    entry_bookinger_pladser.delete(0, tk.END)

    selected = tree_bookinger.focus()
    values = tree_bookinger.item(selected, 'values')

    entry_bookinger_id.insert(0, values[0])
    entry_bookinger_kunde_id.insert(0, values[1])
    entry_bookinger_rejse_id.insert(0, values[2])
    entry_bookinger_pladser.insert(0, values[3])


def click_data_bookinger(e):
    get_data_to_entries_bookinger()

def read_bookinger_entries():  # read content of entry boxes
    return entry_bookinger_id.get(), entry_bookinger_kunde_id.get(), entry_bookinger_rejse_id.get(), entry_bookinger_pladser.get()


def create_bookinger(tree, record):  # add new tuple to database
    bookinger = pbd.Bookinger.convert_from_tuple(record)  # convert tuple to Bookinger
    pladser_ok = pbf.capacity_available(pbsql.get_record(pbd.Rejser, bookinger.rejse_id), bookinger)
    if pladser_ok:
        pbsql.create_record(bookinger)  # update database
        clear_bookinger_entries()  # clear entry boxes
        refresh_treeview(tree, pbd.Bookinger)  # refresh treeview table
    else:
        messagebox.showwarning("", "Not enough available pladser on rejse!")


def update_bookinger(tree, record):  # update tuple in database
    bookinger = pbd.Bookinger.convert_from_tuple(record)  # convert tuple to Bookinger
    pbsql.update_bookinger(bookinger)  # update database
    clear_bookinger_entries()  # clear entry boxes
    refresh_treeview(tree, pbd.Bookinger)  # refresh treeview table


def delete_bookinger(tree, record):  # delete tuple in database
    bookinger = pbd.Bookinger.convert_from_tuple(record)   # convert tuple to Bookinger
    pbsql.delete_soft_bookinger(bookinger)  # update database
    clear_bookinger_entries()  # clear entry boxes
    refresh_treeview(tree, pbd.Bookinger)  # refresh treeview table

# endregion bookinger functions



# main window
main_window = tk.Tk()
main_window.title("Plusbus GUI")
main_window.geometry("1500x500")

rowheight = 24 #rowheight in treeview
treeview_background = "#eeeeee"
treeview_foreground = "black"
treeview_selected = "#206030"



oddrow = "#dddddd"
evenrow = "#cccccc"

# Configure treeview style and colors
style = ttk.Style()
style.theme_use('default')
style.configure("Treeview", background=treeview_background, foreground=treeview_foreground, rowheight=rowheight, fieldbackground=treeview_background)
style.map('Treeview', background=[('selected', treeview_selected)])

# ----------- region Kunder -----------

# label frame
label_frame_kunder = tk.LabelFrame(main_window, text="Kunder")
label_frame_kunder.grid(padx=(5, 10), pady=(10, 15), row=0, column=0)

# frame for treeview
frame_tree_kunder = tk.Frame(label_frame_kunder)
frame_tree_kunder.grid(padx=(5, 10), pady=(10, 20))

# treeview
tree_scrollbar_kunder = tk.Scrollbar(frame_tree_kunder)
tree_scrollbar_kunder.grid(row=0, column=1, sticky="ns")
tree_kunder = ttk.Treeview(frame_tree_kunder, columns=("id", "efternavn", "kontakt"), yscrollcommand=tree_scrollbar_kunder.set, selectmode="browse")
tree_kunder.grid(row=0, column=0, padx=0, pady=0, sticky=tk.N)
tree_scrollbar_kunder.config(command=tree_kunder.yview)

#treeview columns
tree_kunder.column('#0', width=0, stretch=tk.NO)
tree_kunder.column("id", width=35, anchor=tk.E)
tree_kunder.column("efternavn", width=150, anchor=tk.E)
tree_kunder.column("kontakt", width=200, anchor=tk.E)

tree_kunder.heading('#0', text="", anchor=tk.W)
tree_kunder.heading("id", text="Id", anchor=tk.CENTER)
tree_kunder.heading("efternavn", text="Efternavn", anchor=tk.CENTER)
tree_kunder.heading("kontakt", text="Kontakt", anchor=tk.CENTER)

# frame for labels and enries
frame1_kunder = tk.Frame(label_frame_kunder)
frame1_kunder.grid(padx=(0, 10), pady=(10, 15))

# labels
label_kunder_id = tk.Label(frame1_kunder, text="Id")
label_kunder_efternavn = tk.Label(frame1_kunder, text="Efternavn")
label_kunder_kontakt = tk.Label(frame1_kunder, text="Kontakt")

# labels get grid functionality
label_kunder_id.grid(column=0, row=0)
label_kunder_efternavn.grid(column=1, row=0)
label_kunder_kontakt.grid(column=2, row=0)

# entries
entry_kunder_id = tk.Entry(frame1_kunder, width=4)
entry_kunder_efternavn = tk.Entry(frame1_kunder, width=20)
entry_kunder_kontakt = tk.Entry(frame1_kunder, width=20)

# entries get grid functionality
entry_kunder_id.grid(column=0, row=1, padx=8)
entry_kunder_efternavn.grid(column=1, row=1, padx=8)
entry_kunder_kontakt.grid(column=2, row=1, padx=8)

# frame for buttons
frame2_kunder = tk.Frame(label_frame_kunder)
frame2_kunder.grid(padx=(5, 10), pady=(0, 15))


# buttons
button_kunder_create = tk.Button(frame2_kunder, text="Create", command=lambda:create_kunder(tree_kunder, read_kunder_entries()))
button_kunder_update = tk.Button(frame2_kunder, text="Update", command=lambda:update_kunder(tree_kunder, read_kunder_entries()))
button_kunder_delete = tk.Button(frame2_kunder, text="Delete", command=lambda:delete_kunder(tree_kunder, read_kunder_entries()))
button_kunder_clear = tk.Button(frame2_kunder, text="Clear Entry Boxes", command=lambda:clear_kunder_entries())

# buttons get grid functionality
button_kunder_create.grid(column=0, row=0, padx=(20, 4))
button_kunder_update.grid(column=1, row=0, padx=(5, 5))
button_kunder_delete.grid(column=2, row=0, padx=(5, 5))
button_kunder_clear.grid(column=3, row=0, padx=(5, 20))


# ----------- endregion Kunder -----------

# ----------- region Rejser ------------


# label frame
label_frame_rejser = tk.LabelFrame(main_window, text="Rejser")
label_frame_rejser.grid(padx=(5, 10), pady=(10, 15), row=0, column=1)

# frame for treeview
frame_tree_rejser = tk.Frame(label_frame_rejser)
frame_tree_rejser.grid(padx=(5, 10), pady=(10, 20))

# treeview
tree_scrollbar_rejser = tk.Scrollbar(frame_tree_rejser)
tree_scrollbar_rejser.grid(row=0, column=1, sticky="ns")
tree_rejser = ttk.Treeview(frame_tree_rejser, columns=("id", "rute", "dato", "pladskapacitet"), yscrollcommand=tree_scrollbar_rejser.set, selectmode="browse")
tree_rejser.grid(row=0, column=0, padx=0, pady=0, sticky=tk.N)
tree_scrollbar_rejser.config(command=tree_rejser.yview)

# treeview columns
tree_rejser.column('#0', width=0, stretch=tk.NO)
tree_rejser.column('id', width=35, anchor=tk.E)
tree_rejser.column('rute', width=150, anchor=tk.E)
tree_rejser.column('dato', width=100, anchor=tk.E)
tree_rejser.column('pladskapacitet', width=100, anchor=tk.E)

tree_rejser.heading('#0', text="", anchor=tk.W)
tree_rejser.heading('id', text="Id", anchor=tk.CENTER)
tree_rejser.heading("rute", text="Rute", anchor=tk.CENTER)
tree_rejser.heading("dato", text="Dato", anchor=tk.CENTER)
tree_rejser.heading("pladskapacitet", text="Pladskapacitet", anchor=tk.CENTER)

# frame for labels and entries
frame1_rejser = tk.Frame(label_frame_rejser)
frame1_rejser.grid(padx=(0, 10), pady=(10, 15))

# labels
label_rejser_id = tk.Label(frame1_rejser, text="Id")
label_rejser_rute = tk.Label(frame1_rejser, text="Rute")
label_rejser_dato = tk.Label(frame1_rejser, text="Dato")
label_rejser_pladskapacitet = tk.Label(frame1_rejser, text="Pladskapacitet")

# labels get grid functionality
label_rejser_id.grid(column=0, row=0)
label_rejser_rute.grid(column=1, row=0)
label_rejser_dato.grid(column=2, row=0)
label_rejser_pladskapacitet.grid(column=3, row=0)

# entries
entry_rejser_id = tk.Entry(frame1_rejser, width=4)
entry_rejser_rute = tk.Entry(frame1_rejser, width=30)
entry_rejser_dato = tk.Entry(frame1_rejser, width=10)
entry_rejser_pladskapacitet = tk.Entry(frame1_rejser, width=4)

# entries get grid functionality
entry_rejser_id.grid(column=0, row=1, padx=8)
entry_rejser_rute.grid(column=1, row=1, padx=8)
entry_rejser_dato.grid(column=2, row=1, padx=8)
entry_rejser_pladskapacitet.grid(column=3, row=1, padx=8)

# frame for buttons
frame2_rejser = tk.Frame(label_frame_rejser)
frame2_rejser.grid(padx=(5, 10), pady=(0, 15))

# buttons
button_rejser_create = tk.Button(frame2_rejser, text="Create", command=lambda: create_rejser(tree_rejser, read_rejser_entries()))
button_rejser_update = tk.Button(frame2_rejser, text="Update", command=lambda: update_rejser(tree_rejser, read_rejser_entries()))
button_rejser_delete = tk.Button(frame2_rejser, text="Delete", command=lambda: delete_rejser(tree_rejser, read_rejser_entries()))
button_rejser_clear = tk.Button(frame2_rejser, text="Clear Entry Boxes", command=lambda: clear_rejser_entries())

# buttons get grid functionality
button_rejser_create.grid(column=0, row=0, padx=(20, 4))
button_rejser_update.grid(column=1, row=0, padx=(5, 5))
button_rejser_delete.grid(column=2, row=0, padx=(5, 5))
button_rejser_clear.grid(column=3, row=0, padx=(5, 20))


# ----------- endregion Rejser -----------

# ----------- region Bookinger -----------

# label frame
label_frame_bookinger = tk.LabelFrame(main_window, text="Bookinger")
label_frame_bookinger.grid(padx=(5, 10), pady=(10, 15), row=0, column=2)

# frame for treeview
frame_tree_bookinger = tk.Frame(label_frame_bookinger)
frame_tree_bookinger.grid(padx=(5, 10), pady=(10, 20))

# treeview
tree_scrollbar_bookinger = tk.Scrollbar(frame_tree_bookinger)
tree_scrollbar_bookinger.grid(row=0, column=1, sticky="ns")
tree_bookinger = ttk.Treeview(frame_tree_bookinger, columns=("id", "kunde_id", "rejse_id", "pladser"), yscrollcommand=tree_scrollbar_bookinger.set, selectmode="browse")
tree_bookinger.grid(row=0, column=0, padx=0, pady=0, sticky=tk.N)
tree_scrollbar_bookinger.config(command=tree_bookinger.yview)

# treeview columns
tree_bookinger.column("#0", width=0, stretch=tk.NO)
tree_bookinger.column("id", width=35, anchor=tk.E)
tree_bookinger.column("kunde_id", width=70, anchor=tk.E)
tree_bookinger.column("rejse_id", width=70, anchor=tk.E)
tree_bookinger.column("pladser", width=70, anchor=tk.E)

tree_bookinger.heading("#0", text="", anchor=tk.W)
tree_bookinger.heading("id", text="Id", anchor=tk.CENTER)
tree_bookinger.heading("kunde_id", text="Kunde Id", anchor=tk.CENTER)
tree_bookinger.heading("rejse_id", text="Rejse Id", anchor=tk.CENTER)
tree_bookinger.heading("pladser", text="Pladser", anchor=tk.CENTER)

# frame fro labels and entries
frame1_bookinger = tk.Frame(label_frame_bookinger)
frame1_bookinger.grid(padx=(0, 10), pady=(10, 15))

# labels
label_bookinger_id = tk.Label(frame1_bookinger, text="Id")
label_bookinger_kunde_id = tk.Label(frame1_bookinger, text="Kunde Id")
label_bookinger_rejse_id = tk.Label(frame1_bookinger, text="Rejse Id")
label_bookinger_pladser = tk.Label(frame1_bookinger, text="Pladser")

#labels get grid functionality
label_bookinger_id.grid(column=0, row=0)
label_bookinger_kunde_id.grid(column=1, row=0)
label_bookinger_rejse_id.grid(column=2, row=0)
label_bookinger_pladser.grid(column=3, row=0)

# entries
entry_bookinger_id = tk.Entry(frame1_bookinger, width=4)
entry_bookinger_kunde_id = tk.Entry(frame1_bookinger, width=4)
entry_bookinger_rejse_id = tk.Entry(frame1_bookinger, width=4)
entry_bookinger_pladser = tk.Entry(frame1_bookinger, width=4)

# entries get grid functionality
entry_bookinger_id.grid(column=0, row=1, padx=8)
entry_bookinger_kunde_id.grid(column=1, row=1, padx=8)
entry_bookinger_rejse_id.grid(column=2, row=1, padx=8)
entry_bookinger_pladser.grid(column=3, row=1, padx=(8, 0))

# frame for buttons
frame2_bookinger = tk.Frame(label_frame_bookinger)
frame2_bookinger.grid(padx=(5, 10), pady=(0, 15))

# buttons
button_bookinger_create = tk.Button(frame2_bookinger, text="Create", command=lambda: create_bookinger(tree_bookinger, read_bookinger_entries()))
button_bookinger_update = tk.Button(frame2_bookinger, text="Update", command=lambda: update_bookinger(tree_bookinger, read_bookinger_entries()))
button_bookinger_delete = tk.Button(frame2_bookinger, text="Delete", command=lambda: delete_bookinger(tree_bookinger, read_bookinger_entries()))
button_bookinger_clear = tk.Button(frame2_bookinger, text="Clear Entry Boxes", command=lambda: clear_bookinger_entries())

# buttons get grid functionality
button_bookinger_create.grid(column=0, row=0, padx=(20, 4))
button_bookinger_update.grid(column=1, row=0, padx=(5, 5))
button_bookinger_delete.grid(column=2, row=0, padx=(5, 5))
button_bookinger_clear.grid(column=3, row=0, padx=(5, 20))


# ----------- endregion Bookinger -----------


tree_kunder.bind("<ButtonRelease-1>", click_data_kunder)
tree_rejser.bind("<ButtonRelease-1>", click_data_rejser)
tree_bookinger.bind("<ButtonRelease-1>", click_data_bookinger)
if __name__ == "__main__":  # Executed when invoked directly. We use this so main_window.mainloop() does not keep our unit tests from running.
    refresh_treeview(tree_kunder, pbd.Kunder)  # Load data from database
    refresh_treeview(tree_rejser, pbd.Rejser)
    refresh_treeview(tree_bookinger, pbd.Bookinger)
    main_window.mainloop()