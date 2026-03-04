import pdfplumber
import docx2txt

def extract_text(file_path):
    if file_path.endswith('.pdf'):
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text()
        return text.lower()

    elif file_path.endswith('.docx'):
        return docx2txt.process(file_path).lower()


