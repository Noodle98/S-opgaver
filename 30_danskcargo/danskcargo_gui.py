import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import danskcargo_data as dcd
import danskcargo_sql as dcsql
import danskcargo_func as dcf


# region container functions
def clear_container_entries():
    entry_id_container.delete(0, tk.END)
    entry_weight_container.delete(0, tk.END)
    entry_destination_container.delete(0, tk.END)
    entry_weather_container.delete(0, tk.END)


def get_data_to_entries_container():
    entry_id_container.delete(0, tk.END)
    entry_weight_container.delete(0, tk.END)
    entry_destination_container.delete(0, tk.END)

    selected = tree_container.focus()
    values = tree_container.item(selected, 'values')

    entry_id_container.insert(0, values[0])
    entry_weight_container.insert(0, values[1])
    entry_destination_container.insert(0, values[2])


def click_data(e):
    get_data_to_entries()


def read_container_entries():  # Read content of entry boxes
    return entry_id_container.get(), entry_weight_container.get(), entry_destination_container.get()


def create_container(tree, record):  # add new tuple to database
    container = dcd.Container.convert_from_tuple(record)  # Convert tuple to Container
    dcsql.create_record(container)  # Update database
    clear_container_entries()  # Clear entry boxes
    refresh_treeview(tree, dcd.Container)  # Refresh treeview table


def update_container(tree, record):  # update tuple in database
    container = dcd.Container.convert_from_tuple(record)  # Convert tuple to Container
    dcsql.update_container(container)  # Update database
    clear_container_entries()  # Clear entry boxes
    refresh_treeview(tree, dcd.Container)  # Refresh treeview table


def delete_container(tree, record):  # delete tuple in database
    container = dcd.Container.convert_from_tuple(record)  # Convert tuple to Container
    dcsql.delete_soft_container(container)  # Update database
    clear_container_entries()  # Clear entry boxes
    refresh_treeview(tree, dcd.Container)  # Refresh treeview table

# endregion container functions


# region aircraft functions
def clear_aircraft_entries():
    entry_id_aircraft.delete(0, tk.END)
    entry_max_cargo_weight_aircraft.delete(0, tk.END)
    entry_registration_aircraft.delete(0, tk.END)


def get_data_to_entries_aircraft():
    entry_id_aircraft.delete(0, tk.END)
    entry_max_cargo_weight_aircraft.delete(0, tk.END)
    entry_registration_aircraft.delete(0, tk.END)

    selected = tree_aircraft.focus()
    values = tree_aircraft.item(selected, 'values')

    entry_id_aircraft.insert(0, values[0])
    entry_max_cargo_weight_aircraft.insert(0, values[1])
    entry_registration_aircraft.insert(0, values[2])


def click_data_aircraft(e):
    get_data_to_entries_aircraft()

def read_aircraft_entries():  # Read content of entry boxes
    return entry_id_container.get(), entry_weight_container.get(), entry_destination_container.get()


def create_aircraft(tree, record):  # add new tuple to database
    container = dcd.Container.convert_from_tuple(record)  # Convert tuple to Container
    dcsql.create_record(container)  # Update database
    clear_container_entries()  # Clear entry boxes
    refresh_treeview(tree, dcd.Container)  # Refresh treeview table


def update_aircraft(tree, record):  # update tuple in database
    container = dcd.Container.convert_from_tuple(record)  # Convert tuple to Container
    dcsql.update_container(container)  # Update database
    clear_container_entries()  # Clear entry boxes
    refresh_treeview(tree, dcd.Container)  # Refresh treeview table


def delete_aircraft(tree, record):  # delete tuple in database
    container = dcd.Container.convert_from_tuple(record)  # Convert tuple to Container
    dcsql.delete_soft_container(container)  # Update database
    clear_container_entries()  # Clear entry boxes
    refresh_treeview(tree, dcd.Container)  # Refresh treeview table

# endregion aircraft functions


# region transport functions
def clear_transport_entries():
    entry_id_transport.delete(0, tk.END)
    entry_date_transport.delete(0, tk.END)
    entry_container_id_transport.delete(0, tk.END)
    entry_aircraft_id_transport.delete(0, tk.END)


