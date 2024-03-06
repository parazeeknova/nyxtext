from tkinter import *
import tkinter as tk
from tkinter import filedialog, messagebox, ttk, colorchooser
import menu_Bar
import customtkinter
from text_Area import textarea
# Assuming label_element is defined here for simplicity
label_element = [
    "New", "Open", "Open Containing Folder", "Open Folder as Workspace...",
    "Save", "Save As", "Save a Copy as", "Save All", "Rename ...", "Exit",
    "Undo", "Redo", "Cut", "Copy", "Paste", "Delete", "Select All",
    "Find", "Find in Files ...",
    "Syntax highlighting", "Auto Complete", "Git integration",
    "Terminal", "Tabs", "Github Repo", "Discord"
]

class SearchWindow(Toplevel):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Search Window")
        self.geometry("400x200")
        
        
        # Create combobox with options from label_element
        self.combobox = customtkinter.CTkComboBox(self, values=label_element)
        self.combobox.pack(pady=20)
        
        # Create a "Select" button
        self.select_button = customtkinter.CTkButton(self, text="Select")
        self.select_button.pack(pady=10)
        self.select_button.configure(command=self.call_function) # Bind the method correctly

    def call_function(self):
        selected_label = self.combobox.get()
        if selected_label == "Open":
            # Assuming Menubar.open_file is a static method or accessible instance method
            self.open_file()
        else:
            pass
        # Add more conditions here for other actions

    def open_file(self):
        self.file_path_1 = filedialog.askopenfilename(defaultextension=".txt",
                                                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if self.file_path_1:
            with open(self.file_path_1, "r") as file:
                self.text_Area.text_area.delete(1.0, tk.END)  # Clear the text area
                self.text_Area.text_area.insert(tk.INSERT, file.read())  # Insert the file content