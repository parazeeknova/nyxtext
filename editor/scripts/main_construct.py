# Main system construct file aka entry point for the Editor to start
# System imports here
import os
import webbrowser

# File imports here
from about import MyWindow

# Third party imports here
from customtkinter import *
from def_path import resource
from external.CTkScrollableDropdown import *
from CTkToolTip import *
from framework.codespace import Codespace

# Packages
from framework.tab_View import TabView
from framework.welcome_Screen import WelcomeScreen
from framework.workspace import Workspace
from hPyT import *
from menu_Bar import Menubar
from pywinstyles import *

# Function import here
from framework.file_Tree import treeView
from settings import Settings
from text_Area import textarea
from tkterm import Terminal

set_appearance_mode("dark")  # Global default theme (default = dark)

theme_names = [  # Assets and color themes for the editor
    "frappe",
    "latte",
    "macchiato",
    "mocha",
    "H2O",
    "oceanic",
    "slate",
    "lumber"
]

themes = {
    name: resource(os.path.join("color_themes", f"{name}.json")) for name in theme_names
}
icon = resource("misc\\icons\\icon.ico")  # Icon for the editor
def_folder_image = resource("misc\\icons\\folder.png")  # Folder icon for the editor
def_file_image = resource("misc\\icons\\file.png")  # File icon for the editor

class sysUI(CTk):
    def __init__(self, master):
        super().__init__(master=master)

    def change_theme(theme_name):
        if theme_name in themes:
            set_default_color_theme(themes[theme_name])
        else:
            print(f"Theme '{theme_name}' not found.")


