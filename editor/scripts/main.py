import customtkinter


def main():
    root = customtkinter.CTk()
    root.geometry("400x300")
    root.title("NyxText")

    button = customtkinter.CTkButton(root, text="my button")
    button.pack(padx=20, pady=20)

    root.mainloop()
    
if __name__ == "__main__":
    main()