def get_data_to_entries_transport():
    entry_id_transport.delete(0, tk.END)
    entry_date_transport.delete(0, tk.END)
    entry_container_id_transport.delete(0, tk.END)
    entry_aircraft_id_transport.delete(0, tk.END)

    selected = tree_transport.focus()
    values = tree_transport.item(selected, 'values')

    entry_id_transport.insert(0, values[0])
    entry_date_transport.insert(0, values[1])
    entry_container_id_transport.insert(0, values[2])
    entry_aircraft_id_transport.insert(0, values[3])


def click_data_transport(e):
    get_data_to_entries_transport()


def read_transport_entries():  # Read content of entry boxes
    return entry_id_container.get(), entry_weight_container.get(), entry_destination_container.get()


def create_transport(tree, record):  # add new tuple to database
    transport = dcd.Transport.convert_from_tuple(record)  # Convert tuple to Transport
    capacity_ok = dcf.capacity_available(dcsql.get_record(dcd.Aircraft, transport.aircraft_id), transport.date, dcsql.get_record(dcd.Container, transport.container_id))
    destination_ok = dcf.max_one_destination(dcsql.get_record(dcd.Aircraft, transport.aircraft_id), transport.date, dcsql.get_record(dcd.Container, transport.container_id))
    if destination_ok:
        if capacity_ok:
            dcsql.create_record(transport)  # Update database
            clear_transport_entries()  # Clear entry boxes
            refresh_treeview(tree, dcd.Transport)  # Refresh treeview table
        else:
            messagebox.showwarning("", "Not enough capacity on aircraft!")
    else:
        messagebox.showwarning("", "Aircraft already has another destination!")


def update_transport(tree, record):  # add new tuple to database
    transport = dcd.Transport.convert_from_tuple(record)  # Convert tuple to Transport
    capacity_ok = dcf.capacity_available(dcsql.get_record(dcd.Aircraft, transport.aircraft_id), transport.date, dcsql.get_record(dcd.Container, transport.container_id))
    destination_ok = dcf.max_one_destination(dcsql.get_record(dcd.Aircraft, transport.aircraft_id), transport.date, dcsql.get_record(dcd.Container, transport.container_id))
    if destination_ok:
        if capacity_ok:
            dcsql.get_record(transport, transport.id) # Update database
            dcsql.update_transport(transport) # Update database
            clear_transport_entries()  # Clear entry boxes
            refresh_treeview(tree, dcd.Transport)  # Refresh treeview table
        else:
            messagebox.showwarning("", "Not enough capacity on aircraft!")
    else:
        messagebox.showwarning("", "Aircraft already has another destination!")


def delete_transport(tree, record):  # delete tuple in database
    container = dcd.Container.convert_from_tuple(record)  # Convert tuple to Container
    dcsql.delete_soft_container(container)  # Update database
    clear_container_entries()  # Clear entry boxes
    refresh_treeview(tree, dcd.Container)  # Refresh treeview table

# endregion transport functions


# common functions
def read_table(tree, class_):  # fill tree from database
    count = 0  # Used to keep track of odd and even rows, because these will be colored differently.
    result = dcsql.select_all(class_)  # Read all containers from database
    for record in result:
        if record.valid():  # this condition excludes soft deleted records from being shown in the data table
            if count % 2 == 0:  # even
                tree.insert(parent='', index='end', iid=str(count), text='', values=record.convert_to_tuple(), tags=('evenrow',))  # Insert one row into the data table
            else:  # odd
                tree.insert(parent='', index='end', iid=str(count), text='', values=record.convert_to_tuple(), tags=('oddrow',))  # Insert one row into the data table
            count += 1


# region common functions
def empty_treeview(tree):  # Clear treeview table
    tree.delete(*tree.get_children())


def refresh_treeview(tree, class_):  # Refresh treeview table
    empty_treeview(tree)  # Clear treeview table
    read_table(tree, class_)  # Fill treeview from database


# endregion common functions


# main window
main_window = tk.Tk()
main_window.title("my first GUI")
main_window.geometry("1200x500")

rowheight = 24  # rowheight in treeview
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

