# New File option in Welcome Screen : 

import customtkinter as ctk
import os
class newfile_window(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.geometry("400x200")
        self.title("New File")
        if os.name == 'nt': 
                self.wm_attributes('-topmost', False)
        elif os.name=="posix":
            self.wm_attributes('-type','splash')
        # Center the window on the screen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = 310
        window_height = 150
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        self.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        self.attributes('-alpha', 0.95)
        # Close Button
        self.close_button = ctk.CTkButton(self, text="X", command=self.destroy, width=6, height=6, fg_color='transparent', text_color='#ed8796')
        self.close_button.place(x=window_width - 24, y=1)
        # Create a label for New file title
        self.newfile_label = ctk.CTkLabel(self, text="New File Options :",font=("JetBrainsMono NF", 19, "bold"), padx=100,)
        self.newfile_label.pack(side='top', pady=(20,0))
        
        # File Path Label
        # Buttons
        self.button1 = ctk.CTkButton(self, text="New File in Workspace", width=100, height=25, corner_radius=10)
        self.button1.pack(side='left', padx=(0,10))
        
        self.button2 = ctk.CTkButton(self, text="New File in Codespace", width=100, height=25, corner_radius=10)
        self.button2.pack(side='left')
        
        