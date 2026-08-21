from pathlib import Path

import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from customtkinter import filedialog
from pikepdf import Pdf


class PDFMergerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Juntar PDFs")
        self.geometry("720x560")
        self.resizable(False, False)
        self.minsize(620, 480)
        self.files = []

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        self._build_interface()

    def _build_interface(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, padx=32, pady=(28, 12), sticky="ew")
        ctk.CTkLabel(
            header, text="Juntar PDFs", font=ctk.CTkFont(size=28, weight="bold")
        ).pack(anchor="w")
        ctk.CTkLabel(
            header,
            text="Adicione os arquivos na ordem em que deseja unir.",
            text_color=("#5B6472", "#AAB4C3"),
        ).pack(anchor="w", pady=(4, 0))

        toolbar = ctk.CTkFrame(self, fg_color="transparent")
        toolbar.grid(row=1, column=0, padx=32, pady=(0, 12), sticky="ew")
        ctk.CTkButton(toolbar, text="＋  Adicionar PDFs", command=self.add_files).pack(
            side="left"
        )
        ctk.CTkButton(
            toolbar, text="Limpar lista", command=self.clear_files, fg_color="transparent",
            border_width=1, border_color=("#CBD5E1", "#475569"),
            text_color=("#334155", "#E2E8F0"),
        ).pack(side="right")

        list_frame = ctk.CTkFrame(self, corner_radius=10)
        list_frame.grid(row=2, column=0, padx=32, sticky="nsew")
        list_frame.grid_columnconfigure(0, weight=1)
        list_frame.grid_rowconfigure(0, weight=1)

        self.file_list = ctk.CTkScrollableFrame(list_frame, label_text="Arquivos selecionados")
        self.file_list.grid(row=0, column=0, padx=12, pady=12, sticky="nsew")
        self.empty_label = ctk.CTkLabel(
            self.file_list, text="Nenhum PDF adicionado ainda.",
            text_color=("#64748B", "#94A3B8"),
        )
        self.empty_label.pack(pady=80)

        actions = ctk.CTkFrame(self, fg_color="transparent")
        actions.grid(row=3, column=0, padx=32, pady=(14, 28), sticky="ew")
        self.status_label = ctk.CTkLabel(actions, text="0 arquivos", anchor="w")
        self.status_label.pack(side="left")
        ctk.CTkButton(
            actions, text="Mesclar e salvar", command=self.merge_files,
            width=180, height=40, state="disabled"
        ).pack(side="right")
        self.merge_button = actions.winfo_children()[-1]

    def add_files(self):
        selected = filedialog.askopenfilenames(
            title="Selecione os PDFs", filetypes=[("Arquivos PDF", "*.pdf")]
        )
        for filename in selected:
            if filename not in self.files:
                self.files.append(filename)
        self.refresh_list()

    def clear_files(self):
        self.files.clear()
        self.refresh_list()

    def remove_file(self, index):
        self.files.pop(index)
        self.refresh_list()

    def move_file(self, index, direction):
        new_index = index + direction
        if 0 <= new_index < len(self.files):
            self.files[index], self.files[new_index] = self.files[new_index], self.files[index]
            self.refresh_list()

    def refresh_list(self):
        for widget in self.file_list.winfo_children():
            widget.destroy()

        if not self.files:
            self.empty_label = ctk.CTkLabel(
                self.file_list, text="Nenhum PDF adicionado ainda.",
                text_color=("#64748B", "#94A3B8"),
            )
            self.empty_label.pack(pady=80)
        else:
            for index, filename in enumerate(self.files):
                row = ctk.CTkFrame(self.file_list, fg_color="transparent")
                row.pack(fill="x", padx=4, pady=3)
                ctk.CTkLabel(row, text=f"{index + 1:02d}", width=36, anchor="w").pack(side="left")
                ctk.CTkLabel(row, text=Path(filename).name, anchor="w").pack(
                    side="left", fill="x", expand=True
                )
                ctk.CTkButton(
                    row, text="↑", width=32, command=lambda i=index: self.move_file(i, -1)
                ).pack(side="left", padx=2)
                ctk.CTkButton(
                    row, text="↓", width=32, command=lambda i=index: self.move_file(i, 1)
                ).pack(side="left", padx=2)
                ctk.CTkButton(
                    row, text="×", width=32, fg_color="transparent",
                    text_color=("#B42318", "#F97066"), command=lambda i=index: self.remove_file(i)
                ).pack(side="left", padx=(2, 0))

        self.status_label.configure(text=f"{len(self.files)} arquivo(s)")
        self.merge_button.configure(state="normal" if self.files else "disabled")

    def merge_files(self):
        output_file = filedialog.asksaveasfilename(
            title="Salvar PDF", defaultextension=".pdf",
            filetypes=[("Arquivos PDF", "*.pdf")], initialfile="pdfs-mesclados.pdf"
        )
        if not output_file:
            return

        try:
            with Pdf.new() as merged:
                for filename in self.files:
                    with Pdf.open(filename) as source:
                        merged.pages.extend(source.pages)
                merged.save(output_file)
        except Exception as error:
            CTkMessagebox(title="Erro", message=f"Não foi possível mesclar os PDFs.\n{error}", icon="cancel")
            return

        CTkMessagebox(title="Sucesso", message="PDFs mesclados com sucesso!", icon="check")


if __name__ == "__main__":
    app = PDFMergerApp()
    app.mainloop()
