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

        self.columnconfigure((0, 1), weight=1)
        self.rowconfigure(0, weight=1)

        self.source_box = LLGlossaryTextBox(self)
        self.source_box.configure(corner_radius=0)
        self.source_box.grid(row=0, column=0, sticky="nsew")

        self.target_box = LLGlossaryTextBox(self)
        self.target_box.configure(corner_radius=0)
        self.target_box.grid(row=0, column=1, sticky="nsew")


class LLGlossaryTextBox(customtkinter.CTkTextbox):
    def __init__(self, master):
        super().__init__(master)


class LLMainWindow(customtkinter.CTk):
    def __init__(self, linguistlab):
        self.linguistlab = linguistlab
        super().__init__()

        self.title("LinguistLab")
        self.geometry("900x600")

        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        self.sidebar = LLSideBar(self, linguistlab)
        self.sidebar.grid(row=0, column=0, sticky="nsew")

        self.glossary_frame = LLGlossaryFrame(self, linguistlab)
        self.glossary_frame.grid(row=0, column=1, sticky="nsew")


if __name__ == "__main__":
    main_window = LLMainWindow(linguistlab)
    main_window.mainloop()
