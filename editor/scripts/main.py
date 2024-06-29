# System imports here
import os
import threading
import webbrowser
from tkinter import PhotoImage, filedialog, ttk

# Third party imports here
import customtkinter
import vertexai
import vertexai.preview.generative_models as generative_models

# File imports here
from about import MyWindow
from def_path import resource
from framework.codespace import Codespace

# Packages
from framework.tab_View import TabView
from framework.welcome_Screen import WelcomeScreen
from framework.workspace import Workspace
from hPyT import *
from menu_Bar import Menubar
from pywinstyles import *

# Function import here
from settings import Settings
from text_Area import textarea
from tkterm import Terminal
from vertexai.generative_models import FinishReason, GenerativeModel, Part

# Sets (for now the appearance to light and color scheme to blue)
customtkinter.set_appearance_mode("dark")
# Sets the color theme
current_theme = resource("color_themes\\frappe.json")
# Should be replaced with a function in future for catppuccin color scheme
customtkinter.set_default_color_theme("blue")


# Welcome screen for the text editor disabled because currently a mess
# Need to work on this mess in future
def show_welcome_window(root):
    welcome_window = customtkinter.CTkToplevel(root)
    # Relative window centre position
    window_frame.center_relative(welcome_window, root)
    welcome_window.title("Welcome to NyxText")
    welcome_window.geometry(f"{1100}x{580}")
    welcome_window.wm_overrideredirect(True)
    welcome_window.grab_set()
    welcome_label = customtkinter.CTkLabel(
        welcome_window,
        text="Welcome to NyxText, your advanced text editor!\n\nClick 'Start' to proceed.",
        font=("VictorMono Nerd Font", 14),
    )
    welcome_label.pack(pady=50)
    # Button to destroy the window
    start_button = customtkinter.CTkButton(
        welcome_window,
        text="Start",
        command=welcome_window.destroy,
        font=("VictorMono Nerd Font", 14),
    )
    start_button.pack(pady=10)


