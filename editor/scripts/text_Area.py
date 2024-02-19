#text_Area
import tkinter as tk
class textarea():
    def __init__(self,root):
        self.root = root
        self.text_area = tk.Text(root, wrap=tk.WORD) # Create a text area
        self.text_area.pack(expand=True, fill=tk.BOTH)