# ----------- region Container ------------


# label frame
label_frame_container = tk.LabelFrame(main_window, text="Container")
label_frame_container.grid(padx=(5, 10), pady=(10, 15), row=0, column=0)

# frame for treeview
frame_tree_container = tk.Frame(label_frame_container)
frame_tree_container.grid(padx=(5, 10), pady=(10, 20))

# treeview
tree_scrollbar_container = tk.Scrollbar(frame_tree_container)
tree_scrollbar_container.grid(row=0, column=1, sticky="ns")
tree_container = ttk.Treeview(frame_tree_container, columns=("id", "weight", "destination"), yscrollcommand=tree_scrollbar_container.set, selectmode="browse")
tree_container.grid(row=0, column=0, padx=0, pady=0, sticky=tk.N)
tree_scrollbar_container.config(command=tree_container.yview)

# treeview columns
tree_container.column('#0', width=0, stretch=tk.NO)
tree_container.column('id', width=35, anchor=tk.E)
tree_container.column('weight', width=75, anchor=tk.E)
tree_container.column('destination', width=200, anchor=tk.W)

tree_container.heading('#0', text="", anchor=tk.W)
tree_container.heading("id", text="Id", anchor=tk.CENTER)
tree_container.heading("weight", text="Weight", anchor=tk.CENTER)
tree_container.heading('destination', text='Destination', anchor=tk.CENTER)

# frame for labels and entries
frame1_container = tk.Frame(label_frame_container)
frame1_container.grid(padx=(0, 10), pady=(10, 15))

# labels
label_id_container = tk.Label(frame1_container, text="Id")
label_weight_container = tk.Label(frame1_container, text="Weight")
label_destination_container = tk.Label(frame1_container, text="Destination")
label_weather_container = tk.Label(frame1_container, text="Weather")

# labels get grid functionality
label_id_container.grid(column=0, row=0)
label_weight_container.grid(column=1, row=0)
label_destination_container.grid(column=2, row=0)
label_weather_container.grid(column=3, row=0)

# entries
entry_id_container = tk.Entry(frame1_container, width=4)
entry_weight_container = tk.Entry(frame1_container, width=7)
entry_destination_container = tk.Entry(frame1_container, width=20)
entry_weather_container = tk.Entry(frame1_container, width=12)

# entries get grid functionality
entry_id_container.grid(column=0, row=1, padx=8)
entry_weight_container.grid(column=1, row=1, padx=8)
entry_destination_container.grid(column=2, row=1, padx=8)
entry_weather_container.grid(column=3, row=1, padx=(8, 0))

# frame for buttons
frame2_container = tk.Frame(label_frame_container)
frame2_container.grid(padx=(5, 10), pady=(0, 15))

# buttons
button_create_container = tk.Button(frame2_container, text="Create", command=lambda: create_container(tree_container, read_container_entries()))
button_update_container = tk.Button(frame2_container, text="Update", command=lambda: update_container(tree_container, read_container_entries()))
button_delete_container = tk.Button(frame2_container, text="Delete", command=lambda: delete_container(tree_container, read_container_entries()))
button_clear_container = tk.Button(frame2_container, text="Clear Entry Boxes", command=lambda: clear_container_entries())

# buttons get grid functionality
button_create_container.grid(column=0, row=0, padx=(20, 4))
button_update_container.grid(column=1, row=0, padx=(5, 5))
button_delete_container.grid(column=2, row=0, padx=(5, 5))
button_clear_container.grid(column=3, row=0, padx=(5, 20))


# ------------ endregion container ------------

# ----------- region aircraft ------------


# label frame
label_frame_aircraft = tk.LabelFrame(main_window, text="Aircraft")
label_frame_aircraft.grid(padx=(5, 10), pady=(10, 15), row=0, column=1)

# frame for treeview
frame_tree_aircraft = tk.Frame(label_frame_aircraft)
frame_tree_aircraft.grid(padx=(5, 10), pady=(10, 20))

