#menu_bar
import tkinter as tk
from tkinter import filedialog, messagebox, ttk, colorchooser
from text_Area import textarea
class Menubar:
    def __init__(self, root,text_Area):
        self.root = root
        self.text_Area = text_Area
        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="New", command=self.new_file)
        self.filemenu.add_command(label="Open", command=self.open_file)
        self.filemenu.add_command(label="Save", command=self.save_file)
        self.filemenu.add_command(label="Save As", command=self.save_as_file)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.exit_editor)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.editmenu = tk.Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label="Undo", command=self.undo)
        self.editmenu.add_command(label="Redo", command=self.redo)
        self.editmenu.add_separator()
        self.editmenu.add_command(label="Cut", command=self.cut)
        self.editmenu.add_command(label="Copy", command=self.copy)
        # ... rest of your menu bar code ...

    # Define the methods for your menu commands here
    def new_file(self):
        pass

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                self.text_Area.text_area.delete(1.0, tk.END)  # Clear the text area
                self.text_Area.text_area.insert(tk.INSERT, file.read())  # Insert the file content
    def save_file(self):
        pass
    def save_as_file(self):
        pass
    def exit_editor(self):
        pass
    def undo(self):
        pass
    def redo(self):
        pass
    def cut(self):
        pass
    def copy(self):
        pass


        self.menubar.add_cascade(label="Edit", menu=self.editmenu)