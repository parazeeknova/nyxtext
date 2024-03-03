# System imports here
import customtkinter
import tkinter as tk
import os
import webbrowser

# File imports here
from menu_Bar import Menubar
from text_Area import textarea
from settings import Settings
from tkinter import ttk, filedialog
from PIL import Image, ImageTk

# customtkinter.set_widget_scaling(80)
# customtkinter.set_window_scaling(80)

def main():
# This defines the main function, which is the entry point of the application
    root = customtkinter.CTk()
    root.geometry("800x600")
    root.title("NyxText")
    
# Sets (for now the appearance to light and color scheme to blue)
    customtkinter.set_appearance_mode("dark")
    
# Should be replaced with a function in future for catppuccin color scheme 
    customtkinter.set_default_color_theme("dark-blue")

# This is the icon for the application. It is expected to be in the same directory as the script
    ico_path = os.path.abspath("editor\\scripts\\misc\\icons\\icon.ico")
    root.iconbitmap(ico_path)
    
# Setting width of the left frame 10 percent of the screen 
    screen_width = root.winfo_screenwidth() - 50
    screen_height = root.winfo_screenheight() - 210
    frame_width = screen_width *  0.11
    rf = int(screen_width-frame_width)
    
# Static frames at the moment will be replaced by scrollable frames after a while
    top_frame = customtkinter.CTkFrame(root, width=screen_width, height=10) # Adjust height as needed
    top_frame.grid(row=0, column=0, columnspan=2, sticky='ew')
    
# Using scrollable frame for the left frame (for now will be changed in future), used to fix sizing bug
    left_frame = customtkinter.CTkScrollableFrame(root, width=int(frame_width), height=int(screen_height))
    left_frame.grid(row=1, column=0, sticky='nsew') # Ensure left_frame is correctly placed
    
    right_frame = customtkinter.CTkScrollableFrame(root, width=rf,height=int(screen_height))
    right_frame.grid(row=1, column=1, sticky='nsew')
    
    bottom_frame = customtkinter.CTkFrame(root, width=screen_width, height=30)
    bottom_frame.grid(row=2, column=0, columnspan=2, sticky='ew')

# Creates a tab view to show tabs (Static at the moment), Need to impliment the dynamic tab view
    tab_view = customtkinter.CTkTabview(right_frame,width=rf, height=int(screen_height))
    tab_view.grid(row=0, column=1,pady=10, sticky='nsew')
    tab_init = tab_view.add("Workspace")
    
    # Initialize a variable to keep track of the tab count
    global tab_count # Use the global keyword to modify the global variable
    tab_count = 0
    def add_new_tab():
        global tab_count # Use the global keyword to modify the global variable
        tab_count += 1 # Increment the tab count
    # Generate a unique title for the new tab
        tab_title = f"Workspace {tab_count}"
    # Add a new tab to the tab view
        new_tab = tab_view.add(tab_title)
        text_area = textarea(new_tab,int(screen_width),rf,int(screen_height))
        
        
        # Temp for testing will remove later
        # text_area = customtkinter.CTkTextbox(new_tab, height=int(screen_height), width=rf, activate_scrollbars=True, wrap='none')
        # text_area.pack(fill='both', expand=True)
        
    # Function to remove the currently selected tab
    def remove_current_tab():
    # Get the currently selected tab
        selected_tab = tab_view.get()
        if selected_tab:
        # Remove the selected tab
            tab_view.delete(selected_tab)

# Add a button to remove the currently selected tab
    remove_tab_button = customtkinter.CTkButton(bottom_frame, text="Remove Tab", command=remove_current_tab)
    remove_tab_button.pack(side="right", padx=5, pady=10)
    
    add_new_tab = customtkinter.CTkButton(bottom_frame, text="Add New Tab", command=add_new_tab)
    add_new_tab.pack(side="right",padx=5,pady=10)

# All Items for the left frame are below :
    Filetree_Button = customtkinter.CTkLabel(left_frame, text="FileTree :", font=("VictorMono Nerd Font",14,"bold"))
    Filetree_Button.grid(row=0, column=0,pady=5, sticky='nsew')
    Filetree_Button.configure(width=2)

