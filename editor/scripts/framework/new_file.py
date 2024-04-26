# New File option in Welcome Screen :

import os

import customtkinter as ctk


class newfile_window(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("New File options: ")
        if os.name == "nt":
            self.wm_attributes("-topmost", True)
        elif os.name == "posix":
            self.wm_attributes("-type", "splash")

        # Center the window on the screen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = 350
        window_height = 200
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        self.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        self.attributes("-alpha", 0.95)

        # Design Asthetics :
        self.label_plus = ctk.CTkLabel(
            self, text="▲", font=("JetBrainsMono NF", 40), text_color="#ed8796"
        )
        self.label_plus.pack(side="top", pady=(10, 0), anchor="center")

        self.label_new = ctk.CTkLabel(
            self,
            text="New File",
            font=("JetBrainsMono NF", 20, "bold"),
            text_color="#ed8796",
        )
        self.label_new.pack(side="top", anchor="center")

        self.label_sep = ctk.CTkLabel(
            self,
            text="------",
            font=("JetBrainsMono NF", 20, "bold"),
            text_color="#8aadf4",
        )
        self.label_sep.pack(side="top", anchor="center")

        def new_des() -> None:
            self.after(250, self.destroy)

        # Buttons
        self.button_work = ctk.CTkButton(
            self,
            text="New File in Workspace",
            width=100,
            height=25,
            corner_radius=5,
            text_color="#8aadf4",
            command=new_des,
        )
        self.button_work.pack(side="bottom", pady=5)

        self.button_cod = ctk.CTkButton(
            self,
            text="New File in Codespace",
            width=100,
            height=25,
            corner_radius=5,
            text_color="#91d7e3",
            command=new_des,
        )
        self.button_cod.pack(side="bottom", pady=5)
