import customtkinter as ctk
import tkinter as tk
from collections import deque

class textarea():
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.parent_frame.grid_rowconfigure(0, weight=1)
        self.parent_frame.grid_columnconfigure(0, weight=1)

        self.text_area = ctk.CTkTextbox(parent_frame, height=1, width=1, font=("JetbrainsMono NF", 16,), activate_scrollbars=True, wrap='none')
        self.text_area.grid(row=0, column=0, sticky='nsew')
        self.text_area.configure(padx=10, pady=10, takefocus=True)

        def do_popup(event):
            try:
                popup_menu.tk_popup(event.x_root, event.y_root)
            finally:
                popup_menu.grab_release()

        popup_menu = tk.Menu(self.parent_frame, tearoff=0)
        popup_menu.add_command(label="Cut", command=self.cut)
        popup_menu.add_command(label="Copy", command=self.copy)
        popup_menu.add_command(label="Paste", command=self.paste)
        popup_menu.add_separator()
        popup_menu.add_command(label="Undo", command=self.undo)
        popup_menu.add_command(label="Redo", command=self.redo)

        # Bind the focusout event to hide the menu
        popup_menu.bind("<FocusOut>", lambda event: popup_menu.unpost())

        self.text_area.bind("<Button-3>", do_popup)
        self.undo_stack = deque(maxlen=10)
        self.redo_stack = deque(maxlen=10)
        self.undo_stack.append(self.text_area.get(1.0, tk.END))

    def cut(self):
        try:
            start, end = self.text_area.tag_ranges(tk.SEL)
            self.text_area.clipboard_clear()
            self.text_area.clipboard_append(self.text_area.get(start, end))
            self.text_area.delete(start, end)
        except tk.TclError:
            pass # No selection

    def copy(self):
        try:
            start, end = self.text_area.tag_ranges(tk.SEL)
            self.text_area.clipboard_clear()
            self.text_area.clipboard_append(self.text_area.get(start, end))
        except tk.TclError:
            pass # No selection

    def paste(self):
        self.text_area.insert(tk.INSERT, self.text_area.clipboard_get())

    def undo(self):
        if len(self.undo_stack) > 1: # Ensure there's more than one state to undo
            self.redo_stack.append(self.text_area.get(1.0, tk.END))
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(1.0, self.undo_stack.pop())

    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.text_area.get(1.0, tk.END))
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(1.0, self.redo_stack.pop())
