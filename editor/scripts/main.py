# System imports here
import customtkinter
import tkinter as tk
import os
import webbrowser

# File imports here
from menu_Bar import Menubar
from text_Area import textarea
from settings import Settings

# customtkinter.set_widget_scaling(80)
# customtkinter.set_window_scaling(80)

def main():
# This defines the main function, which is the entry point of the application
    root = customtkinter.CTk()
    root.geometry("800x600")
    root.title("NyxText")
    
# Sets (for now the appearance to light and color scheme to blue)
    customtkinter.set_appearance_mode("dark")
    
# Should be replaced with a function in future for catppuccin color scheme 
    customtkinter.set_default_color_theme("dark-blue")

# This is the icon for the application. It is expected to be in the same directory as the script
    ico_path = os.path.abspath("editor\\scripts\\icon.ico")
    root.iconbitmap(ico_path)
    
# Setting width of the left frame 10 percent of the screen 
    screen_width = root.winfo_screenwidth() - 50
    screen_height = root.winfo_screenheight() - 200
    frame_width = screen_width *  0.10
    rf = int(screen_width-frame_width)
    
# Static frames at the moment will be replaced by scrollable frames after a while
    top_frame = customtkinter.CTkFrame(root, width=screen_width, height=10) # Adjust height as needed
    top_frame.grid(row=0, column=0, columnspan=2, sticky='ew')
    
    left_frame = customtkinter.CTkFrame(root, width=int(frame_width), height=int(screen_height))
    left_frame.grid(row=1, column=0, sticky='nsew') # Ensure left_frame is correctly placed
    
    right_frame = customtkinter.CTkScrollableFrame(root, width=rf,)
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
    
# All buttons and search bar in the top frame for different functions (Right)
    
    def open_settings_window():
        settings = Settings(root)
    settings_button = customtkinter.CTkButton(top_frame, text="⚙️",command=open_settings_window)
    settings_button.pack(side="right",padx=5,pady=10)
    settings_button.configure(width=10)
    
    def Seperator_R():
        Seperator = customtkinter.CTkLabel(top_frame, text="|")
        Seperator.pack(side="right",padx=2,pady=10)
        Seperator.configure(width=2,font = ("Arial",16),fg_color="transparent")
    Seperator_R()
    
    def chat_gpt():
            webbrowser.open('https://chat.openai.com/')
    chat_gpt_button = customtkinter.CTkButton(top_frame, text="⚙️ ChatGPT",command=chat_gpt)
    chat_gpt_button.pack(side="right",padx=5,pady=10)
    chat_gpt_button.configure(width=10)
    
    def Phind():
            webbrowser.open('https://www.phind.com/')
    chat_gpt_button = customtkinter.CTkButton(top_frame, text="Phind",command=Phind)
    chat_gpt_button.pack(side="right",padx=5,pady=10)
    chat_gpt_button.configure(width=10)
    
    def Blackbox_AI():
            webbrowser.open('https://www.blackbox.ai/')
    chat_gpt_button = customtkinter.CTkButton(top_frame, text="BlackBox AI",command=Blackbox_AI)
    chat_gpt_button.pack(side="right",padx=5,pady=10)
    chat_gpt_button.configure(width=10)
    
    def Gemini():
            webbrowser.open('https://gemini.google.com/')
    chat_gpt_button = customtkinter.CTkButton(top_frame, text="Gemini",command=Gemini)
    chat_gpt_button.pack(side="right",padx=5,pady=10)
    chat_gpt_button.configure(width=10)
    
    Seperator_R()
    
    # Commented at the moment, will implement later
    
    # right_arrow = customtkinter.CTkButton(top_frame, text=">")
    # right_arrow.pack(side="right",padx=1,pady=10)
    # right_arrow.configure(width= 2,fg_color="transparent")
    
    Search_bar = customtkinter.CTkEntry(top_frame, placeholder_text="🔍 Search")
    Search_bar.pack(side="right",padx=5,pady=10)
    Search_bar.configure(width=250, font = ("VictorMono Nerd Font Bold",15))
    
    # Commented at the moment, will be implemented later 
    
    # left_arrow = customtkinter.CTkButton(top_frame, text="<")
    # left_arrow.pack(side="right",padx=1,pady=10)
    # left_arrow.configure(width= 2,fg_color="transparent")
    
    Seperator_R()
    
