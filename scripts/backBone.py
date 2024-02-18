# This is an ancient code snippet from the original NyxText project.
# It is not used in this project.
# Version v0.0.1-alpha-firstrelease uses this ancient buggy, stupiud code snippet.
# This file is discontinued and will be removed in the future or not maybe.

# RELIC CODE



import tkinter as tk
from tkinter import filedialog, messagebox, ttk, colorchooser

#import scripts.menu as menu

# Function to handle opening a file
def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not file_path:
        return
    with open(file_path, "r") as file:
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.INSERT, file.read())
        

# Function to handle saving a file
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not file_path:
        return
    with open(file_path, "w") as file:
        file.write(text_area.get(1.0, tk.END))

# Function to handle creating a new file
def new_file():
    tk.Toplevel() ###TO create new file We will try in future taking lots of brain memory
    

# Function to handle changing the text color
def change_color():
    color = colorchooser.askcolor()
    if color[1] is not None:
        text_area.config(fg=color[1])

# Function to handle changing the text font
def change_font():
    font_name = font_name_var.get()
    font_size = font_size_var.get()
    text_area.config(font=(font_name, font_size))

# Function to handle searching text
def search_text():
    search_query = search_entry.get()
    text_area.tag_remove("highlight", "1.0", tk.END)
    if search_query:
        start = "1.0"
        while True:
            start = text_area.search(search_query, start, tk.END)
            if not start:
                break
            end = f"{start}+{len(search_query)}c"
            text_area.tag_add("highlight", start, end)
            start = end
        text_area.tag_config("highlight", background="yellow", foreground="black")

# Function to add a new tab
def add_new_tab():
    tab = ttk.Frame(tabs)
    tabs.add(tab, text='Tab '+ str(tabs.index(tk.END) + 1))
    
    
# Function to clear all tabs except for Tab  1
def clear_all_tabs_except_first():
    # Get the total number of tabs
    total_tabs = tabs.index('end') +  1
    
    # Loop through all tabs except for the first one
    for i in range(3, total_tabs):
        # Get the widget associated with the tab
        tab_widget = tabs.tab(i, 'widget')
        # Remove the tab from the notebook
        tabs.forget(tab_widget)
def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("New Window")
    new_window.geometry("200x200")
    tk.Label(new_window, text="This is a new window").pack()
# Create the main window
root = tk.Tk()
root.title("Python Text Editor")

#Logo
# logo = tk.PhotoImage(file="main\\assets\\logo\\text-edit-icon-9.png")
# root.iconphoto(False, logo)

# Create a text area
text_area = tk.Text(root, wrap=tk.WORD)
text_area.pack(expand=True, fill=tk.BOTH)

# Create a scrollbar
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure the scrollbar to work with the text area
text_area.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text_area.yview)

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a file menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Create an edit menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=lambda: text_area.event_generate("<<Cut>>"))
edit_menu.add_command(label="Copy", command=lambda: text_area.event_generate("<<Copy>>"))
edit_menu.add_command(label="Paste", command=lambda: text_area.event_generate("<<Paste>>"))
edit_menu.add_command(label="Clear Page", command=lambda: text_area.delete(1.0, tk.END))
edit_menu.add_command(label="Add Tab",command=add_new_tab)

# Create a search menu
search_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Search", menu=search_menu)
search_menu.add_command(label="Find", command=search_text)

# Create a view menu
view_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="View", menu=view_menu)
view_menu.add_command(label="Change Color", command=change_color)
view_menu.add_command(label="Clear all Tabs", command=clear_all_tabs_except_first)
# Create a settings menu
settings_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Settings", menu=settings_menu)
font_name_var = tk.StringVar(root) 
font_name_var.set("Arial")
font_size_var = tk.StringVar(root)
font_size_var.set("12")
settings_menu.add_command(label="Change Font", command=change_font)

# Create a help menu
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "Python Text Editor"))

#Button for Dark and Light Mode
theme_button = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Theme", menu=theme_button,compound="right")

# Create the Notebook widget and add it to the window
tabs = ttk.Notebook(root)
tabs.pack(expand=1, fill='both')

# Add two initial tabs
tab1 = ttk.Frame(tabs)
tabs.add(tab1, text='Tab  1')

tab2 = ttk.Frame(tabs)
tabs.add(tab2, text='Tab  2')

#Add more tabs 
add_tab_button = tk.Button(root, text="+", command=add_new_tab)
add_tab_button.pack(side="left")  # Place the button next to the tabs

# Start the Tkinter event loop
root.mainloop()