# This defines the main function, which is the entry point of the application
def main():
    global root
    root = customtkinter.CTk()
    root.geometry(f"{1100}x{580}")
    root.title("NyxText")

    # configure grid layout (4x4)
    # Useful for responsiveness
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=2)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    # Menu bar in the title bar for windows also this is the icon for the application.
    icon = resource("misc\\icons\\icon.ico")
    if os.name == "nt":  # for Windows
        # Pywinstyles for theming
        apply_style(root, "aero")
        change_border_color(
            root, color=get_accent_color()
        )  # Change the border color to the accent color
        change_header_color(
            root, color=get_accent_color()
        )  # Change the header color to the accent color
        root.iconbitmap(icon)
        menu_bar = Menubar(root)
    elif os.name == "posix":  # for Linux and MacOS
        # root.iconphoto(False, PhotoImage(file="editor/scripts/misc/icons/icon.png"))
        pass

    # Setting width variables
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Frames for the main text editor
    top_frame = customtkinter.CTkFrame(
        root, width=screen_width, height=int(screen_height * 0.15), corner_radius=0
    )  # Adjust height as needed
    top_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")

    left_frame = customtkinter.CTkFrame(
        root, width=screen_width * 0.16, corner_radius=0
    )
    left_frame.grid(row=1, column=0, rowspan=4, sticky="nsew")

    right_frame = customtkinter.CTkFrame(
        root,
        width=int(screen_width) - 100,
        height=int(screen_height) - 30,
        corner_radius=1,
    )
    right_frame.grid(row=1, column=1, sticky="nsew")

    bottom_frame = customtkinter.CTkFrame(
        root, width=screen_width, height=int(screen_height * 0.15), corner_radius=0
    )
    bottom_frame.grid(row=2, column=0, columnspan=2, sticky="nsew")

    right_frame.grid_rowconfigure(0, weight=1)
    right_frame.grid_columnconfigure(0, weight=2)

    # Create a toggable more_bottom_frame for terminal and other features
    def toggle_more_bottom_frame():
        if more_bottom_frame.winfo_viewable():
            more_bottom_frame.grid_remove()
        else:
            more_bottom_frame.grid()

    def toggle_left_frame():
        if left_frame.winfo_viewable():
            left_frame.grid_remove()
        else:
            left_frame.grid()

    def toggle_ai_bottom_frame():
        if ai_bottom_frame.winfo_viewable():
            ai_bottom_frame.grid_remove()
        else:
            ai_bottom_frame.grid()

    more_bottom_frame = customtkinter.CTkFrame(
        root, width=screen_width, height=int(screen_height * 0.15), corner_radius=0
    )
    more_bottom_frame.grid(row=3, column=0, columnspan=2, sticky="nsew")

    ai_bottom_frame = customtkinter.CTkFrame(
        root, width=int(screen_width), height=int(screen_height), corner_radius=0
    )
    ai_bottom_frame.grid(row=0, column=3, columnspan=2, rowspan=3, sticky="nsew")

    toggle_button = customtkinter.CTkButton(
        bottom_frame, text="Terminal", width=5, command=toggle_more_bottom_frame
    )
    toggle_button.pack(side="right", padx=2, pady=10)
    more_bottom_frame.grid_remove()

    toggle_left_frame_button = customtkinter.CTkButton(
        top_frame, text="Toggle FileTree", width=5, command=toggle_left_frame
    )
    toggle_left_frame_button.pack(side="right", padx=2, pady=10)

    def combined_op():
        toggle_ai_bottom_frame()
        toggle_left_frame()

    toggle_ai_bottom_frame_button = customtkinter.CTkButton(
        bottom_frame, text="AI", width=5, command=combined_op
    )
    toggle_ai_bottom_frame_button.pack(side="right", padx=2, pady=10)
    ai_bottom_frame.grid_remove()

    # Terminal :
    terminal = Terminal(more_bottom_frame)
    terminal.shell = True
    terminal.linebar = True
    terminal.pack(expand=True, fill="both")

    # Creates a tab view to show tabs, implimented the dynamic tab view for the workspace (Text Area) :
    # Uses framework package to create the tab view
    tab_view = TabView(right_frame, screen_width, screen_height)

    # Welcome tab from the welcome_Screen.py file in framework folder which is a package now
    welcome_tab = WelcomeScreen(tab_view.tab_view)

    # Workspace creates a Default text area for text editing:
    # All functions of the menu bar works on this tab, NEED TO FIX AND MAKE THE FUNCTIONS TO WORK ON SELECTED TAB !!
    tab_init = Workspace(tab_view.tab_view)

    # Codespace creates a DEfault code area for code editing:
    # Gives the ability for syntax Highlighting
    Codeview = Codespace(tab_view.tab_view)

    # All Items for the left frame are below :
    Filetree_Button = customtkinter.CTkLabel(
        left_frame, text="FileTree :", font=("VictorMono Nerd Font", 14, "bold")
    )
    Filetree_Button.grid(row=0, column=0, pady=5, sticky="nsew")
    Filetree_Button.configure(width=2)

    # Preparing images for the file tree
    # Commented for better version in future
    def_folder_image = resource("misc\\icons\\folder.png")
    folder_image = PhotoImage(file=def_folder_image)
    folder_path = folder_image

    def_file_image = resource("misc\\icons\\file.png")
    file_image = PhotoImage(file=def_file_image)
    file_path = file_image

    # Inside the main function, after creating the left_frame
    file_tree = ttk.Treeview(left_frame, height=35)
    file_tree.heading("#0", text="Files :", anchor="w")
    file_tree.grid(row=1, column=0, sticky="nsew")

    # Function to put items in the file tree :
    def populate_file_tree(tree, path):
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                # Insert the directory into the tree and get its ID
                dir_id = tree.insert("", "end", text=item, open=True, image=folder_path)
                # Recursively populate the directory
                populate_file_tree(tree, item_path)
            else:
                # Insert the file into the tree using the parent directory's ID
                dir_id = tree.insert("", "end", text=item, open=True)
                tree.insert(dir_id, "end", text=item, image=file_path)

    def open_directory_dialog():
        directory_path = filedialog.askdirectory()
        if directory_path:
            # Clear the current file tree
            for item in file_tree.get_children():
                file_tree.delete(item)
        # Populate the file tree with the selected directory
        populate_file_tree(file_tree, directory_path)

    # Styling the Treeview to look dark
    style = ttk.Style()
    style.configure("Treeview", background="#51576d", foreground="#fff")
    style.configure("Treeview.Heading", background="#51576d", foreground="#fff")

    # Customizing the appearance of selected items and lines
    style.map(
        "Treeview", background=[("selected", "#555")], foreground=[("selected", "#fff")]
    )

    # Bydefault populate the file tree with the desktop directory
    # desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    current_directory_path = os.getcwd()
    populate_file_tree(file_tree, current_directory_path)

    # Add a button to open the directory dialog
    open_directory_button = customtkinter.CTkButton(
        left_frame, text="Open Directory", command=open_directory_dialog
    )
    open_directory_button.grid(row=2, column=0, pady=5, sticky="nsew")

    def new_instance_window():
        pass

    open_new_window = customtkinter.CTkButton(
        left_frame, text="Open New Window", command=new_instance_window
    )
    open_new_window.grid(row=3, column=0, pady=5, sticky="nsew")

    # All buttons and search bar in the top frame for different functions (Right)
    def open_settings_window():
        settings = Settings(root)

    settings_button = customtkinter.CTkButton(
        top_frame, text="⚙️", command=open_settings_window
    )
    settings_button.pack(side="right", padx=5, pady=10)
    settings_button.configure(width=10)

    # Switch to change Light and DarkMode :
    def change_appearance_mode_event(new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    Appearance_mode_optionemenu = customtkinter.CTkOptionMenu(
        top_frame,
        values=["Light", "Dark", "System"],
        command=change_appearance_mode_event,
    )
    Appearance_mode_optionemenu.pack(side="right", padx=2, pady=10)

    # Switch to change the System Scaling to user desired percentage
    def change_scaling_event(new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    scaling_optionemenu = customtkinter.CTkOptionMenu(
        top_frame,
        width=80,
        values=["80%", "90%", "100%", "110%", "120%"],
        command=change_scaling_event,
    )
    scaling_optionemenu.pack(side="right", padx=2, pady=10)

    def Seperator_R() -> None:
        Seperator = customtkinter.CTkLabel(top_frame, text="|")
        Seperator.pack(side="right", padx=2, pady=10)
        Seperator.configure(width=2, font=("Arial", 16), fg_color="transparent")

    Seperator_R()

    def chat_gpt():
        webbrowser.open("https://chat.openai.com/")

    chat_gpt_button = customtkinter.CTkButton(
        top_frame, text="⚙️ ChatGPT", command=chat_gpt
    )
    chat_gpt_button.pack(side="right", padx=5, pady=10)
    chat_gpt_button.configure(width=10)

    def Phind():
        webbrowser.open("https://www.phind.com/")

    chat_gpt_button = customtkinter.CTkButton(top_frame, text="Phind", command=Phind)
    chat_gpt_button.pack(side="right", padx=5, pady=10)
    chat_gpt_button.configure(width=10)

    def Blackbox_AI():
        webbrowser.open("https://www.blackbox.ai/")

    chat_gpt_button = customtkinter.CTkButton(
        top_frame, text="BlackBox AI", command=Blackbox_AI
    )
    chat_gpt_button.pack(side="right", padx=5, pady=10)
    chat_gpt_button.configure(width=10)

    def Gemini():
        webbrowser.open("https://gemini.google.com/")

    chat_gpt_button = customtkinter.CTkButton(top_frame, text="Gemini", command=Gemini)
    chat_gpt_button.pack(side="right", padx=5, pady=10)
    chat_gpt_button.configure(width=10)

    Seperator_R()

    # Instantiate SearchWindow and pass the text area
    # def open_search_window():
    #     search = Searchwindow(root)

    label_gemini = customtkinter.CTkLabel(
        ai_bottom_frame, text="Gemini ✨", font=("JetBrainsMono NF", 14, "bold")
    )
    label_gemini.pack(side="top", padx=10, pady=10)
    output_text = customtkinter.CTkTextbox(
        ai_bottom_frame, width=350, wrap="word", font=("JetBrainsMono NF", 12)
    )
    output_text.pack(fill="both", expand=True)
    label_about_dev = customtkinter.CTkLabel(
        ai_bottom_frame,
        text="Configured by Parazeeknova",
        font=("JetBrainsMono NF", 10, "italic"),
    )
    label_about_dev.pack(side="bottom", padx=10, pady=0)
    label_about = customtkinter.CTkLabel(
        ai_bottom_frame,
        text="Powered by Google Vertex AI ☁️ - Gemini AI Experimental",
        font=("JetBrainsMono NF", 10, "italic"),
    )
    label_about.pack(side="bottom", padx=10, pady=0)

    def generate(input_text):
        vertexai.init(project="vital-platform-421513", location="us-central1")
        model = GenerativeModel("gemini-1.5-flash-001")
        global responses
        responses = model.generate_content(
            [input_text],
            generation_config=generation_config,
            safety_settings=safety_settings,
            stream=True,
        )

        for response in responses:
            output_text.insert(customtkinter.END, response.text)
            output_text.see(customtkinter.END)

    generation_config = {
        "max_output_tokens": 8192,
        "temperature": 1,
        "top_p": 0.95,
    }

    safety_settings = {
        generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    }

    def combined_command(event=None):
        on_button_click()
        toggle_ai_bottom_frame()
        toggle_left_frame()

    generate_button = customtkinter.CTkButton(
        top_frame, text="🔍", command=combined_command, width=1
    )
    generate_button.pack(side="right", padx=2, pady=10)

    input_entry = customtkinter.CTkEntry(
        top_frame, placeholder_text="Search | Powered by Gemini ✨", height=35
    )
    input_entry.pack(fill="x", expand=True, side="right", padx=10, pady=10)
    input_entry.bind("<Return>", combined_command)

    def on_button_click():
        input_text = input_entry.get()
        threading.Thread(target=generate, args=(input_text,)).start()

    # All buttons in the top frame for different functions (Left)
    New_button = customtkinter.CTkButton(top_frame, text="📄")
    New_button.pack(side="left", padx=2, pady=10)
    New_button.configure(width=2, font=("Arial", 18))

    def file_path_prompt():
        file_path = filedialog.askopenfilename()
        return file_path

    Open_button = customtkinter.CTkButton(
        top_frame,
        text="📂",
        command=lambda: tab_view.add_new_workspace_with_file(file_path_prompt()),
    )
    Open_button.pack(side="left", padx=2, pady=10)
    Open_button.configure(width=2, font=("Arial", 18))

    Save_button = customtkinter.CTkButton(top_frame, text="💾")
    Save_button.pack(side="left", padx=3, pady=10)
    Save_button.configure(width=2, font=("Arial", 18))

    def Seperator() -> None:
        Seperator = customtkinter.CTkLabel(top_frame, text="|")
        Seperator.pack(side="left", padx=2, pady=10)
        Seperator.configure(width=2, font=("Arial", 16), fg_color="transparent")

    Seperator()

    Cut_button = customtkinter.CTkButton(top_frame, text="Cut")
    Cut_button.pack(side="left", padx=3, pady=10)
    Cut_button.configure(width=2)

    Copy_button = customtkinter.CTkButton(top_frame, text="Copy")
    Copy_button.pack(side="left", padx=3, pady=10)
    Copy_button.configure(width=2)

    Paste_button = customtkinter.CTkButton(top_frame, text="Paste")
    Paste_button.pack(side="left", padx=3, pady=10)
    Paste_button.configure(width=2)

    select_button = customtkinter.CTkButton(top_frame, text="Select")
    select_button.pack(side="left", padx=3, pady=10)
    select_button.configure(width=2)

    undo_button = customtkinter.CTkButton(top_frame, text="Undo")
    undo_button.pack(side="left", padx=3, pady=10)
    undo_button.configure(width=2)

    redo_button = customtkinter.CTkButton(top_frame, text="Redo")
    redo_button.pack(side="left", padx=3, pady=10)
    redo_button.configure(width=2)

    Seperator()

    Suggestions = customtkinter.CTkButton(top_frame, text="Suggest a Feature")
    Suggestions.pack(side="left", padx=2, pady=10)
    Suggestions.configure(width=3)

    # About button in the top_bar
    About = customtkinter.CTkButton(top_frame, text="About", command=MyWindow)
    About.pack(side="left", padx=2, pady=10)
    About.configure(width=2)

    Exit_button = customtkinter.CTkButton(top_frame, text="Exit")
    Exit_button.pack(side="left", padx=3, pady=10)
    Exit_button.configure(width=2)

    Seperator()
    # All buttons in the bottom frame for different functions
    # Creating a button for theme change
    # Not working at the moment will implement in future

    # def changetheme_event(changetheme_next: str):
    #     customtkinter.set_default_color_theme(changetheme_next)
    # Changetheme_optionmenu = customtkinter.CTkOptionMenu(bottom_frame, values=["blue","dark-blue","green"],
    #                                                         command=changetheme_event)
    # Changetheme_optionmenu.pack(side="left",padx=5,pady=10)

    Dir_Label = customtkinter.CTkLabel(bottom_frame, text="Working directory : ")
    Dir_Label.pack(side="left", padx=(10, 0), pady=10)
    Dir_Label.configure(width=2, font=("JetBrainsMono NF", 12, "bold"))

    dirvar = str(current_directory_path)
    Dir_Label_pth = customtkinter.CTkLabel(bottom_frame, text=dirvar)
    Dir_Label_pth.pack(side="left", padx=2, pady=10)
    Dir_Label_pth.configure(width=2, font=("JetBrainsMono NF", 12))

    # Search_bar = customtkinter.CTkEntry(
    #     bottom_frame, placeholder_text="Enter your commands here.."
    # )
    # Search_bar.pack(side="right", padx=10, pady=10)
    # Search_bar.configure(width=250, font=("VictorMono Nerd Font Bold", 15))

    # left_arrow = customtkinter.CTkButton(bottom_frame, text="⇐")
    # left_arrow.pack(side="right",padx=1,pady=10)
    # left_arrow.configure(width= 2,fg_color="transparent")

    # right_arrow = customtkinter.CTkButton(bottom_frame, text="⇒")
    # right_arrow.pack(side="right",padx=1,pady=10)
    # right_arrow.configure(width= 2,fg_color="transparent")

    def Seperator_R() -> None:
        Seperator = customtkinter.CTkLabel(bottom_frame, text="|")
        Seperator.pack(side="right", padx=2, pady=10)
        Seperator.configure(width=2, font=("Arial", 16), fg_color="transparent")

    Seperator_R()

    remove_current_tab = customtkinter.CTkButton(
        bottom_frame, text="Remove Tab", command=tab_view.remove_current_tab
    )
    remove_current_tab.pack(side="right", padx=2, pady=10)

    add_workspace_button = customtkinter.CTkButton(
        bottom_frame, text="Add Workspace", command=tab_view.add_new_workspace
    )
    add_workspace_button.pack(side="right", padx=2, pady=10)

    add_codespace_button = customtkinter.CTkButton(
        bottom_frame, text="Add Codespace", command=tab_view.add_new_codespace
    )
    add_codespace_button.pack(side="right", padx=2, pady=10)

    Seperator_R()

    # Function to set opacity of the frames (pywinstyles)
    set_opacity(top_frame, value=0.6)
    set_opacity(left_frame, value=0.6)
    set_opacity(right_frame, value=0.6)
    set_opacity(bottom_frame, value=0.6)
    set_opacity(more_bottom_frame, value=0.6)
    set_opacity(ai_bottom_frame, value=0.6)


# The main function is called only when the script is run directly, not when it's imported as a module
if __name__ == "__main__":
    main()
    # show_welcome_window(root)
    # This is the main loop of the application. It keeps the application running until it is closed
    root.mainloop()
