import customtkinter as ctk

class newfile_window(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.geometry("400x200")
        self.title("New File")
        
        # Create a label for New file title
        self.newfile_label = ctk.CTkLabel(self, text="New File Options :",
                                                font=('Calibri',18,"bold"),
                                                padx=100,anchor="center")
        self.newfile_label.pack(side='top',pady=(20,0))
