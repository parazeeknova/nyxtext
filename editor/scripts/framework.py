import customtkinter
import tkinter as tk
from tkinter import filedialog, messagebox, ttk, colorchooser
import os

# Currenty this code does not work need to work upon this in future, untill then this fill will not be imported anywhere
class Framework:
    def __init__(self,root,selected_tab):
        self.root = root
        self.selected_tab = selected_tab
        self.file_path_1 = None
        
        # To Open file in selected Workspace: 
        def open_file(self):
            self.file_path_1 = filedialog.askopenfilename(defaultextension=".txt",
                                                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
            if self.file_path_1:
                with open(self.file_path_1, "r") as file:
                    self.selected_tab.delete(1.0, tk.END)  # Clear the text area
                    self.selected_tab.insert(tk.INSERT, file.read())