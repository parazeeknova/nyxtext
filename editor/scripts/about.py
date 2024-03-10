import customtkinter as ctk
import tkinter

class MyWindow(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.geometry("1600x1000")
        self.wm_overrideredirect(True)
        
        # Center the window on the screen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = 600
        window_height = 600
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

        # Create three buttons in the middle
        self.button1 = ctk.CTkButton(self, text="NyxText - Discussions")
        self.button1.pack(side='top', padx=30, pady=10)

        self.button2 = ctk.CTkButton(self, text="Report an Issue")
        self.button2.pack(side='top', padx=30, pady=10)

        self.button3 = ctk.CTkButton(self, text="Github Repo...")
        self.button3.pack(side='top', padx=30, pady=10)

        # Add a label named "Social"
        self.social_label = ctk.CTkLabel(self, text="Social", font=("JetBrainsMono NF", 15, "bold"))
        self.social_label.pack(side='top', pady=10)

        # Add a button with "Discord" written on it
        self.discord_button = ctk.CTkButton(self, text="Discord")
        self.discord_button.pack(side='top', padx=30, pady=10)

        # Add a label with "Text made with love"
        self.love_label = ctk.CTkLabel(self, text="Text made with ❤️....", font=("JetBrainsMono NF", 15, "italic"))
        self.love_label.pack(side='top', pady=10)
