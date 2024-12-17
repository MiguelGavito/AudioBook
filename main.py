import pyttsx3
import fitz
from tkinter.filedialog import *

def main():
    book = askopenfilename(title="Select an PDF document", filetypes=[("PDF Files","*.pdf")])
    if not book:
        print("document not selected.")
        return
    
    pdfDoc = fitz.open(book)
    totalPag = len(pdfDoc)
    print(f"This document have {totalPag} pages.")

    try:
        StartPag = int(input(f"Select the start page from 1 - {totalPag}: ")) - 1
        EndPag = int(input(f"Select the end page form {StartPag +2 } - {totalPag}"))

        if StartPag < 0 or EndPag > totalPag or StartPag >= EndPag:
            print("Rango de paginas invalido")
            return
    
    except:
        print("Use numbers.")
        return

    player = pyttsx3.init()

    for num in range(StartPag, EndPag):
        page = pdfDoc[num]
        text = page.get_text()
        print(f"Reading page {num + 1}...\n{text}\n")
        player.say(text)

    player.runAndWait()
    print("Reading complete")


if __name__ == "__main__":
    main()
"""
book = askopenfilename()

pdfreader = PdfReader(book)
pages = len(pdfreader.pages)

player = pyttsx3.init()

for num in range(0, pages):
    page = pdfreader.pages[num]
    text = page.extract_text()
    player.say(text)

player.runAndWait()
"""