# Preparing images for the file tree
    folder_image = Image.open("editor\\scripts\\misc\\icons\\folder.ico")
    resized_folder_icon = folder_image.resize((16, 16), Image.BICUBIC)
    folder_path = ImageTk.PhotoImage(resized_folder_icon)
    
    file_image = Image.open("editor\\scripts\\misc\\icons\\file.ico")
    resized_file_icon = file_image.resize((16, 16), Image.BICUBIC)
    file_path = ImageTk.PhotoImage(resized_file_icon)

# Inside the main function, after creating the left_frame
    file_tree = ttk.Treeview(left_frame,height=35)
    file_tree.heading("#0", text="Files :", anchor="w")
    file_tree.grid(row=1, column=0, sticky='nsew')


    def populate_file_tree(tree, path):
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
            # Insert the directory into the tree and get its ID
                global dir_id
                dir_id = tree.insert("", "end", text=item, open=True,image= folder_path)
            # Recursively populate the directory
                populate_file_tree(tree, item_path)
            else:
            # Insert the file into the tree using the parent directory's ID
                tree.insert(dir_id, "end", text=item, image= file_path)

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
    style.configure('Treeview', background='#333', foreground='#fff')
    style.configure('Treeview.Heading', background='#333', foreground='#333')

# Customizing the appearance of selected items and lines
    style.map('Treeview',
    background=[('selected', '#555')],
    foreground=[('selected', '#fff')]
)

# Bydefault populate the file tree with the desktop directory
    # desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    current_directory_path = os.getcwd()
    populate_file_tree(file_tree, current_directory_path)
    
# Add a button to open the directory dialog
    open_directory_button = customtkinter.CTkButton(left_frame, text="Open Directory", command=open_directory_dialog)
    open_directory_button.grid(row=2, column=0,pady=5, sticky='nsew')

# This imports the text_Area class from a module named text_area.py. This class is expected to contain the logic for creating a text area for the application
    global Textarea
    Textarea = textarea(tab_init,int(screen_width),rf,int(screen_height))
    
# This imports the Menubar class from a module named menu_bar.py. This class is expected to contain the logic for creating a menu bar for the application
    menu_bar = Menubar(root,Textarea)
    root.config(menu=menu_bar.menubar)
    
# All buttons and search bar in the top frame for different functions (Right)
    
    def open_settings_window():
        settings = Settings(root)
    settings_button = customtkinter.CTkButton(top_frame, text="⚙️",command=open_settings_window)
    settings_button.pack(side="right",padx=5,pady=10)
    settings_button.configure(width=10)
    
    def Seperator_R():
        Seperator = customtkinter.CTkLabel(top_frame, text="|")
        Seperator.pack(side="right",padx=2,pady=10)
        Seperator.configure(width=2,font = ("Arial",16),fg_color="transparent")
    Seperator_R()
    
    def chat_gpt():
            webbrowser.open('https://chat.openai.com/')
    chat_gpt_button = customtkinter.CTkButton(top_frame, text="⚙️ ChatGPT",command=chat_gpt)
    chat_gpt_button.pack(side="right",padx=5,pady=10)
    chat_gpt_button.configure(width=10)
    
    def Phind():
            webbrowser.open('https://www.phind.com/')
    chat_gpt_button = customtkinter.CTkButton(top_frame, text="Phind",command=Phind)
    chat_gpt_button.pack(side="right",padx=5,pady=10)
    chat_gpt_button.configure(width=10)
    
    def Blackbox_AI():
            webbrowser.open('https://www.blackbox.ai/')
    chat_gpt_button = customtkinter.CTkButton(top_frame, text="BlackBox AI",command=Blackbox_AI)
    chat_gpt_button.pack(side="right",padx=5,pady=10)
    chat_gpt_button.configure(width=10)
    
    def Gemini():
            webbrowser.open('https://gemini.google.com/')
    chat_gpt_button = customtkinter.CTkButton(top_frame, text="Gemini",command=Gemini)
    chat_gpt_button.pack(side="right",padx=5,pady=10)
    chat_gpt_button.configure(width=10)
    
    Seperator_R()
    
    # Commented at the moment, will implement later
    
    # right_arrow = customtkinter.CTkButton(top_frame, text=">")
    # right_arrow.pack(side="right",padx=1,pady=10)
    # right_arrow.configure(width= 2,fg_color="transparent")
    
    Search_bar = customtkinter.CTkEntry(top_frame, placeholder_text="🔍 Search")
    Search_bar.pack(side="right",padx=5,pady=10)
    Search_bar.configure(width=250, font = ("VictorMono Nerd Font Bold",15))
    
    # Commented at the moment, will be implemented later 
    
    # left_arrow = customtkinter.CTkButton(top_frame, text="<")
    # left_arrow.pack(side="right",padx=1,pady=10)
    # left_arrow.configure(width= 2,fg_color="transparent")
    
    Seperator_R()
    
