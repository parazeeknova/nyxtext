#menu_bar
import tkinter as tk
from tkinter import filedialog, messagebox, ttk, colorchooser
from text_Area import textarea
import os as os
class Menubar:
    def __init__(self, root,text_Area):
        self.root = root
        self.text_Area = text_Area
        self.menubar = tk.Menu(self.root)
        #Defining menu options as menu objects
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.editmenu = tk.Menu(self.menubar, tearoff=0)
        self.searchmenu = tk.Menu(self.menubar, tearoff=0)
        self.viewmenu = tk.Menu(self.menubar, tearoff=0)
        self.settings = tk.Menu(self.menubar, tearoff=0)
        self.tools = tk.Menu(self.menubar, tearoff=0)
        self.macro = tk.Menu(self.menubar, tearoff=0)
        self.run = tk.Menu(self.menubar, tearoff=0)
        self.window = tk.Menu(self.menubar, tearoff=0)
        self.helpmenu = tk.Menu(self.menubar, tearoff=0)
        #Menu Bar
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)
        self.menubar.add_cascade(label="Search", menu=self.searchmenu)
        self.menubar.add_cascade(label="View", menu=self.viewmenu)
        self.menubar.add_cascade(label="Settings", menu=self.settings)
        self.menubar.add_cascade(label="Tools", menu=self.tools)
        self.menubar.add_cascade(label="Macro", menu=self.macro)
        self.menubar.add_cascade(label="Run", menu=self.run)
        self.menubar.add_cascade(label="Window", menu=self.window)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)
        #Functions of menu bar
        
        #functions of file option
        self.filemenu.add_command(label="New", command=self.new_file)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Open", command=self.open_file)
        self.filemenu.add_command(label="Open Containing Folder", command=self.open_folder)
        self.filemenu.add_command(label="Open Folder as Workspace...", command=self.open_workspace)
        self.filemenu.add_separator()

        #Save OPtions
        self.filemenu.add_command(label="Save", command=self.save_file)
        self.filemenu.add_command(label="Save As", command=self.save_as_file)
        self.filemenu.add_command(label="Save a Copy as", command=self.save_copy_as)
        self.filemenu.add_cascade(label="Save All", menu=self.save_all)
        self.filemenu.add_separator()

        self.filemenu.add_cascade(label="Rename ...", menu=self.rename)
        self.filemenu.add_separator()
        #CLose Options
        self.filemenu.add_cascade(label="Close", menu=self.close)
        self.filemenu.add_cascade(label="Close All", menu=self.close_all)
        self.filemenu.add_cascade(label="Close Multiple Documents", menu=self.close_multiple)
        
        self.filemenu.add_cascade(label="Move to Recycle Bin", menu=self.move_to_recycle)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.exit_editor)
        #functions for edit option
        self.editmenu.add_command(label="Undo", command=self.undo)
        self.editmenu.add_command(label="Redo", command=self.redo)
        self.editmenu.add_separator()
        self.editmenu.add_command(label="Cut", command=self.cut)
        self.editmenu.add_command(label="Copy", command=self.copy)
        
    # Define the methods for your menu commands here
    def new_file(self):
        pass
    file_path = None
    def save_file(self):
        # global self.file_path
        if self.file_path and os.path.exists(self.file_path):
            # Write to the file and close it
            with open(self.file_path, "w") as file:
                file.write(self.text_Area.text_area.get(1.0, tk.END))
        else:
            self.save_as_file()
    def open_file(self):
        self.file_path = filedialog.askopenfilename(defaultextension=".txt",
                                                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if self.file_path:
            with open(self.file_path, "r") as file:
                self.text_Area.text_area.delete(1.0, tk.END)  # Clear the text area
                self.text_Area.text_area.insert(tk.INSERT, file.read())  # Insert the file content
        
    def save_as_file(self):
        self.file_path = filedialog.asksaveasfile(defaultextension=".txt",
                                        filetypes=[("Text file","*.txt"),("All Files","*.*")])
        if not self.file_path:
            return
        self.file_path.write(self.text_Area.text_area.get(1.0, tk.END))
        self.file_path.close()
    

    def exit_editor(self):
        if messagebox.askokcancel("Exit ?","Do you want to save your changes?"):
            self.save_file()
        self.root.destroy()
        
    def open_folder(self):
        pass

    def open_workspace(self):
        pass

    def save_copy_as(self):
        pass

    def save_all(self):
        pass

    def rename(self):
        pass

    def close(self):
        pass

    def close_all(self):
        pass

    def close_multiple(self):
        pass

    def move_to_recycle(self):
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