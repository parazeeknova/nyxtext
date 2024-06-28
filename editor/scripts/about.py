import os
import sys
import webbrowser

import customtkinter as ctk
from def_path import resource
from features import FeaturesWindow
from PIL import Image

def_light_image = resource("misc\\logo\\logo.png")
def_dark_image = resource("misc\\logo\\logo.png")


class MyWindow(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.geometry("1600x1000")
        self.wm_overrideredirect(True)

        # Center the window on the screen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = 600
        window_height = 650
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        self.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        self.attributes("-alpha", 0.95)
        # Create a close button with specified width and height
        self.close_button = ctk.CTkButton(
            self,
            text="X",
            command=self.destroy,
            width=20,
            height=20,
            fg_color="transparent",
            text_color="#ed8796",
        )
        # Place the close button at the top right corner
        self.close_button.place(x=window_width - 24, y=10)

        # Create a label with big bold text in the top and middle
        if os.name == "nt":
            self.my_image = ctk.CTkImage(
                light_image=Image.open(def_light_image),
                dark_image=Image.open(def_dark_image),
                size=(400, 200),
            )
            self.welcome_title_text = ctk.CTkLabel(
                self,
                text="",
                image=self.my_image,
                font=("JetBrainsMono NF", 80, "bold"),
                padx=100,
                anchor="center",
            )
            self.welcome_title_text.pack(side="top", pady=(50, 0))

        elif os.name == "posix":
            self.welcome_title_text = ctk.CTkLabel(
                self,
                text="NyxText",
                font=("JetBrainsMono NF", 80, "bold"),
                padx=100,
                anchor="center",
            )
            self.welcome_title_text.pack(side="top", pady=(50, 0))

            welcome_title_desc = ctk.CTkLabel(
                self,
                text="- A Catppuccin based Text Editor",
                font=("JetBrainsMono NF", 20, "italic"),
                padx=100,
                anchor="center",
            )
            welcome_title_desc.pack(side="top")

        # Update Button :
        self.update_button = ctk.CTkButton(
            self,
            text=" ↻ Update ",
            font=("JetBrainsMono NF", 13),
            fg_color="#b7bdf8",
            text_color="#363a4f",
            hover=False,
        )
        self.update_button.pack(side="top", padx=30, pady=(15, 0))
        # Create three buttons in the middle
        self.button1 = ctk.CTkButton(
            self,
            text="NyxText - Discussions",
            font=("JetBrainsMono NF", 13),
            fg_color="transparent",
            text_color="#91d7e3",
        )
        self.button1.pack(side="top", padx=30, pady=(30, 5))

        self.button2 = ctk.CTkButton(
            self,
            text="Report an Issue",
            font=("JetBrainsMono NF", 13),
            fg_color="transparent",
            text_color="#ed8796",
        )
        self.button2.pack(side="top", padx=30, pady=5)

        self.button3 = ctk.CTkButton(
            self,
            text="Github Repository",
            font=("JetBrainsMono NF", 13),
            fg_color="transparent",
            command=self.open_website,
            text_color="#a6da95",
        )
        self.button3.pack(side="top", padx=30, pady=5)

        # Add a label named "Social"
        self.social_label = ctk.CTkLabel(
            self, text="Socials", font=("JetBrainsMono NF", 20, "bold")
        )
        self.social_label.pack(side="top", pady=10)

        # Add a button with "Discord" written on it
        self.discord_button = ctk.CTkButton(
            self,
            text="Discord",
            font=("JetBrainsMono NF", 13),
            fg_color="transparent",
            command=self.discord,
            text_color="#8aadf4",
        )
        self.discord_button.pack(side="top", padx=30, pady=5)

        self.features_button = ctk.CTkButton(
            self,
            text="Features",
            font=("JetBrainsMono NF", 13),
            fg_color="transparent",
            command=self.open_features,
            text_color="#a6da95",
        )
        self.features_button.pack(side="top", padx=30, pady=5)
        # Version Number
        self.build = ctk.CTkLabel(
            self, text="Build: Daily", font=("JetBrainsMono NF", 10, "bold")
        )
        self.build.pack(side="bottom")
        self.version = ctk.CTkLabel(
            self, text="Version: v0.0.5-ɑ", font=("JetBrainsMono NF", 10, "bold")
        )
        self.version.pack(side="bottom")

        # Add a label with "Text made with love"
        self.love_label = ctk.CTkLabel(
            self,
            text="NyxText made with 💖 by NYX",
            font=("JetBrainsMono NF", 12, "italic"),
        )
        self.love_label.pack(side="bottom", pady=10)

    @staticmethod
    def open_website():
        # Open a URL in the default web browser
        webbrowser.open("https://github.com//parazeeknova//nyxtext")

    @staticmethod
    def discord():
        webbrowser.open("https://discord.com/invite/UwmqqXkV")

    def open_features(self):
        features_window = FeaturesWindow(self)
        features_window.mainloop()
