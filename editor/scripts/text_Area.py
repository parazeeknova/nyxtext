import customtkinter as ctk
class textarea():
    def __init__(self,root):
        self.root = root
        self.text_area = ctk.CTkTextbox(root, wrap=ctk.WORD) # Create a text area
        self.text_area.pack(expand=True, fill=ctk.BOTH)
