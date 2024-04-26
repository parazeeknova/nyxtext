from tkinter import *

import customtkinter

# Assuming label_element is defined here for simplicity
label_element = [
    "New",
    "Open",
    "Open Containing Folder",
    "Save",
    "Save As",
    "Rename ...",
    "Exit",
    "Undo",
    "Redo",
    "Cut",
    "Copy",
    "Paste",
    "Delete",
    "Select All",
    "Terminal",
    "About",
    "Add Workspace",
    "Add codespace",
    "Colour Scheme",
    "Syatem Themes",
    "Font size",
    "Scaling",
    "Save all...",
]


class Searchwindow:
    def __init__(self, master):
        inputbox = customtkinter.CTkInputDialog(text="Search...", title="Search")
