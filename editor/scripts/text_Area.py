import customtkinter as ctk

from tkinter import *
from collections import deque

class textarea():
    def __init__(self, parent_frame, screen_width, rf, screen_height):
        self.parent_frame = parent_frame
        self.screen_width = screen_width
        self.rf = rf
        self.text_area = ctk.CTkTextbox(parent_frame, height= screen_height-20, width = rf, font=("JetbrainsMono NF", 16,),activate_scrollbars = True, wrap = 'none')
        self.text_area.grid(row = 0, column = 1, sticky = 'nsew')
        self.text_area.configure(padx = 10, pady = 10,takefocus = True)
        
        # Would help in redo and undo
        # self.stack = deque(maxlen = 10)
        # self.stackcursor = 0 