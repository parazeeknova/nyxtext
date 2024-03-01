# System imports here
import customtkinter
import tkinter as tk
import os

# File imports here
from menu_Bar import Menubar
from text_Area import textarea
from settings import Settings


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
    screen_height = root.winfo_screenheight() - 150
    frame_width = screen_width *  0.10
    rf = int(screen_width-frame_width)
    
# Static frames at the moment will be replaced by scrollable frames after a while
    top_frame = customtkinter.CTkFrame(root, width=screen_width, height=30) # Adjust height as needed
    top_frame.grid(row=0, column=0, columnspan=2, sticky='ew')
    
    left_frame = customtkinter.CTkFrame(root, width=int(frame_width), height=int(screen_width))
    left_frame.grid(row=1, column=0, sticky='nsew') # Ensure left_frame is correctly placed
    
    right_frame = customtkinter.CTkFrame(root, width=rf, height=int(screen_width))
    right_frame.grid(row=1, column=1, sticky='nsew')
    
    bottom_frame = customtkinter.CTkFrame(root, width=screen_width, height=30)
    bottom_frame.grid(row=2, column=0, columnspan=2, sticky='ew')

# Creates a tab view to show tabs (Static at the moment), Need to impliment the dynamic tab view
    tab_view = customtkinter.CTkTabview(right_frame,width=rf, height=int(screen_width))
    tab_view.grid(row=0, column=1, sticky='nsew')
    tab_1 = tab_view.add("Tab 1")
    tab_2 = tab_view.add("Tab 2")
    
# This imports the text_Area class from a module named text_area.py. This class is expected to contain the logic for creating a text area for the application
    global Textarea
    Textarea = textarea(tab_1,int(screen_width),rf,int(screen_height))
    
# This imports the Menubar class from a module named menu_bar.py. This class is expected to contain the logic for creating a menu bar for the application
    menu_bar = Menubar(root,Textarea) 
    root.config(menu=menu_bar.menubar)

# Test Area will be removed after few commits: 
    testoptionmenu = customtkinter.CTkOptionMenu(top_frame,values=["option 1", "option 2"])
    testoptionmenu.pack(side="left",padx=5,pady=10)
    
    testoptionmenu2 = customtkinter.CTkOptionMenu(top_frame,values=["option 2", "option 2"])
    testoptionmenu2.pack(side="left",padx=5,pady=10)
    
    testoptionmenu3 = customtkinter.CTkOptionMenu(top_frame,values=["option 3", "option 2"])
    testoptionmenu3.pack(side="left",padx=5,pady=10)

    def open_settings_window():
        settings = Settings(root)
    testoptionmenu4 = customtkinter.CTkButton(top_frame, text="Settings",command=open_settings_window)
    testoptionmenu4.pack(side="left",padx=5,pady=10)

    entry = customtkinter.CTkEntry(top_frame, placeholder_text="Search", width=400)
    entry.pack(side="left",padx=500,pady=10)
    
    utton = customtkinter.CTkButton(left_frame, text="Files")
    utton.pack(side="top",padx=10,pady=22)
    

# This is the main loop of the application. It keeps the application running until it is closed
    root.mainloop()
    
# The main function is called only when the script is run directly, not when it's imported as a module 
if __name__ == "__main__":
    main()