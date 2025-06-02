import pdfplumber
import docx

def extract_text_from_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        return "\n".join(page.extract_text() or "" for page in pdf.pages)

def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    return "\n".join(paragraph.text for paragraph in doc.paragraphs)
