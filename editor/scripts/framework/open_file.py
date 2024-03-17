# Open File option in Welcome Screen : 

import customtkinter as ctk
from tkinter import filedialog
import tkinter as tk
import os
from framework.tab_View import TabView

class openfile_window(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Open File options: ")
        # Creating execption handeling for windows & Linux
        if os.name == 'nt': 
                self.wm_attributes('-topmost', True)
        elif os.name=="posix":
            self.wm_attributes('-type','splash')
        # Center the window on the screen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = 280
        window_height = 260
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        self.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        self.attributes('-alpha', 0.95)
        
        # Create a label for New file title
        self.open_label = ctk.CTkLabel(self, text="◉",font=("JetBrainsMono NF", 40),text_color='#a6da95')
        self.open_label.pack(side='top',pady=(10,0),anchor="center")
        
        self.label_new = ctk.CTkLabel(self, text="New File", font=("JetBrainsMono NF", 20, 'bold'),text_color='#a6da95')
        self.label_new.pack(side='top',anchor="center")
        
        self.label_sep = ctk.CTkLabel(self, text="------", font=("JetBrainsMono NF", 20, 'bold'),text_color='#8aadf4')
        self.label_sep.pack(side='top',anchor="center")

        # File Path Entry Box
        self.file_path_entry = ctk.CTkEntry(self, width=300, height=25, corner_radius=5, placeholder_text="Enter File Path...",justify='center')
        self.file_path_entry.pack(side='top', pady=(0,10),anchor="center")
        
        # Buttons
        self.button1 = ctk.CTkButton(self, text="Open in Workspace", width=100, height=25, corner_radius=5,text_color='#91d7e3',command=self.open_work)
        self.button1.pack(side='bottom',pady=5)
        
        self.button2 = ctk.CTkButton(self, text="Open in Codespace", width=100, height=25, corner_radius=5,text_color='#ee99a0',command=self.open_code)
        self.button2.pack(side='bottom',pady=5)
        
        self.button_open = ctk.CTkButton(self, text="Open", width=100, height=25, corner_radius=5, text_color='#8aadf4',command=self.open_file)
        self.button_open.pack(side="bottom",pady=5)

    def open_work(self):pass
    def open_code(self):pass
    def open_file(self):pass