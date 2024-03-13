import customtkinter
import tkinter as tk
import os
from text_Area import textarea
from chlorophyll import CodeView
import pygments.lexers

class TabView:
    def __init__(self, right_frame, screen_width, screen_height):
        self.tab_view = customtkinter.CTkTabview(right_frame, width=int(screen_width)-250, height=int(screen_height)-200)
        self.tab_view.grid(row=0, column=0, pady=10, sticky='nsew')
        self.tab_count = 0
        self.codespace_count = 0

    def add_new_tab(self):
        self.tab_count += 1
        tab_title = f"Workspace {self.tab_count}"
        new_tab = self.tab_view.add(tab_title)
        text_area = textarea(new_tab)
        return new_tab

    def add_new_codespace(self):
        self.codespace_count += 1
        codespace_title = f"CodeSpace {self.codespace_count}"
        new_codespace = self.tab_view.add(codespace_title)
        codespace = CodeView(new_codespace, lexer=pygments.lexers.PythonLexer, color_scheme="dracula")
        codespace.pack(fill="both", expand=True)
        return new_codespace

    def remove_current_tab(self):
        selected_tab = self.tab_view.get()
        if selected_tab:
            self.tab_view.delete(selected_tab)