# All buttons in the top frame for different functions (Left)
    New_button = customtkinter.CTkButton(top_frame, text="📄")
    New_button.pack(side="left",padx=2,pady=10)
    New_button.configure(width=2,font = ("Arial",18),fg_color="transparent")
    
    Open_button = customtkinter.CTkButton(top_frame, text="📂")
    Open_button.pack(side="left",padx=2,pady=10)
    Open_button.configure(width=2,font = ("Arial",18),fg_color="transparent")
    
    Save_button = customtkinter.CTkButton(top_frame, text="💾")
    Save_button.pack(side="left",padx=3,pady=10)
    Save_button.configure(width=2,font = ("Arial",18),fg_color="transparent")
    
    def Seperator():
        Seperator = customtkinter.CTkLabel(top_frame, text="|")
        Seperator.pack(side="left",padx=2,pady=10)
        Seperator.configure(width=2,font = ("Arial",16),fg_color="transparent")
    Seperator()
        
    Cut_button = customtkinter.CTkButton(top_frame, text="Cut")
    Cut_button.pack(side="left",padx=3,pady=10)
    Cut_button.configure(width=2)
    
    Copy_button = customtkinter.CTkButton(top_frame, text="Copy")
    Copy_button.pack(side="left",padx=3,pady=10)
    Copy_button.configure(width=2)
    
    Paste_button = customtkinter.CTkButton(top_frame, text="Paste")
    Paste_button.pack(side="left",padx=3,pady=10)
    Paste_button.configure(width=2)
    
    Seperator()
    
    Exit_button = customtkinter.CTkButton(top_frame, text="Exit")
    Exit_button.pack(side="left",padx=3,pady=10)
    Exit_button.configure(width=2)
    
    Dark_Light_mode = customtkinter.CTkButton(top_frame, text="🌓")
    Dark_Light_mode.pack(side="left",padx=2,pady=10)
    Dark_Light_mode.configure(width=2,font = ("Arial",16))
    
    About = customtkinter.CTkButton(top_frame, text="About")
    About.pack(side="left",padx=2,pady=10)
    About.configure(width=2)
    
    Seperator()
    
    Discussion = customtkinter.CTkButton(top_frame, text="NyxText - Discussions")
    Discussion.pack(side="left",padx=2,pady=10)
    Discussion.configure(width=3)
    
    Issues = customtkinter.CTkButton(top_frame, text="Report an Issue")
    Issues.pack(side="left",padx=2,pady=10)
    Issues.configure(width=3)
    
    Suggestions = customtkinter.CTkButton(top_frame, text="Suggest a Feature")
    Suggestions.pack(side="left",padx=2,pady=10)
    Suggestions.configure(width=3) 
    
# All buttons in the bottom frame for different functions
    Color_Scheme_Button = customtkinter.CTkLabel(bottom_frame, text="Color Scheme :")
    Color_Scheme_Button.pack(side="left",padx=2,pady=10)
    Color_Scheme_Button.configure(width=2,fg_color="transparent")

    Color_Scheme_button = customtkinter.CTkSegmentedButton(bottom_frame, values=["Frappe", "Latte", "Macchiato", "Mocha"])
    Color_Scheme_button.pack(side="left",padx=5,pady=10)
    Color_Scheme_button.configure(width=10)

# This is the main loop of the application. It keeps the application running until it is closed
    root.mainloop()
    
# The main function is called only when the script is run directly, not when it's imported as a module 
if __name__ == "__main__":
    main()