import tkinter as tk
import customtkinter 
import os

# File imports here
from menu_Bar import Menubar
from text_Area import textarea

class Settings():
   
   def __init__(self, master):
        self.settings_window = customtkinter.CTkToplevel(master)
        self.settings_window.title("Settings")
        self.settings_window.geometry("300x200")
        customtkinter.CTkLabel(self.settings_window, text="Settings Window").pack()


   
