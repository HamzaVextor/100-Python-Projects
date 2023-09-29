import PyPDF2

pdffile = open('Sample.pdf', 'rb')

pdfreader = PyPDF2.PdfReader(pdffile)

numpages = len(pdfreader.pages)

page = pdfreader.pages[0]


text = page.extract_text()

text_of_pages = f"Text: {text}"

with open('extracted_text.txt', 'w') as f:
    f.write(text_of_pages)