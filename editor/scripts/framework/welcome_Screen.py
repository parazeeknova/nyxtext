import customtkinter
import tkinter as tk
import os
from new_file import newfile_window
from open_file import openfile_window
from open_folder import openfolder_window
from about import MyWindow

class WelcomeScreen:
    def __init__(self, tab_view):
        self.welcome_tab = tab_view.add("Welcome")
        self.tab_view = tab_view

    def create_welcome_tab(self):
        # ... (code to create the welcome tab)
        pass

    def new_window(self, master):
        new = newfile_window(master)

    def open_window(self, master):
        open = openfile_window(master)

    def openfol_window(self, master):
        openfolder = openfolder_window(master)

    def about_window(self, master):
        about = MyWindow(master)