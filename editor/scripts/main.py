# main.py
import tkinter as tk
from menu_bar import Menubar
from text_area import text_Area

# This defines the main function, which is the entry point of the application
def main():
    root = tk.Tk()
    root.title("NyxText")
    
    menu_bar = Menubar(root) # This imports the Menubar class from a module named menu_bar.py. This class is expected to contain the logic for creating a menu bar for the application
    root.config(menu=menu_bar.menubar) 
    
    textarea = text_Area(root) # This imports the text_Area class from a module named text_area.py. This class is expected to contain the logic for creating a text area for the application
    
    root.mainloop()
    
# The main function is called only when the script is run directly, not when it's imported as a module
if __name__ == "__main__":
    main()
