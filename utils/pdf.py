from pdf2image import convert_from_path
from pytesseract import pytesseract

# Dots per inch value to use for converting PDF into images.
# This will determine the final resolution of the images despite of the original
# scan quality.
DEFAULT_DPI = 300


def pdf_to_text(file_path: str, dpi=DEFAULT_DPI, join: str = '\n--page--\n') -> str:
    """
    Open the PDF file in file_path and convert it into a single string. If multiple pages are
    present, the strings will be joined using the join string.
    :param file_path:
    :param dpi:
    :param join:
    :return:
    """
    pages = convert_from_path(pdf_path=file_path, dpi=dpi)
    content = (pytesseract.image_to_string(image=page) for page in pages)
    return join.join(content)
