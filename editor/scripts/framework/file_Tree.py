import sys
from pathlib import Path
import customtkinter as C
import tkinter as tk
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

      self.folder_image = PhotoImage(file= def_folder_image)  # Default folder path for the editor
      self.file_image = PhotoImage(file=def_file_image)  # Default file path for the editor

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

      self.treeview = ttk.Treeview(self.part_frame, height=40, show="tree")
      # self.treeview.heading("#0", text="Files: ", anchor="w")
      self.treeview.grid(row=1, column=0, columnspan=2, sticky="nsew")

      # Call the item_opened() method each item an item is expanded.
      self.treeview.tag_bind(
          "fstag", "<<TreeviewOpen>>", self.item_opened)
      # This dictionary maps the treeview items IDs with the
      # path of the file or folder.
      self.fsobjects: dict[str, Path] = {}
      self.load_tree(Path(Path(sys.executable).anchor))

  def safe_iterdir(self, path: Path) -> tuple[Path, ...] | tuple[()]:
        """
        Like `Path.iterdir()`, but do not raise on permission errors.
        """
        try:
            return tuple(path.iterdir())
        except PermissionError:
            print("You don't have permission to read", path)
            return ()
    
  def get_icon(self, path: Path) -> tk.PhotoImage:
        """
        Return a folder icon if `path` is a directory and
        a file icon otherwise.
        """
        return self.folder_image if path.is_dir() else self.file_image
    
  def insert_item(self, name: str, path: Path, parent: str = "") -> str:
        """
        Insert a file or folder into the treeview and return the item ID.
        """
        iid = self.treeview.insert(
            parent, tk.END, text=name, tags=("fstag",),
            image=self.get_icon(path))
        self.fsobjects[iid] = path
        return iid
    
  def load_tree(self, path: Path, parent: str = "") -> None:
        """
        Load the contents of `path` into the treeview. 
        """
        for fsobj in self.safe_iterdir(path):
            fullpath = path / fsobj
            child = self.insert_item(fsobj.name, fullpath, parent)
            # Preload the content of each directory within `path`.
            # This is necessary to make the folder item expandable.
            if fullpath.is_dir():
                for sub_fsobj in self.safe_iterdir(fullpath):
                    self.insert_item(sub_fsobj.name, fullpath / sub_fsobj, child)
    
  def load_subitems(self, iid: str) -> None:
        """
        Load the content of each folder inside the specified item
        into the treeview.
        """
        for child_iid in self.treeview.get_children(iid):
            if self.fsobjects[child_iid].is_dir():
                self.load_tree(self.fsobjects[child_iid],
                                parent=child_iid)
    
  def item_opened(self, _event: tk.Event) -> None:
        """
        Handler invoked when a folder item is expanded.
        """
        # Get the expanded item.
        iid = self.treeview.selection()[0]
        # If it is a folder, loads its content.
        self.load_subitems(iid)
