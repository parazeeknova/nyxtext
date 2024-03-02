import tkinter as tk
import customtkinter as ctk
import tkinter.font as tkFont
from text_Area import textarea

class Settings():
    def __init__(self, master, textarea_instance):
        self.settings_window = ctk.CTkToplevel(master)
        self.settings_window.title("Settings")
        self.settings_window.geometry("500x500")

        # Create a label for the font settings
        font_label = ctk.CTkLabel(self.settings_window, text="Font")
        font_label.pack(side='left', fill='x', expand=True)

        # Function to handle font selection
        def on_font_select(font_name):
            # ctk.set_widget_font(family=font_name, size=12)
            print(f"Selected font: {font_name}")
            textarea_instance.set_font(font_name)

        # Get available fonts
        available_fonts = tkFont.families()

        # Create a variable to store the selected font
        selected_font = tk.StringVar(self.settings_window)
        selected_font.set(available_fonts[0])  # Default to the first font

        # Create the option menu with font options
        font_option_menu = ctk.CTkOptionMenu(self.settings_window, values=available_fonts, variable=selected_font, command=on_font_select)
        font_option_menu.pack(side='left', fill='x', expand=True)

# # Example usage

# text_area = textarea(self)
# text_area.pack(expand=True, fill='both')

# settings = Settings(root, text_area)
# settings.settings_window.focus()

