# Tab View :

import os
import customtkinter
import pygments.lexers
from chlorophyll import CodeView
from text_Area import textarea
class TabView:
    def __init__(self, right_frame, screen_width, screen_height):
        self.tab_view = customtkinter.CTkTabview(
            right_frame, width=int(screen_width) - 220, height=int(screen_height) - 250
        )
        self.tab_view.grid(row=0, column=0, pady=10, sticky="nsew")
        self.tab_count = 0
        self.codespace_count = 0

    def add_new_workspace(self):
        self.tab_count += 1
        tab_title = f"Workspace {self.tab_count}"
        new_tab = self.tab_view.add(tab_title)
        text_area = textarea(new_tab)
        return new_tab

    def add_new_codespace(self):
        self.codespace_count += 1
        codespace_title = f"CodeSpace {self.codespace_count}"
        new_codespace = self.tab_view.add(codespace_title)
        codespace = CodeView(
            new_codespace, lexer=pygments.lexers.PythonLexer, color_scheme="dracula"
        )
        codespace.pack(fill="both", expand=True)
        return new_codespace

    def remove_current_tab(self):
        selected_tab = self.tab_view.get()
        if selected_tab:
            self.tab_view.delete(selected_tab)

    def select_current_tab(self):
        selected_tab = self.tab_view.get()
        return selected_tab
    
    def add_new_workspace_with_file(self, filepath):
      self.tab_count += 1
      tab_title = os.path.basename(filepath)
      new_tab = self.tab_view.add(tab_title)
      text_area = textarea(new_tab)
      file_content = self.read_file_content(filepath)
      text_area.insert('1.0', file_content)
      return new_tab

    def read_file_content(self, filepath):
      with open(filepath, 'r') as file:
        content = file.read()
      return content