# treeview
tree_scrollbar_aircraft = tk.Scrollbar(frame_tree_aircraft)
tree_scrollbar_aircraft.grid(row=0, column=1, sticky="ns")
tree_aircraft = ttk.Treeview(frame_tree_aircraft, columns=("id", "max_cargo_weight", "registration"), yscrollcommand=tree_scrollbar_aircraft.set, selectmode="browse")
tree_aircraft.grid(row=0, column=0, padx=0, pady=0, sticky=tk.N)
tree_scrollbar_aircraft.config(command=tree_aircraft.yview)

# treeview columns
tree_aircraft.column('#0', width=0, stretch=tk.NO)
tree_aircraft.column('id', width=35, anchor=tk.E)
tree_aircraft.column('max_cargo_weight', width=100, anchor=tk.E)
tree_aircraft.column('registration', width=100, anchor=tk.W)

tree_aircraft.heading('#0', text="", anchor=tk.W)
tree_aircraft.heading("id", text="Id", anchor=tk.CENTER)
tree_aircraft.heading("max_cargo_weight", text="Max.Carg.Wgt.", anchor=tk.CENTER)
tree_aircraft.heading('registration', text='Registration', anchor=tk.CENTER)

# frame for labels and entries
frame1_aircraft = tk.Frame(label_frame_aircraft)
frame1_aircraft.grid(padx=(0, 10), pady=(10, 15))

# labels
label_id_aircraft = tk.Label(frame1_aircraft, text="Id")
label_max_cargo_weight_aircraft = tk.Label(frame1_aircraft, text="Max Cargo Weight")
label_registration_aircraft = tk.Label(frame1_aircraft, text="Registration")

# labels get grid functionality
label_id_aircraft.grid(column=0, row=0)
label_max_cargo_weight_aircraft.grid(column=1, row=0)
label_registration_aircraft.grid(column=2, row=0)

# entries
entry_id_aircraft = tk.Entry(frame1_aircraft, width=4)
entry_max_cargo_weight_aircraft = tk.Entry(frame1_aircraft, width=7)
entry_registration_aircraft = tk.Entry(frame1_aircraft, width=20)

# entries get grid functionality
entry_id_aircraft.grid(column=0, row=1, padx=8)
entry_max_cargo_weight_aircraft.grid(column=1, row=1, padx=8)
entry_registration_aircraft.grid(column=2, row=1, padx=8)

# frame for buttons
frame2_aircraft = tk.Frame(label_frame_aircraft)
frame2_aircraft.grid(padx=(5, 10), pady=(0, 15))

# buttons
button_create_aircraft = tk.Button(frame2_aircraft, text="Create", command=lambda: create_container(tree_aircraft, read_container_entries()))
button_update_aircraft = tk.Button(frame2_aircraft, text="Update", command=lambda: update_container(tree_aircraft, read_container_entries()))
button_delete_aircraft = tk.Button(frame2_aircraft, text="Delete", command=lambda: delete_container(tree_aircraft, read_container_entries()))
button_clear_aircraft = tk.Button(frame2_aircraft, text="Clear Entry Boxes", command=lambda: clear_container_entries())

# buttons get grid functionality
button_create_aircraft.grid(column=0, row=0, padx=(20, 4))
button_update_aircraft.grid(column=1, row=0, padx=(5, 5))
button_delete_aircraft.grid(column=2, row=0, padx=(5, 5))
button_clear_aircraft.grid(column=3, row=0, padx=(5, 20))

# ------------ endregion aircraft ------------


# ----------- region transport ------------

# label frame
label_frame_transport = tk.LabelFrame(main_window, text="Transport")
label_frame_transport.grid(padx=(5, 10), pady=(10, 15), row=0, column=2)

# frame for treeview
frame_tree_transport = tk.Frame(label_frame_transport)
frame_tree_transport.grid(padx=(5, 10), pady=(10, 20))

# treeview
tree_scrollbar_transport = tk.Scrollbar(frame_tree_transport)
tree_scrollbar_transport.grid(row=0, column=1, sticky="ns")
tree_transport = ttk.Treeview(frame_tree_transport, columns=("id", "date", "container_id", "aircraft_id"), yscrollcommand=tree_scrollbar_transport.set, selectmode="browse")
tree_transport.grid(row=0, column=0, padx=0, pady=0, sticky=tk.N)
tree_scrollbar_transport.config(command=tree_transport.yview)

