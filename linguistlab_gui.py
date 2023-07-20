import customtkinter
import linguistlab

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")


class LLSideBar(customtkinter.CTkFrame):
    def __init__(self, master, linguistlab):
        self.linguistlab = linguistlab
        super().__init__(master)

        self.btn_open_glossary = customtkinter.CTkButton(
            master, text="Open glossary", command=linguistlab.open_glossary
        )
        self.btn_open_glossary.grid(row=0, column=0, sticky="n")


class LLMainWindow(customtkinter.CTk):
    def __init__(self, linguistlab):
        self.linguistlab = linguistlab
        super().__init__()

        self.title("LinguistLab")
        self.geometry("900x600")

        self.sidebar = LLSideBar(self, linguistlab)
        self.sidebar.grid(row=0, column=0, sticky="nsw")


if __name__ == "__main__":
    main_window = LLMainWindow(linguistlab)
    main_window.mainloop()
