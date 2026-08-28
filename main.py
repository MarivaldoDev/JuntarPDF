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
        self.colors = {
            "background": "#101417",
            "surface": "#182126",
            "surface_alt": "#202C33",
            "border": "#30414A",
            "text": "#F3F7F5",
            "muted": "#91A39F",
            "accent": "#E8A35C",
            "accent_hover": "#F0B875",
            "danger": "#F27D72",
        }
        self.configure(fg_color=self.colors["background"])
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, padx=36, pady=(30, 18), sticky="ew")
        ctk.CTkLabel(
            header,
            text="FERRAMENTA DE DOCUMENTOS",
            text_color=self.colors["accent"],
            font=ctk.CTkFont(size=10, weight="bold"),
        ).grid(row=0, column=0, sticky="w")
        ctk.CTkLabel(
            header,
            text="Juntar PDFs",
            text_color=self.colors["text"],
            font=ctk.CTkFont(size=28, weight="bold"),
        ).grid(row=1, column=0, sticky="w", pady=(1, 0))
        ctk.CTkLabel(
            header,
            text="Adicione os arquivos na ordem em que deseja unir.",
            text_color=self.colors["muted"],
            font=ctk.CTkFont(size=12),
        ).grid(row=2, column=0, sticky="w", pady=(5, 0))

        toolbar = ctk.CTkFrame(self, fg_color="transparent")
        toolbar.grid(row=1, column=0, padx=36, pady=(0, 14), sticky="ew")
        ctk.CTkButton(
            toolbar,
            text="＋  Adicionar PDFs",
            command=self.add_files,
            height=38,
            fg_color=self.colors["accent"],
            hover_color=self.colors["accent_hover"],
            text_color="#101417",
            font=ctk.CTkFont(size=13, weight="bold"),
        ).pack(side="left")
        ctk.CTkButton(
            toolbar,
            text="Limpar lista",
            command=self.clear_files,
            height=36,
            fg_color="transparent",
            border_width=1,
            border_color=self.colors["border"],
            text_color=self.colors["muted"],
            hover_color=self.colors["surface_alt"],
        ).pack(side="right")

        list_frame = ctk.CTkFrame(
            self,
            corner_radius=16,
            fg_color=self.colors["surface"],
            border_width=1,
            border_color=self.colors["border"],
        )
        list_frame.grid(row=2, column=0, padx=36, sticky="nsew")
        list_frame.grid_columnconfigure(0, weight=1)
        list_frame.grid_rowconfigure(0, weight=1)

        self.file_list = ctk.CTkScrollableFrame(
            list_frame,
            label_text="  ARQUIVOS SELECIONADOS  ",
            label_text_color=self.colors["muted"],
            fg_color="transparent",
            scrollbar_button_color=self.colors["border"],
            scrollbar_button_hover_color=self.colors["muted"],
        )
        self.file_list.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.empty_label = ctk.CTkLabel(
            self.file_list,
            text="Nenhum PDF adicionado ainda.\n\nComece adicionando seus arquivos acima.",
            text_color=self.colors["muted"],
            justify="center",
            font=ctk.CTkFont(size=13),
        )
        self.empty_label.pack(pady=80)

        actions = ctk.CTkFrame(self, fg_color="transparent")
        actions.grid(row=3, column=0, padx=36, pady=(16, 30), sticky="ew")
        self.status_label = ctk.CTkLabel(
            actions,
            text="0 arquivos",
            anchor="w",
            text_color=self.colors["muted"],
            font=ctk.CTkFont(size=12),
        )
        self.status_label.pack(side="left")
        ctk.CTkButton(
            actions,
            text="Mesclar e salvar",
            command=self.merge_files,
            width=190,
            height=42,
            state="disabled",
            corner_radius=10,
            fg_color=self.colors["surface_alt"],
            hover_color=self.colors["accent_hover"],
            text_color=self.colors["text"],
            font=ctk.CTkFont(size=13, weight="bold"),
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
            self.files[index], self.files[new_index] = (
                self.files[new_index],
                self.files[index],
            )
            self.refresh_list()

    def refresh_list(self):
        for widget in self.file_list.winfo_children():
            widget.destroy()

        if not self.files:
            self.empty_label = ctk.CTkLabel(
                self.file_list,
                text="Nenhum PDF adicionado ainda.\n\nComece adicionando seus arquivos acima.",
                text_color=self.colors["muted"],
                justify="center",
                font=ctk.CTkFont(size=13),
            )
            self.empty_label.pack(pady=80)
        else:
            for index, filename in enumerate(self.files):
                row = ctk.CTkFrame(
                    self.file_list,
                    fg_color=self.colors["surface_alt"],
                    corner_radius=10,
                )
                row.pack(fill="x", padx=4, pady=3)
                ctk.CTkLabel(
                    row,
                    text=f"{index + 1:02d}",
                    width=42,
                    anchor="center",
                    text_color=self.colors["accent"],
                    font=ctk.CTkFont(size=12, weight="bold"),
                ).pack(side="left", padx=(4, 0))
                ctk.CTkLabel(
                    row,
                    text=Path(filename).name,
                    anchor="w",
                    text_color=self.colors["text"],
                ).pack(side="left", fill="x", expand=True)
                ctk.CTkButton(
                    row,
                    text="↑",
                    width=30,
                    height=28,
                    fg_color="transparent",
                    hover_color=self.colors["border"],
                    text_color=self.colors["muted"],
                    command=lambda i=index: self.move_file(i, -1),
                ).pack(side="left", padx=2)
                ctk.CTkButton(
                    row,
                    text="↓",
                    width=30,
                    height=28,
                    fg_color="transparent",
                    hover_color=self.colors["border"],
                    text_color=self.colors["muted"],
                    command=lambda i=index: self.move_file(i, 1),
                ).pack(side="left", padx=2)
                ctk.CTkButton(
                    row,
                    text="×",
                    width=30,
                    height=28,
                    fg_color="transparent",
                    hover_color="#573238",
                    text_color=self.colors["danger"],
                    command=lambda i=index: self.remove_file(i),
                ).pack(side="left", padx=(2, 0))

        self.status_label.configure(text=f"{len(self.files)} arquivo(s)")
        self.merge_button.configure(state="normal" if self.files else "disabled")

    def merge_files(self):
        output_file = filedialog.asksaveasfilename(
            title="Salvar PDF",
            defaultextension=".pdf",
            filetypes=[("Arquivos PDF", "*.pdf")],
            initialfile="pdfs-mesclados.pdf",
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
            CTkMessagebox(
                title="Erro",
                message=f"Não foi possível mesclar os PDFs.\n{error}",
                icon="cancel",
            )
            return

        CTkMessagebox(
            title="Sucesso", message="PDFs mesclados com sucesso!", icon="check"
        )


if __name__ == "__main__":
    app = PDFMergerApp()
    app.mainloop()
