import customtkinter as ctk

class FeaturesWindow(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.geometry("1600x1000")
        self.wm_overrideredirect(True)
        
        # Center the window on the screen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = 600
        window_height = 500
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        self.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        self.attributes('-alpha', 0.95)
        
        # Create a close button with specified width and height
        self.close_button = ctk.CTkButton(self, text="X", command=self.destroy, width=20, height=20, fg_color='transparent', text_color='#ed8796')
        # Place the close button at the top right corner
        self.close_button.place(x=window_width - 24, y=10)
        
        self.welcome_title_text = ctk.CTkLabel(self, text="Features",
                                                font=('JetBrainsMono NF',80,"bold"),
                                                padx=100, anchor="center")
        self.welcome_title_text.pack(side='top', pady=(50,0))
        
        # Define a list of colors
        colors = ['#ed8796', '#87ed96', '#9687ed', '#ed9687', '#8796ed', '#96ed87', '#ed8787', '#87ed87', '#9687ed', '#ed9696']
        
        # List of features
        features = [
            "1- Work on multiple text files simultaneously.",
            "2- Syntax highlighting - For the code space area.",
            "3- Catpuccin Color Palette themes(4) + 4 Custom made themes and counting on..",
            "4- Dark / Light mode.",
            "5- Basic functions (new,open,save,cut,copy, etc.) check menu bar for more..",
            "6- FileTree View which shows all your project's files & folders.) check menu bar for more..",
            "7- System scaling support.",
            "8- Responsive design - 3 modes (windowed, middleman, fullscreen).",
            "9- AI assistence, shortcuts to Gemini, ChatGPT, BlackboxAI...",
            "10- Code area for coding"
        ]
        
        # Iterate over features and create labels with different colors
        for i, feature in enumerate(features):
            feature_label = ctk.CTkLabel(self, text=feature,
                                        font=('JetBrainsMono NF',15,"italic"),
                                        padx=100, anchor="center",
                                        text_color=colors[i % len(colors)]) # Use modulo to cycle through colors
            feature_label.pack(side='top')
