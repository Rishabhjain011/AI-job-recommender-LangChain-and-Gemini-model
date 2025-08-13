import fitz  # PyMuPDF

def extract_text_from_pdf(file):
    """
    Extract text from a PDF file.
    Works with both file paths (str) and file-like objects (BytesIO).
    """
    text = ""

    # Detect if input is a file path or BytesIO
    if isinstance(file, (str, bytes)):
        pdf = fitz.open(file)  # Path to file
    else:
        pdf = fitz.open(stream=file.read(), filetype="pdf")  # File-like object from Streamlit

    for page in pdf:
        text += page.get_text()
    pdf.close()

    return text.strip()
