from PyPDF2 import PdfReader

def extract_text_from_pdf(file_bytes: bytes) -> str:
    with open("temp.pdf", "wb") as f:
        f.write(file_bytes)
    reader = PdfReader("temp.pdf")
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text.strip()