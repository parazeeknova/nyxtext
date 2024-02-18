import tkinter as tk
from tkinter import filedialog, messagebox, ttk, colorchooser
from text_area import text_Area
class Menubar:
    def __init__(self, root):
        self.root = root
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
        # Logic for creating a new file
        pass

    def open_file(self):
        # Logic for opening a file
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                            filetypes=[("Text Files","*.txt"),("All Files","*.*")])
        if not file_path: 
            return
        with open(file_path, "r") as file:
            text_Area.text_Area.delete(1.0, tk.END)
            text_Area.text_Area.insert(1.0,file.read())
    def save_file(self):
        # Logic to save the file
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                filetypes=[("Text Files","*.txt"),("All Files","*.*")])
        if not file_path:
            return
        with open(file_path,"w") as file:
            file.write(text_Area.text_Area.get(1.0, tk.END))
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

    # ... and so on for the other commands ...

    # Don't forget to add your edit menu to the menubar
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)