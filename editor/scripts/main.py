import customtkinter
import tkinter as tk
import os

from menu_Bar import Menubar
from text_Area import textarea


def main():
    root = customtkinter.CTk()
    root.geometry("400x300")
    root.title("NyxText")

    # This is the icon for the application. It is expected to be in the same directory as the script
    ico_path = os.path.abspath("editor\\scripts\\icon.ico")
    root.iconbitmap(ico_path)
    
    # This imports the text_Area class from a module named text_area.py. This class is expected to contain the logic for creating a text area for the application
    global Textarea
    Textarea = textarea(root)
    
    # Menu bar
    menu_bar = Menubar(root,Textarea) 
    root.config(menu=menu_bar.menubar)

    root.mainloop()
    
if __name__ == "__main__":
    main()