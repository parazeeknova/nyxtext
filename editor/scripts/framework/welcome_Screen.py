# Welcome Screen :

import customtkinter
import os

from PIL import Image
from about import MyWindow

# File Imports here : 
from framework.new_file import newfile_window
from framework.open_file import openfile_window
from framework.open_folder import openfolder_window

class WelcomeScreen:
    def __init__(self, tab_view):
        self.welcome_tab = tab_view.add("Welcome")
        self.tab_view = tab_view
        
        # Creating execption handeling for windows & Linux
        welcome_title_text = customtkinter.CTkLabel(self.welcome_tab, text="NyxText",
                                                    font=('JetBrainsMono NF',80,"bold"),
                                                    padx=100,anchor="center")
        welcome_title_text.pack(side='top',pady=(100,0))

        welcome_title_desc = customtkinter.CTkLabel(self.welcome_tab, text="- A Catppuccin based Text Editor",
                                                        font=('JetBrainsMono NF',20,"italic"),
                                                        padx=100,anchor="center")
        welcome_title_desc.pack(side='top')
            
        
        welcome_title_start = customtkinter.CTkLabel(self.welcome_tab, text="Start",
                                                    font=('JetBrainsMono NF',16,"bold"),
                                                    padx=100,anchor="center")
        welcome_title_start.pack(side='top',pady=(30,10))
    
    # Opens a new window for creating a new file : 
        def new_window(master):
                new = newfile_window(master)
        welcome_new_button = customtkinter.CTkButton(self.welcome_tab,text=" New file... ", command=lambda: new_window(self.welcome_tab),
                                                fg_color='transparent',hover=False,anchor="center",text_color='#ed8796')
        welcome_new_button.pack()
        
        def open_window(master):
                open = openfile_window(master)
        welcome_open_button = customtkinter.CTkButton(self.welcome_tab,text=" Open file... ", command=lambda: open_window(self.welcome_tab),
                                                fg_color='transparent',hover=False,anchor="center",text_color='#a6da95')
        welcome_open_button.pack()
        
        def openfol_window(master):
                openfolder = openfolder_window(master)
        welcome_openfolder_button = customtkinter.CTkButton(self.welcome_tab,text=" Open Folder... ", command=lambda: openfol_window(self.welcome_tab),
                                                fg_color='transparent',hover=False,anchor="center",text_color='#91d7e3')
        welcome_openfolder_button.pack()
    
        def about_window(master):
                about = MyWindow(master)
        welcome_about_button = customtkinter.CTkButton(self.welcome_tab, text=" About... ",
                                    fg_color='transparent', hover=False, anchor="center", text_color='#8aadf4', command=lambda: about_window(self.welcome_tab))
        welcome_about_button.pack()
    
        welcome_title_recents = customtkinter.CTkLabel(self.welcome_tab, text="Recents",
                                                font=('JetBrainsMono NF',16,"bold"),
                                                padx=100,anchor="center")
        welcome_title_recents.pack(side='top',pady=(30,10))
    
    # Static at the moment need to replace with dynamic :
        welcome_recent = customtkinter.CTkButton(self.welcome_tab,text=" Github/Parazeeknova/Nyxtext ",
                                                fg_color='transparent',hover=False,anchor="center",text_color='#ee99a0')
        welcome_recent.pack()
    
        welcome_recent = customtkinter.CTkButton(self.welcome_tab,text=" Github/Parazeeknova ",
                                                fg_color='transparent',hover=False,anchor="center",text_color='#ee99a0')
        welcome_recent.pack()