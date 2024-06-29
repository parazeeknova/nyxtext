import os

from CTkMenuBar import *


class Menubar:
    def __init__(self, root):
        if os.name == "nt":
            self.menubar = CTkTitleMenu(root)
        elif os.name == "posix":
            self.menubar = CTkMenuBar(root)

        # Title bar menus
        self.file_menu = self.menubar.add_cascade("File")
        self.edit_menu = self.menubar.add_cascade("Edit")
        self.Search_menu = self.menubar.add_cascade("Search")
        self.view_menu = self.menubar.add_cascade("View")
        self.run_menu = self.menubar.add_cascade("Run")
        self.help_menu = self.menubar.add_cascade("Help")

        self.file_menu_drop = CustomDropdownMenu(widget=self.file_menu)
        self.file_menu_drop.add_option(option="Open   Ctrl+O").configure(
            font=("JetBrainsMono Nerd Font", 12, "bold")
        )
        self.file_menu_drop.add_option(option="New    Ctrl+N").configure(
            font=("JetBrainsMono Nerd Font", 12, "bold")
        )
        self.file_menu_drop.add_separator()
        self.file_menu_drop.add_option(option="Save   Ctrl+S").configure(
            font=("JetBrainsMono Nerd Font", 12, "bold")
        )
        self.file_menu_drop.add_option(option="Save As   Ctrl+Shift+S").configure(
            font=("JetBrainsMono Nerd Font", 12, "bold")
        )
        self.file_menu_drop.add_separator()
        self.file_menu_drop.add_option(option="Close   Ctrl+W").configure(
            font=("JetBrainsMono Nerd Font", 12, "bold"), hover_color="#ed8796"
        )
        self.file_menu_drop.add_option(option="Exit   Ctrl+Q").configure(
            font=("JetBrainsMono Nerd Font", 12, "bold"), hover_color="#ed8796"
        )

        self.edit_menu_drop = CustomDropdownMenu(widget=self.edit_menu)
        self.edit_menu_drop.add_option(option="Undo  Ctrl+Z").configure(
            font=("JetBrainsMono Nerd Font", 12, "bold")
        )
        self.edit_menu_drop.add_option(option="Redo  Ctrl+Y").configure(
            font=("JetBrainsMono Nerd Font", 12, "bold")
        )
        self.edit_menu_drop.add_separator()
        self.edit_menu_drop.add_option(option="Cut   Ctrl+X").configure(
            font=("JetBrainsMono Nerd Font", 12, "bold")
        )
        self.edit_menu_drop.add_option(option="Copy  Ctrl+C").configure(
            font=("JetBrainsMono Nerd Font", 12, "bold")
        )
        self.edit_menu_drop.add_option(option="Paste  Ctrl+V").configure(
            font=("JetBrainsMono Nerd Font", 12, "bold")
        )
        self.edit_menu_drop.add_separator()
        self.edit_menu_drop.add_option(option="Delete  Del").configure(
            font=("JetBrainsMono Nerd Font", 12, "bold"), hover_color="#ed8796"
        )

        self.Search_menu_drop = CustomDropdownMenu(widget=self.Search_menu)
        self.Search_menu_drop.add_option(option="Find Ctrl+F").configure(
            font=("JetBrainsMono Nerd Font", 12, "bold")
        )
        self.Search_menu_drop.add_option(option="Find Next  Ctrl+G").configure(
            font=("JetBrainsMono Nerd Font", 12, "bold")
        )
        self.Search_menu_drop.add_option(
            option="Find Previous  Ctrl+Shift+G"
        ).configure(font=("JetBrainsMono Nerd Font", 12, "bold"))
        self.Search_menu_drop.add_separator()
        self.Search_menu_drop.add_option(option="Replace  Ctrl+H").configure(
            font=("JetBrainsMono Nerd Font", 12, "bold")
        )
        self.Search_menu_drop.add_option(option="Go To  Ctrl+J").configure(
            font=("JetBrainsMono Nerd Font", 12, "bold")
        )
        self.Search_menu_drop.add_option(option="Select All  Ctrl+A").configure(
            font=("JetBrainsMono Nerd Font", 12, "bold")
        )
        self.Search_menu_drop.add_option(option="Select None  Ctrl+Shift+A").configure(
            font=("JetBrainsMono Nerd Font", 12, "bold")
        )

        self.view_menu_drop = CustomDropdownMenu(widget=self.view_menu)
        self.view_menu_drop.add_option(option="Status Bar  Ctrl+Shift+B").configure(
            font=("JetBrainsMono Nerd Font", 12, "bold")
        )
        self.view_menu_drop.add_option(option="Tool Bar  Ctrl+Shift+T").configure(
            font=("JetBrainsMono Nerd Font", 12, "bold")
        )
        self.view_menu_drop.add_option(option="Full Screen  Ctrl+Shift+F").configure(
            font=("JetBrainsMono Nerd Font", 12, "bold")
        )
        self.view_menu_drop.add_option(option="Zoom In  Ctrl+Shift+Plus").configure(
            font=("JetBrainsMono Nerd Font", 12, "bold")
        )
        self.view_menu_drop.add_option(option="Zoom Out   Ctrl+Shift+Minus").configure(
            font=("JetBrainsMono Nerd Font", 12, "bold")
        )

        self.run_menu_drop = CustomDropdownMenu(widget=self.run_menu)
        self.run_menu_drop.add_option(option="Run  Ctrl+R").configure(
            font=("JetBrainsMono Nerd Font", 12, "bold")
        )
        self.run_menu_drop.add_option(option="Run All  Ctrl+Shift+R").configure(
            font=("JetBrainsMono Nerd Font", 12, "bold")
        )
        self.run_menu_drop.add_separator()
        self.run_menu_drop.add_option(option="Terminal Ctrl+T").configure(
            font=("JetBrainsMono Nerd Font", 12, "bold")
        )

        self.help_menu_drop = CustomDropdownMenu(widget=self.help_menu)
        self.help_menu_drop.add_option(option="About").configure(
            font=("JetBrainsMono Nerd Font", 12, "bold")
        )
        self.help_menu_drop.add_option(option="Help").configure(
            font=("JetBrainsMono Nerd Font", 12, "bold")
        )
        self.help_menu_drop.add_option(option="Github").configure(
            font=("JetBrainsMono Nerd Font", 12, "bold")
        )
        self.help_menu_drop.add_option(option="Documentation").configure(
            font=("JetBrainsMono Nerd Font", 12, "bold")
        )
        self.help_menu_drop.add_option(option="License").configure(
            font=("JetBrainsMono Nerd Font", 12, "bold")
        )
        self.help_menu_drop.add_option(option="Changelog").configure(
            font=("JetBrainsMono Nerd Font", 12, "bold")
        )
