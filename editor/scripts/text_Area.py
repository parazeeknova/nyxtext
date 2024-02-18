import tkinter as tk
root = tk.Tk()

text_area = tk.Text(root, wrap=tk.WORD)
text_area.pack(expand=True, fill=tk.BOTH)

root.mainloop()