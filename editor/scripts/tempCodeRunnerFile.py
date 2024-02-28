# System imports here
import customtkinter
import tkinter as tk
import os

# File imports here
from menu_Bar import Menubar
from text_Area import textarea


def main():
# This defines the main function, which is the entry point of the application
    root = customtkinter.CTk()
    root.geometry("400x300")
    root.title("NyxText")
    
# Sets (for now the appearance to light and color scheme to blue)
    customtkinter.set_appearance_mode("light")
    
# Should be replaced with a function in future for catppuccin color scheme 
    customtkinter.set_default_color_theme("blue")

# This is the icon for the application. It is expected to be in the same directory as the script
    ico_path = os.path.abspath("editor\\scripts\\icon.ico")
    root.iconbitmap(ico_path)
    
# Setting width of the left frame 10 percent of the screen 
    screen_width = root.winfo_screenwidth()
    frame_width = screen_width *  0.10
    rf = int(screen_width-frame_width)
# Frames 
    left_frame = customtkinter.CTkFrame(root, width=int(frame_width), height=int(screen_width))
    left_frame.grid(row=0, column=0, sticky='nsew') # Ensure left_frame is correctly placed
    
    right_frame = customtkinter.CTkFrame(root, width=rf, height=int(screen_width))
    right_frame.grid(row=0, column=1, sticky='nsew')
# This imports the text_Area class from a module named text_area.py. This class is expected to contain the logic for creating a text area for the application
    global Textarea
    Textarea = textarea(right_frame,int(screen_width), rf)
    
# This imports the Menubar class from a module named menu_bar.py. This class is expected to contain the logic for creating a menu bar for the application
    menu_bar = Menubar(root,Textarea) 
    root.config(menu=menu_bar.menubar)

# This is the main loop of the application. It keeps the application running until it is closed
    root.mainloop()
    
# The main function is called only when the script is run directly, not when it's imported as a module 
if __name__ == "__main__":
    main()