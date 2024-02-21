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
    
    # Setting width of the left frame 10 percent of the screen 
    screen_width = root.winfo_screenwidth()
    frame_width = screen_width *  0.10
    
    # Creates frame left for side bar and right for text area, bottom for the bottom menu bar
    left_frame = tk.Frame(root)
    left_frame.place(x = frame_width, y=0, width=frame_width, height=screen_width)
    right_frame = tk.Frame(root)
    right_frame.place(x=frame_width, y=0, width=screen_width-frame_width, height=screen_width)
    bottom_frame = tk.Frame(root)
    bottom_frame.pack(side="bottom",fill="x")
    
    # This imports the text_Area class from a module named text_area.py. This class is expected to contain the logic for creating a text area for the application
    global Textarea
    Textarea = textarea(right_frame)

    # This imports the Menubar class from a module named menu_bar.py. This class is expected to contain the logic for creating a menu bar for the application
    menu_bar = Menubar(root,Textarea) 
    root.config(menu=menu_bar.menubar) 
    # Temprory button to switch themes for testing
    theme_button = tk.Button(bottom_frame, text="Toggle Theme", command=lambda: toggle_theme(root))
    theme_button.pack(side="left",padx=10,pady=5)

    # This is the main loop of the application. It keeps the application running until it is closed
    root.mainloop()
    
# The main function is called only when the script is run directly, not when it's imported as a module
if __name__ == "__main__":
    main()
