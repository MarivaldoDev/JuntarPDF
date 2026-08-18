from pikepdf import Pdf
import os

pdfs = os.listdir("pdfs")


with Pdf.new() as merged:
    for filename in pdfs:
        src = Pdf.open(f"pdfs/{filename}")
        merged.pages.extend(src.pages)
    merged.save('merged.pdf')

print("Processo finalizado!")
