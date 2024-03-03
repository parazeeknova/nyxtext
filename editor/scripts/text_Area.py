import customtkinter as ctk
import tkinter as tk
import tkinter.font as tkFont
class textarea():
    def __init__(self, parent_frame, screen_width, rf, screen_height):
        self.parent_frame = parent_frame
        self.screen_width = screen_width
        self.rf = rf
        self.text_area = ctk.CTkTextbox(parent_frame, height= screen_height-20, width = rf, activate_scrollbars = True, wrap = 'none')
        self.text_area.grid(row = 0, column = 1, sticky = 'nsew')
        self.text_area.configure(padx = 10, pady = 10,takefocus = True)
        # Set default font
        
    def set_font(self, font_name):
        font = ctk.CTkFont(family=font_name, size=12)
        self.text_area.configure(font=font)
        self.text_area.update()