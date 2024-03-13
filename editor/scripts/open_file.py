import customtkinter as ctk
from tkinter import filedialog
import tkinter as tk

class openfile_window(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.geometry("400x200")
        self.title("New File")
        self.wm_attributes('-type', 'splash')
        # Center the window on the screen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = 280
        window_height = 250
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
        self.file_path_label = ctk.CTkLabel(self, text="File Path:", font=('JetBrainsMono NF',13),)
        self.file_path_label.pack(side='top', pady=(10,0)) # Adjust pady as needed
        
        # File Path Entry Box
        self.file_path_entry = ctk.CTkEntry(self, width=300, height=25, corner_radius=10, placeholder_text="Enter file path")
        self.file_path_entry.pack(side='top', pady=(0,10))
        # Open File Button
        self.button_open = ctk.CTkButton(self, text="Open...", width=100, height=25, corner_radius=10, command=self.open_file)
        self.button_open.pack(side="top",pady=5)
        # Buttons
        self.button1 = ctk.CTkButton(self, text="OPen in Workspace", width=100, height=25, corner_radius=10)
        self.button1.pack(side='left', padx=(0,10))
        
        self.button2 = ctk.CTkButton(self, text="Open in Codespace", width=100, height=25, corner_radius=10)
        self.button2.pack(side='left')
        
        
        
    def open_file(self):
        self.file_path_1 = filedialog.askopenfilename(defaultextension=".txt",
                                        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if self.file_path_1:
            with open(self.file_path_1, "r") as file:
                self.text_Area.text_area.delete(1.0, tk.END)  # Clear the text area
                self.text_Area.text_area.insert(tk.INSERT)