# treeview columns
tree_transport.column('#0', width=0, stretch=tk.NO)
tree_transport.column('id', width=35, anchor=tk.E)
tree_transport.column('date', width=75, anchor=tk.E)
tree_transport.column('container_id', width=75, anchor=tk.E)
tree_transport.column('aircraft_id', width=75, anchor=tk.E)

tree_transport.heading('#0', text="", anchor=tk.W)
tree_transport.heading("id", text="Id", anchor=tk.CENTER)
tree_transport.heading("date", text="Date", anchor=tk.CENTER)
tree_transport.heading('container_id', text='Container Id', anchor=tk.CENTER)
tree_transport.heading('aircraft_id', text='Aircraft Id', anchor=tk.CENTER)

# frame for labels and entries
frame1_transport = tk.Frame(label_frame_transport)
frame1_transport.grid(padx=(0, 10), pady=(10, 15))

# labels
label_id_transport = tk.Label(frame1_transport, text="Id")
label_date_transport = tk.Label(frame1_transport, text="Date")
label_container_id_transport = tk.Label(frame1_transport, text="Container Id")
label_aircraft_id_transport = tk.Label(frame1_transport, text="Aircraft Id")

# labels get grid functionality
label_id_transport.grid(column=0, row=0)
label_date_transport.grid(column=1, row=0)
label_container_id_transport.grid(column=2, row=0)
label_aircraft_id_transport.grid(column=3, row=0)

# entries
entry_id_transport = tk.Entry(frame1_transport, width=4)
entry_date_transport = tk.Entry(frame1_transport, width=10)
entry_container_id_transport = tk.Entry(frame1_transport, width=4)
entry_aircraft_id_transport = tk.Entry(frame1_transport, width=4)

# entries get grid functionality
entry_id_transport.grid(column=0, row=1, padx=8)
entry_date_transport.grid(column=1, row=1, padx=8)
entry_container_id_transport.grid(column=2, row=1, padx=8)
entry_aircraft_id_transport.grid(column=3, row=1, padx=(8, 0))

# frame for buttons
frame2_transport = tk.Frame(label_frame_transport)
frame2_transport.grid(padx=(5, 10), pady=(0, 15))

# buttons
button_create_transport = tk.Button(frame2_transport, text="Create", command=lambda: create_transport(tree_transport, read_transport_entries()))
button_update_transport = tk.Button(frame2_transport, text="Update", command=lambda: update_transport(tree_transport, read_transport_entries()))
button_delete_transport = tk.Button(frame2_transport, text="Delete", command=lambda: delete_transport(tree_transport, read_transport_entries()))
button_clear_transport = tk.Button(frame2_transport, text="Clear Entry Boxes", command=lambda: clear_transport_entries())

# buttons get grid functionality
button_create_transport.grid(column=0, row=0, padx=(20, 4))
button_update_transport.grid(column=1, row=0, padx=(5, 5))
button_delete_transport.grid(column=2, row=0, padx=(5, 5))
button_clear_transport.grid(column=3, row=0, padx=(5, 20))


# ------------ endregion transport ------------

"""
id_list = [1, 2, 3, 4]
weight_list = [1000, 2000, 3000, 4000]
destination_list = ['oslo', 'chicago', 'milano', 'amsterdam']

for x in range(len(id_list)):
    tree_container.insert(parent='', index=x, values=(id_list[x], weight_list[x], destination_list[x]))
"""
tree_container.bind("<ButtonRelease-1>", click_data)
tree_aircraft.bind("<ButtonRelease-1>", click_data_aircraft)
tree_transport.bind("<ButtonRelease-1>", click_data_transport)

if __name__ == "__main__":  # Executed when invoked directly. We use this so main_window.mainloop() does not keep our unit tests from running.
    refresh_treeview(tree_container, dcd.Container)  # Load data from database
    refresh_treeview(tree_aircraft, dcd.Aircraft)
    refresh_treeview(tree_transport, dcd.Transport)
    main_window.mainloop()  # Wait for button clicks and act upon them
