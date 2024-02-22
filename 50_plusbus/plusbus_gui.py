import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import plusbus_data as pbd
import plusbus_sql as pbsql
import plusbus_func as pbf


# main window
main_window = tk.Tk()
main_window.title("Plusbus GUI")
main_window.geometry("1200x500")

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
tree_kunder = ttk.Treeview(frame_tree_kunder, columns=("efternavn", "kontakt"), yscrollcommand=tree_scrollbar_kunder.set, selectmode="browse")
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


