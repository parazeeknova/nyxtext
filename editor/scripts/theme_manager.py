# theme_manager.py
import tkinter as tk
from tkinter import ttk, colorchooser

def toggle_theme(root):
    current_theme = root.cget("bg")  # Get the current theme color
    if current_theme == "white":
        # Switch to dark theme
        root.configure(bg='#26242f')
        # Change the theme of all widgets
        for widget in root.winfo_children():
            widget.configure(bg='#26242f')
    else:
        # Switch to light theme
        root.configure(bg='white')
        # Change the theme of all widgets
        for widget in root.winfo_children():
            widget.configure(bg='white')