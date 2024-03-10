import customtkinter as ctk
import tkinter

class MyWindow(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.geometry("600x500")
        self.wm_overrideredirect(True)
        
        # Center the window on the screen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = 600
        window_height = 400
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        self.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        
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
        self.button_close = ctk.CTkButton(self, text="OK", command=self.destroy)
        self.button_close.place(x=200,y=400) # Adjust x and y as needed
        self.button1 = ctk.CTkButton(self, text="Button 1")
        self.button1.pack(side='left', padx=50, pady=20)

        self.button2 = ctk.CTkButton(self, text="Button 2")
        self.button2.pack(side='left', padx=50, pady=20)

        self.button3 = ctk.CTkButton(self, text="Button 3")
        self.button3.pack(side='left', padx=50, pady=20)


