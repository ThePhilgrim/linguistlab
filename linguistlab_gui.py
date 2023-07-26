import customtkinter
import linguistlab

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")


class LLMainWindow(customtkinter.CTk):
    def __init__(self, linguistlab):
        self.linguistlab = linguistlab
        super().__init__()

        self.title("LinguistLab")
        self.geometry("900x600")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.glossary_tab = LLGlossaryTab(self, linguistlab)
        self.glossary_tab.grid(row=0, column=0, sticky="nswew")


class LLGlossaryTab(customtkinter.CTkFrame):
    def __init__(self, master, linguistlab):
        super().__init__(master)

        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        # Sidebar
        self.sidebar = customtkinter.CTkFrame(self, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")

        self.btn_open_glossary = customtkinter.CTkButton(
            self.sidebar, text="Open Glossary", command=self.open_glossary
        )
        self.btn_open_glossary.grid(row=0, column=0, padx=(8), pady=(8))

        # Glossary pane
        self.glossary_pane = customtkinter.CTkFrame(self, corner_radius=0)
        self.glossary_pane.grid(row=0, column=1, sticky="nsew")

        self.glossary_pane.columnconfigure(0, weight=1)
        self.glossary_pane.rowconfigure(0, weight=1)

        # TODO: Make textbox read-only
        self.glossary_textbox = customtkinter.CTkTextbox(self.glossary_pane, corner_radius=0)
        self.glossary_textbox.grid(row=0, column=0, sticky="nsew")

    def open_glossary(self):
        glossary = linguistlab.read_glossary_file()

        # User pressed cancel in filedialog
        if not glossary:
            return

        self.insert_glossary(glossary)

    def insert_glossary(self, glossary):
        row_num = 1

        # Make source term bold https://www.youtube.com/watch?v=X6zqePBPDVU&ab_channel=Codemy.com
        # https://customtkinter.tomschimansky.com/documentation/widgets/textbox#insertindex-text-tagsnone
        for source_term in glossary.glossary_content.keys():
            self.glossary_textbox.insert(f"{row_num}.0", f"{source_term}\n")
            row_num += 1

            for target_term in glossary.glossary_content[source_term]:
                self.glossary_textbox.insert(f"{row_num}.0", f"            {target_term}\n")
                row_num += 1

            for i in range(2):
                self.glossary_textbox.insert(f"{row_num}.0", "\n")
                row_num += 1


if __name__ == "__main__":
    main_window = LLMainWindow(linguistlab)
    main_window.mainloop()
