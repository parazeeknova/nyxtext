# Main system construct file aka entry point for the Editor to start
# System imports here
import os

# File imports here
from about import MyWindow

# Third party imports here
from customtkinter import *
from def_path import resource
from external.CTkScrollableDropdown import *
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
        self.settings_button.configure(fg_color="transparent", width=10)

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

        # Always keep this at the end of the constructor to prevent widgets being hidden
        for frame in [ # Set the opacity for the frames for the editor
            self.top_frame,
            self.left_frame,
            self.right_frame,
            self.bottom_frame,
        ]:
            set_opacity(frame, value=0.6)

    def create_frames(self):  # Skeleton for the editor
        self.top_frame = self.create_frame(
            height=self.screen_height * 0.05,
            width=self.screen_width,
            grid_config={"row": 0, "column": 0, "columnspan": 2},
        )
        self.left_frame = self.create_frame(
            width=self.screen_width * 0.15,
            height=self.screen_height,
            grid_config={"row": 1, "column": 0, "rowspan": 4},
        )
        self.right_frame = self.create_frame(
            width=self.screen_width * 0.8,
            height=self.screen_height,
            grid_config={"row": 1, "column": 1},
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
        ).grid_remove()
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
    
    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        set_widget_scaling(new_scaling_float)

# Main function to start the editor
if __name__ == "__main__":
    editor = Nyxtext()
    editor.mainloop()
