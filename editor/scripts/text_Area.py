import tkinter as tk
class text_Area():
    def __init__(self,root):
        self.root = root
        self.text_area = tk.Text(root, wrap=tk.WORD)
        self.text_area.pack(expand=True, fill=tk.BOTH)

