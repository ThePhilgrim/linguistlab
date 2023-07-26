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

        # Glossary frame
        self.glossary_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.glossary_frame.grid(row=0, column=1, sticky="nsew")

        self.glossary_frame.columnconfigure(0, weight=1)
        self.glossary_frame.rowconfigure(1, weight=1)

        # Search bars
        self.search_frame = customtkinter.CTkFrame(self.glossary_frame, corner_radius=0)
        self.search_frame.grid(row=0, column=0, pady=(0, 16), sticky="nsew")

        self.search_frame.columnconfigure((0, 1), weight=1)

        self.source_search_label = customtkinter.CTkLabel(
            self.search_frame, text="Search source term"
        )
        self.source_search_label.grid(row=0, column=0, sticky="w")

        self.source_search = customtkinter.CTkEntry(self.search_frame)
        self.source_search.grid(row=1, column=0, sticky="nsew")

        self.target_search_label = customtkinter.CTkLabel(
            self.search_frame, text="Search target term"
        )
        self.target_search_label.grid(row=0, column=1, sticky="w")

        self.target_search = customtkinter.CTkEntry(self.search_frame)
        self.target_search.grid(row=1, column=1, sticky="nsew")

        # Text box
        self.glossary_textbox = customtkinter.CTkTextbox(self.glossary_frame, corner_radius=0)
        self.glossary_textbox.grid(row=1, column=0, sticky="nsew")

    def open_glossary(self):
        glossary = linguistlab.read_glossary_file()

        # User pressed cancel in filedialog
        if not glossary:
            return

        self.insert_glossary(glossary)

    # TODO Remove when terminology search is possible
    def insert_glossary(self, glossary):
        self.glossary_textbox.configure(state="normal")
        self.glossary_textbox.delete("0.0", "end")

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

        self.glossary_textbox.configure(state="disabled")


if __name__ == "__main__":
    main_window = LLMainWindow(linguistlab)
    main_window.mainloop()
