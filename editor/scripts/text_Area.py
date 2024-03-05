import customtkinter as ctk

from tkinter import *
from collections import deque

class textarea():
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        # Inside the textarea class, after creating the text_area
        self.parent_frame.grid_rowconfigure(0, weight=1)
        self.parent_frame.grid_columnconfigure(0, weight=1)

        self.text_area = ctk.CTkTextbox(parent_frame, height=1, width =1, font=("JetbrainsMono NF", 16,),activate_scrollbars = True, wrap = 'none')
        self.text_area.grid(row = 0, column = 0, sticky = 'nsew')
        self.text_area.configure(padx = 10, pady = 10,takefocus = True)
        
        # Would help in redo and undo
        # self.stack = deque(maxlen = 10)
        # self.stackcursor = 0 