class Nyxtext(CTk):
    def __init__(self):
        super().__init__()

        self.geometry(f"{800}x{600}")
        self.title("Nyxtext")
        sysUI.change_theme("frappe")  # Default color scheme is frappe for now

        # Configure grid rows
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=2)
        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=2)
        self.rowconfigure(2, weight=1)

        if os.name == "nt":  # Setting OS specific settings for the editor
            apply_style(self, "aero")
            change_border_color(
                self, color=get_accent_color()
            )  # Change border color to accent color
            change_header_color(
                self, color=get_accent_color()
            )  # Change header color to accent color
            self.iconbitmap(icon)  # Set the icon for the editor
            menubar = Menubar(self)
        elif os.name == "posix":
            menubar = Menubar(self)

        screen_width = self.winfo_screenwidth()  # Calculate the screen width and height
        screen_height = self.winfo_screenheight()
        self.screen_width = int(screen_width)
        self.screen_height = int(screen_height)

        self.create_frames()  # Create the frames for the editor
        self.right_frame.grid_rowconfigure(0, weight=1)
        self.right_frame.grid_columnconfigure(0, weight=2)

        self.terminal_frame.grid_remove()  # Hide the terminal frame for the editor
        self.terminal = Terminal(self.terminal_frame)  # Create the terminal for the editor
        self.terminal.shell = True
        self.terminal.linebar = True
        self.terminal.pack(fill="both", expand=True)


        self.tabview = TabView(
            self.right_frame, screen_width, screen_height
        )  # Create the tab view for the editor
        self.welcomeTab = WelcomeScreen(
            self.tabview.tab_view
        )  # Create the welcome screen for the editor
        self.workspace = Workspace(
            self.tabview.tab_view
        )  # Create the workspace for the editor
        self.codespace = Codespace(
            self.tabview.tab_view
        )  # Create the codespace for the editor

        bg_color_tree = self._apply_appearance_mode(ThemeManager.theme["CTkFrame"]["fg_color"]) # Treeview (theme colors are selected)
        selected_color_tree = self._apply_appearance_mode(ThemeManager.theme["CTkButton"]["fg_color"])

        self.treeView = treeView(
            self.left_frame,bg_color_tree,selected_color_tree,def_folder_image,def_file_image
        )  # Create the tree view for the editor

        self.settings_button = CTkButton(self.top_frame, text="⚙️", command=self.open_settings_window)
        self.settings_button.pack(side="right", padx=5, pady=2)
        self.settings_button.configure(width=10)

        self.terminal_button = CTkButton(self.top_frame, text="⋕", command=lambda: self.toggle_frame(self.terminal_frame))
        self.terminal_button.configure(width=5)
        self.terminal_button.pack(side="right", padx=5, pady=2)

        self.filetree_button = CTkButton(self.top_frame, text="◧", command=lambda: self.toggle_frame(self.left_frame))
        self.filetree_button.configure(width=5)
        self.filetree_button.pack(side="right", padx=5, pady=2)

        self.bottomframe_button = CTkButton(self.top_frame, text="⬓", command=lambda: self.toggle_frame(self.bottom_frame))
        self.bottomframe_button.configure(width=5)
        self.bottomframe_button.pack(side="right", padx=5, pady=2)

        appearance_optionmenu = CTkOptionMenu( 
            self.top_frame,
            values=["◑"],
            width=2
        )
        appearance_optionmenu.pack(side="right", padx=2, pady=2)
        CTkScrollableDropdown(appearance_optionmenu,
                              values=["Light","Dark"],
                              command=self.change_appearance_mode_event,
                              width=100,
                              alpha=0.5,
                              frame_border_width=0,
                              scrollbar=False
        )

        self.seperator(self.top_frame,"right")

        self.remove_current_tab = CTkButton(self.top_frame, text="✕", command=self.tabview.remove_current_tab)
        self.remove_current_tab.configure(width=5)
        self.remove_current_tab.pack(side="right", padx=5, pady=2)

        self.add_new_tab = CTkButton(self.top_frame, text="⌂", command=self.tabview.add_new_workspace)
        self.add_new_tab.configure(width=5)
        self.add_new_tab.pack(side="right", padx=5, pady=2)

        self.add_new_codespace = CTkButton(self.top_frame, text="⋊", command=self.tabview.add_new_codespace)
        self.add_new_codespace.configure(width=5)
        self.add_new_codespace.pack(side="right", padx=5, pady=2)

        self.seperator(self.top_frame,"right")        

        self.remove_top_frame = CTkButton(self.bottom_frame, text="⬒", command=lambda: self.toggle_frame(self.top_frame))
        self.remove_top_frame.configure(width=5)
        self.remove_top_frame.pack(side="left", padx=5, pady=2)

        current_dir_path = os.path.dirname(os.path.realpath(__file__))
        directory_label = CTkLabel(self.bottom_frame, text=current_dir_path)
        directory_label.pack(side="left", padx=10, pady=2)
        directory_label.configure(width=100, font=("JetBrainsMono Nerd Font", 12, "bold"), fg_color=f"{ThemeManager.theme['CTkLabel']['fg_color']}")

        tooltips = [ # Tooltips for the editor 
          (appearance_optionmenu, "Dark / Light switch"),
          (self.settings_button, "Settings"),
          (self.terminal_button, "Terminal"),
          (self.filetree_button, "Toggle Filetree"),
          (self.add_new_tab, "Add new workspace"),
          (self.add_new_codespace, "Add new codespace"),
          (self.remove_current_tab, "Remove current tab"),
          (self.remove_top_frame, "Toggle Toolbar"),
          (self.bottomframe_button, "Toggle Status bar"),
        ]

        for widget, text in tooltips:
          CTkToolTip(widget, text, alpha=0.7)

        # Always keep this at the end of the constructor to prevent widgets being hidden
        for frame in [ # Set the opacity for the frames for the editor
            self.top_frame,
            self.left_frame,
            self.right_frame,
            self.bottom_frame,
        ]:
            set_opacity(frame, value=0.6)

        # Frame specific opacity
        set_opacity(self.terminal_frame, value=1.0)  # Set the opacity for the terminal frame for the editor

        self.update()  # Update the editor
        self.update_idletasks()  # Update the editor

    def create_frames(self):  # Skeleton for the editor
        self.top_frame = self.create_frame(
            height=self.screen_height * 0.05,
            width=self.screen_width,
            grid_config={"row": 0, "column": 0, "columnspan": 2},
        )
        self.left_frame = self.create_frame(
            width=self.screen_width * 0.15,
            height=self.screen_height,
            grid_config={"row": 1, "column": 0, "rowspan": 1},
        )
        self.right_frame = self.create_frame(
            width=self.screen_width * 0.8,
            height=self.screen_height,
            grid_config={"row": 1, "column": 1, "rowspan": 1},
            corner_radius=1,
        )
        self.bottom_frame = self.create_frame(
            height=self.screen_height * 0.05,
            width=self.screen_width,
            grid_config={"row": 2, "column": 0, "columnspan": 2},
        )

        self.terminal_frame = self.create_frame(
            height=self.screen_height * 0.15,
            width=self.screen_width,
            corner_radius=0,
            grid_config={"row": 3, "column": 0, "columnspan": 2},
        )
        self.ai_frame = self.create_frame(
            width=self.screen_width,
            height=self.screen_height,
            corner_radius=0,
            grid_config={"row": 0, "column": 2, "rowspan": 3, "columnspan": 2},
        ).grid_remove()

    def create_frame(self, width, height, grid_config={}, corner_radius=0):
        frame = CTkFrame(self, width=width, height=height, corner_radius=corner_radius)
        frame.grid(
            row=grid_config.get("row"),
            column=grid_config.get("column"),
            rowspan=grid_config.get("rowspan", 1),
            columnspan=grid_config.get("columnspan", 1),
            sticky="nsew",
        )
        return frame

    def open_settings_window(self):
        self.settings = Settings(self)
    
    def change_appearance_mode_event(self,new_appearance_mode: str):
        set_appearance_mode(new_appearance_mode)
    
    def seperator(self,frame,side) -> None:
        seperator = CTkLabel(frame, text="|")
        seperator.pack(side=f"{side}", padx=4, pady=2)
        seperator.configure(width=2, font=("Arial", 16, "bold"), fg_color="transparent")

    def toggle_frame(self, frame):
        if frame.winfo_viewable():
            frame.grid_remove()
            self.update_idletasks()
        else:
            frame.grid()
            self.update_idletasks()

# Main function to start the editor
if __name__ == "__main__":
    editor = Nyxtext()
    editor.mainloop()