# All buttons in the top frame for different functions (Left)
    New_button = customtkinter.CTkButton(top_frame, text="📄")
    New_button.pack(side="left",padx=2,pady=10)
    New_button.configure(width=2,font = ("Arial",18))
    
    Open_button = customtkinter.CTkButton(top_frame, text="📂")
    Open_button.pack(side="left",padx=2,pady=10)
    Open_button.configure(width=2,font = ("Arial",18))
    
    Save_button = customtkinter.CTkButton(top_frame, text="💾")
    Save_button.pack(side="left",padx=3,pady=10)
    Save_button.configure(width=2,font = ("Arial",18))
    
    def Seperator():
        Seperator = customtkinter.CTkLabel(top_frame, text="|")
        Seperator.pack(side="left",padx=2,pady=10)
        Seperator.configure(width=2,font = ("Arial",16),fg_color="transparent")
    Seperator()
        
    Cut_button = customtkinter.CTkButton(top_frame, text="Cut")
    Cut_button.pack(side="left",padx=3,pady=10)
    Cut_button.configure(width=2)
    
    Copy_button = customtkinter.CTkButton(top_frame, text="Copy")
    Copy_button.pack(side="left",padx=3,pady=10)
    Copy_button.configure(width=2)
    
    Paste_button = customtkinter.CTkButton(top_frame, text="Paste")
    Paste_button.pack(side="left",padx=3,pady=10)
    Paste_button.configure(width=2)
    
    Seperator()
    
    Exit_button = customtkinter.CTkButton(top_frame, text="Exit")
    Exit_button.pack(side="left",padx=3,pady=10)
    Exit_button.configure(width=2)
    
    Dark_Light_mode = customtkinter.CTkButton(top_frame, text="🌓")
    Dark_Light_mode.pack(side="left",padx=2,pady=10)
    Dark_Light_mode.configure(width=2,font = ("Arial",16))
    
    About = customtkinter.CTkButton(top_frame, text="About")
    About.pack(side="left",padx=2,pady=10)
    About.configure(width=2)
    
    Seperator()
    
    Discussion = customtkinter.CTkButton(top_frame, text="NyxText - Discussions")
    Discussion.pack(side="left",padx=2,pady=10)
    Discussion.configure(width=3)
    
    Issues = customtkinter.CTkButton(top_frame, text="Report an Issue")
    Issues.pack(side="left",padx=2,pady=10)
    Issues.configure(width=3)
    
    Suggestions = customtkinter.CTkButton(top_frame, text="Suggest a Feature")
    Suggestions.pack(side="left",padx=2,pady=10)
    Suggestions.configure(width=3) 
    
# All buttons in the bottom frame for different functions
    Color_Scheme_Button = customtkinter.CTkLabel(bottom_frame, text="Color Scheme :")
    Color_Scheme_Button.pack(side="left",padx=2,pady=10)
    Color_Scheme_Button.configure(width=2)

    Color_Scheme_button = customtkinter.CTkSegmentedButton(bottom_frame, values=["Frappe", "Latte", "Macchiato", "Mocha"])
    Color_Scheme_button.pack(side="left",padx=5,pady=10)
    Color_Scheme_button.configure(width=10)

# This is the main loop of the application. It keeps the application running until it is closed
    root.mainloop()
    
# The main function is called only when the script is run directly, not when it's imported as a module 
if __name__ == "__main__":
    main()