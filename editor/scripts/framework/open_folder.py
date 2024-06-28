# Open Folder option in welcome screen :

import os
import tkinter as tk
from tkinter import filedialog

import customtkinter as ctk
class openfolder_window(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.geometry("400x200")
        self.title("New folder")
        if os.name == "nt":
            self.wm_attributes("-topmost", False)
        elif os.name == "posix":
            self.wm_attributes("-type", "splash")

        # Center the window on the screen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = 280
        window_height = 250
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        self.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        self.attributes("-alpha", 0.9)

        self.close_button = ctk.CTkButton(
            self,
            text="X",
            command=self.destroy,
            width=6,
            height=6,
            fg_color="transparent",
            text_color="#ed8796",
        )
        self.close_button.place(x=24, y=1)
        # Create a label for New folder title
        self.openfolder_label = ctk.CTkLabel(
            self,
            text="Folder Options :",
            font=("JetBrainsMono NF", 19, "bold"),
            padx=100,
        )
        self.openfolder_label.pack(side="top", pady=(20, 0))

        self.button_open = ctk.CTkButton(
            self,
            text="Open Folder",
            width=100,
            height=25,
            corner_radius=10,
            command=self.open_folder,
        )
        self.button_open.pack(side="top", pady=5)
        # Buttons
        self.button1 = ctk.CTkButton(
            self, text="New folder in Workspace", width=100, height=25, corner_radius=10
        )
        self.button1.pack(side="top", pady=5)

        self.button2 = ctk.CTkButton(
            self, text="New folder in Codespace", width=100, height=25, corner_radius=10
        )
        self.button2.pack(side="top", pady=5)

        self.button3 = ctk.CTkButton(
            self,
            text="Open folder in Workspace",
            width=100,
            height=25,
            corner_radius=10,
        )
        self.button3.pack(side="top", pady=5)

        self.button4 = ctk.CTkButton(
            self,
            text="Open folder in Codespace",
            width=100,
            height=25,
            corner_radius=10,
        )
        self.button4.pack(side="top", pady=5)

    def open_folder(self):
        self.Folder_path_1 = filedialog.askopenfilename(
            defaultextension=".txt",
            Foldertypes=[("Text Folder", "*.txt"), ("All Folders", "*.*")],
        )
        if self.Folder_path_1:
            with open(self.Folder_path_1, "r") as Folder:
                self.text_Area.text_area.delete(1.0, tk.END)  # Clear the text area
                self.text_Area.text_area.insert(tk.INSERT)
