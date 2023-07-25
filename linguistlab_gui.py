import customtkinter
import linguistlab

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")


class LLSideBar(customtkinter.CTkFrame):
    def __init__(self, master, linguistlab):
        super().__init__(master)
        self.linguistlab = linguistlab

        self.btn_open_glossary = customtkinter.CTkButton(
            self, text="Open glossary", command=linguistlab.open_glossary
        )
        self.btn_open_glossary.grid(row=0, column=0)


class LLGlossaryFrame(customtkinter.CTkFrame):
    def __init__(self, master, linguistlab):
        super().__init__(master)
        self.linguistlab = linguistlab


class LLMainWindow(customtkinter.CTk):
    def __init__(self, linguistlab):
        self.linguistlab = linguistlab
        super().__init__()

        self.title("LinguistLab")
        self.geometry("900x600")

        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        self.sidebar = LLSideBar(self, linguistlab)
        # self.sidebar.configure(fg_color="red")
        self.sidebar.grid(row=0, column=0, sticky="nswe")

        self.glossary_frame = LLGlossaryFrame(self, linguistlab)
        # self.glossary_frame.configure(fg_color="blue")
        self.glossary_frame.grid(row=0, column=1, sticky="nswe")


if __name__ == "__main__":
    main_window = LLMainWindow(linguistlab)
    main_window.mainloop()
