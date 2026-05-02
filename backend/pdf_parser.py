import fitz  # PyMuPDF

def extract_text_from_pdf(filepath: str) -> str:
    """Extract all text from a PDF file"""
    doc = fitz.open(filepath)
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    doc.close()
    return full_text