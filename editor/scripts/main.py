# main.py
import tkinter as tk
from tkinter import filedialog, messagebox, ttk, colorchooser
import os
from menu_bar import Menubar
from text_Area import textarea
from theme_manager import toggle_theme

# This defines the main function, which is the entry point of the application
def main():
    root = tk.Tk()
    root.geometry("800x600")
    root.title("NyxText")
    
    # This is the icon for the application. It is expected to be in the same directory as the script
    ico_path = os.path.abspath("editor\\scripts\\icon.ico")
    root.iconbitmap(ico_path) 
    
    # This imports the text_Area class from a module named text_area.py. This class is expected to contain the logic for creating a text area for the application
    global Textarea
    Textarea = textarea(root)

    # This imports the Menubar class from a module named menu_bar.py. This class is expected to contain the logic for creating a menu bar for the application
    menu_bar = Menubar(root,Textarea) 
    root.config(menu=menu_bar.menubar) 
    # Temprory button to switch themes for testing
    theme_button = tk.Button(root, text="Toggle Theme", command=lambda: toggle_theme(root))
    theme_button.pack(pady=10)

    
    root.mainloop()
    
# The main function is called only when the script is run directly, not when it's imported as a module
if __name__ == "__main__":
    main()
