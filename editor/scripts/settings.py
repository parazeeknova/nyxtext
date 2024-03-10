import tkinter as tk
import customtkinter as ctk
import tkinter.font as tkFont
from text_Area import textarea
from tkinter import colorchooser

class Settings():
    def __init__(self, master):

        self.settings_window = ctk.CTkToplevel(master)
        # self.settings_window.geometry(f"{self.winfo_width()}x{self.winfo_height()}+{self.winfo_x()}+{self.winfo_y()}")
        self.settings_window.title("Settings")
        self.settings_window.geometry("500x500")
        self.settings_window.wm_overrideredirect(True)
        
        # Center the window on the screen
        screen_width = self.settings_window.winfo_screenwidth()
        screen_height = self.settings_window.winfo_screenheight()
        window_width = 400
        window_height = 400
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        self.settings_window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        
        # Create a label for the font settings
        font_label = ctk.CTkLabel(self.settings_window, text="Font Type")
        font_label.place(x=20, y=20) # Position the label on the left side

        # Function to handle font selection
        def on_font_select(font_name):
            print(f"Selected font: {font_name}")
            # Here you would typically update the font of your text area or any other widget
            # For demonstration, we're just printing the selected font

        # Get available fonts
        available_fonts = tkFont.families()

        # Create a variable to store the selected font
        selected_font = tk.StringVar(self.settings_window)
        selected_font.set(available_fonts[0]) # Default to the first font

        # Create the option menu with font options
        font_option_menu = ctk.CTkOptionMenu(self.settings_window, values=available_fonts, variable=selected_font, command=on_font_select)
        font_option_menu.place(x=200, y=20) # Position the option menu to the right of the label
        
        #Create a label for the font size settings
        font_size_label = ctk.CTkLabel(self.settings_window, text="Font Size")
        font_size_label.place(x=20, y=70) # Position the label below the font label

        # Function to handle font size selection
        def on_font_size_select(font_size):
            print(f"Selected font size: {font_size}")
            # Here you would typically update the font size of your text area or any other widget
            # For demonstration, we're just printing the selected font size

# List of font sizes to be displayed in the option menu
        font_sizes = [str(size) for size in range(1, 251)]

        # Create a variable to store the selected font size
        selected_font_size = tk.StringVar(self.settings_window)
        selected_font_size.set(font_sizes[0]) # Default to the first size

        # Create the option menu with font size options
        font_size_option_menu = ctk.CTkComboBox(self.settings_window, values=font_sizes, variable=selected_font_size, command=on_font_size_select)
        font_size_option_menu.place(x=200, y=70) # Position the option menu to the right of the font size label
        
        # Create a label for the font color settings
        font_color_label = ctk.CTkLabel(self.settings_window, text="Font Color")
        font_color_label.place(x=20, y=120) # Position the label below the font size label
        # Function to handle font color selection using color chooser dialog
        def on_font_color_select():
            color_code = colorchooser.askcolor(title="Choose color")
            if color_code[1]: # Check if a color was selected (color_code[1] is not None)
                print(f"Selected font color: {color_code[1]}")
                # Here you would typically update the font color of your text area or any other widget
                # For demonstration, we're just printing the selected font color

        # Create a button to open the color chooser dialog
        font_color_button = ctk.CTkButton(self.settings_window, text="Choose Color", command=on_font_color_select)
        font_color_button.place(x=200, y=120) # Position the button to the right of the font color label
        
        # Create a label for the system theme settings
        system_theme_label = ctk.CTkLabel(self.settings_window, text="System Theme")
        system_theme_label.place(x=20, y=170) # Position the label below the font color label

        # Function to handle system theme selection
        def on_system_theme_select(theme):
            print(f"Selected system theme: {theme}")
            # Here you would typically update the system theme of your application
            # For demonstration, we're just printing the selected theme
        # List of system themes to be displayed in the option menu
        system_themes = ["Dark", "Light", "Kaam "]

        # Create a variable to store the selected system theme
        selected_system_theme = tk.StringVar(self.settings_window)
        selected_system_theme.set(system_themes[0]) # Default to the first theme

        # Create the option menu with system theme options
        system_theme_option_menu = ctk.CTkOptionMenu(self.settings_window, values=system_themes, variable=selected_system_theme, command=on_system_theme_select)
        system_theme_option_menu.place(x=200, y=170) # Position the option menu to the right of the system theme label
        
        # Create a label for the color scheme settings
        color_scheme_label = ctk.CTkLabel(self.settings_window, text="Color Scheme")
        color_scheme_label.place(x=20, y=220) # Position the label below the system theme label

        # Function to handle color scheme selection
        def on_color_scheme_select(color_scheme):
            print(f"Selected color scheme: {color_scheme}")
            # Here you would typically update the color scheme of your application
            # For demonstration, we're just printing the selected color scheme

        # List of color schemes to be displayed in the option menu
        color_schemes = ["Dark Blue", "Blue", "Slate","Lumber","Frappe","Latte","Mocha","Macchito","Oceanic","Blue Green","Jim Jam"]

        # Create a variable to store the selected color scheme
        selected_color_scheme = tk.StringVar(self.settings_window)
        selected_color_scheme.set(color_schemes[0]) # Default to the first scheme

        # Create the option menu with color scheme options
        color_scheme_option_menu = ctk.CTkOptionMenu(self.settings_window, values=color_schemes, variable=selected_color_scheme, command=on_color_scheme_select)
        color_scheme_option_menu.place(x=200, y=220) # Position the option menu to the right of the color scheme label
        
        color_schemes1 = ["Dark Blue", "Blue", "Slate","Lumber","Frappe","Latte","Mocha","Macchito","Oceanic","Blue Green","Jim Jam"]
        
        selected_color_scheme1 = tk.StringVar(self.settings_window)
        selected_color_scheme1.set(color_schemes[0]) # Default to the first scheme
        # Create a label for the CodeSpace color scheme settings
        codespace_color_scheme_label = ctk.CTkLabel(self.settings_window, text="CodeSpace Color Scheme")
        codespace_color_scheme_label.place(x=20, y=270) # Position the label below the color scheme option menu

        # Create the option menu with CodeSpace color scheme options
        codespace_color_scheme_option_menu = ctk.CTkOptionMenu(self.settings_window, values=color_schemes1, variable=selected_color_scheme1, command=on_color_scheme_select)
        codespace_color_scheme_option_menu.place(x=200, y=270) # Position the option menu to the right of the CodeSpace color scheme label
        
        start_button = ctk.CTkButton(self.settings_window, text="OK", command=self.settings_window.destroy, font=("VictorMono Nerd Font", 14))
        start_button.place(x=110 ,y= 320)
        self.settings_window.grab_set()
