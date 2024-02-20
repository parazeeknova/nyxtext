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
    
    # Creates frame left for side bar and right for text area
    left_frame = tk.Frame(root)
    left_frame.pack(side=tk.LEFT, fill=tk.Y)
    right_frame = tk.Frame(root)
    right_frame.pack(side=tk.RIGHT, fill=tk.Y)
    
    # This imports the text_Area class from a module named text_area.py. This class is expected to contain the logic for creating a text area for the application
    global Textarea
    Textarea = textarea(right_frame)

    # This imports the Menubar class from a module named menu_bar.py. This class is expected to contain the logic for creating a menu bar for the application
    menu_bar = Menubar(root,Textarea) 
    root.config(menu=menu_bar.menubar) 
    # Temprory button to switch themes for testing
    theme_button = tk.Button(left_frame, text="Toggle Theme", command=lambda: toggle_theme(right_frame,left_frame))
    theme_button.pack(side="bottom",padx=10,pady=5)

    # This is the main loop of the application. It keeps the application running until it is closed
    root.mainloop()
    
# The main function is called only when the script is run directly, not when it's imported as a module
if __name__ == "__main__":
    main()
