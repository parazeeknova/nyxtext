# main.py
import tkinter as tk
from menu_bar import Menubar
from text_area import text_Area


def main():
    root = tk.Tk()
    root.title("NyxText")
    
    menu_bar = Menubar(root)
    root.config(menu=menu_bar.menubar)
    
    textarea = text_Area(root)
    
    root.mainloop()

if __name__ == "__main__":
    main()
