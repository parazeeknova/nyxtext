import customtkinter as ctk

class MyWindow(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.geometry("400x500")
        self.wm_overrideredirect(True)
        # Create a label with big bold text in the top and middle
        self.welcome_title_text = ctk.CTkLabel(self, text="NyxText",
                                                font=('JetBrainsMono NF',80,"bold"),
                                                padx=100,anchor="center")
        self.welcome_title_text.pack(side='top',pady=(100,0))

        welcome_title_desc = ctk.CTkLabel(self, text="- A Catppuccin based Text Editor",
                                                    font=('JetBrainsMono NF',20,"italic"),
                                                    padx=100,anchor="center")
        welcome_title_desc.pack(side='top')
        # Create a label with normal text just below the big bold text
        self.label = ctk.CTkLabel(self, text="About",font=("JetBrainsMono NF",15,"bold"))
        self.label.pack(pady=20)

        # Create three buttons in the middle
        self.button1 = ctk.CTkButton(self, text="Button 1")
        self.button1.pack(side="left", padx=20)
        self.button2 = ctk.CTkButton(self, text="Button 2")
        self.button2.pack(side="left", padx=20)
        self.button3 = ctk.CTkButton(self, text="Button 3")
        self.button3.pack(side="left", padx=20)

