import os
import customtkinter as C
from tkinter import ttk,PhotoImage, filedialog

class treeView:
  def __init__(self,parent_frame,bg_color_tree,selected_color_tree,def_folder_image,def_file_image):
    self.part_frame = parent_frame
    self.setup_treeview(parent_frame,bg_color_tree,selected_color_tree,def_folder_image,def_file_image)

  def setup_treeview(self,parent_frame,bg_color_tree,selected_color_tree,def_folder_image,def_file_image):
      self.fileTree_label = C.CTkLabel(
          parent_frame, text="Treeview", font=("JetbrainsMono Nerd Font", 12, "bold")
      )
      self.fileTree_label.grid(
          row=0, column=0,pady =2,padx=4, columnspan=2, sticky="nsew"
      )
      self.fileTree_label.configure(width = 10)

      folder_path = PhotoImage(file= def_folder_image)  # Default folder path for the editor
      file_path = PhotoImage(file=def_file_image)  # Default file path for the editor

      treestyle = ttk.Style()
      treestyle.theme_use("default")
      treestyle.configure(
          "Treeview", background=bg_color_tree, fieldbackground=bg_color_tree, borderwidth=0
      )
      treestyle.configure("Treeview.Heading", background=bg_color_tree, foreground="white")
      treestyle.configure("Treeview", treeareaforeground="gray")
      treestyle.map(
          "Treeview", background=[("selected", selected_color_tree)], foreground=[("selected", "white")]
      )

      self.treeview = ttk.Treeview(self.part_frame, height=40)
      self.treeview.heading("#0", text="Files: ", anchor="w")
      self.treeview.grid(row=1, column=0, columnspan=2, sticky="nsew")

      self.treeview.bind("<<TreeviewSelect>>", lambda event: self.treeview.focus_set())

      def populate_file_tree(tree, path):
          for item in os.listdir(path):
              item_path = os.path.join(path, item)
              if os.path.isdir(item_path):
                  dir_id = tree.insert("", "end", text=item, open=True, image=folder_path) # Insert the directory into the tree and get its ID
                  populate_file_tree(tree, item_path) # Recursively populate the directory
              else:
                  dir_id = tree.insert("", "end", text=item, open=False) # Insert the file into the tree using the parent directory's ID
                  tree.insert(dir_id, "end", text=item, image=file_path)

      def open_directory_dialog():
          directory_path = filedialog.askdirectory()
          if directory_path:
              for item in self.treeview.get_children():
                  self.treeview.delete(item)
          populate_file_tree(self.treeview, directory_path) # Populate the file tree with the selected directory

      current_directory = os.getcwd()
      populate_file_tree(self.treeview, current_directory)


