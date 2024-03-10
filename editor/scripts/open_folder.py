import customtkinter as ctk

class openfolder_window(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.geometry("400x200")
        self.title("New File")
        
        # Create a label for New file title
        self.openfolder_label = ctk.CTkLabel(self, text="Open Folder content in workspaces :",
                                                font=('Calibri',18,"bold"),
                                                padx=100,anchor="center")
        self.openfolder_label.pack(side='top',pady=(20,0))