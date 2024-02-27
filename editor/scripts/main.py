import customtkinter
import tkinter as tk
import os

# from menu_Bar import Menubar


def main():
    root = customtkinter.CTk()
    root.geometry("400x300")
    root.title("NyxText")

    # This is the icon for the application. It is expected to be in the same directory as the script
    ico_path = os.path.abspath("editor\\scripts\\icon.ico")
    root.iconbitmap(ico_path)
    
    #Menu bar
    # menu_bar = Menubar(root) 
    # root.config(menu=menu_bar.menubar)

    root.mainloop()
    
if __name__ == "__main__":
    main()