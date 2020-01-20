from pdf2image import convert_from_path
from pytesseract import pytesseract

DEFAULT_DPI = 300


def pdf_to_text(file_path: str, dpi=DEFAULT_DPI, join='\n--page--\n') -> str:
    pages = convert_from_path(pdf_path=file_path, dpi=dpi)
    content = (pytesseract.image_to_string(image=page) for page in pages)
    return join.join(content)
