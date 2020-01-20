""""
A script to process pdf files from a traditional scanner and extract plaintext content from it.
Utilizes tesseract ocr engine, make sure it is installed properly.
"""
import argparse

from pdf2image import convert_from_path
from pytesseract import pytesseract

DEFAULT_DPI = 300
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Process pdf files from a traditional scanner and extract plaintext content from it')
    parser.add_argument('filename', type=str, nargs=1, help='The path to the pdf file to parse')
    parser.add_argument('--dpi', '-d',
                        metavar='D',
                        type=int, nargs=1, default=DEFAULT_DPI,
                        help=f"The dpi value to use while converting pdf into images. Defaults to {DEFAULT_DPI}.")

    args = parser.parse_args()
    file_path = args.filename[0]
    dpi = args.dpi
    print(f"Parsing file: {file_path} with dpi: {dpi}..")
    pages = convert_from_path(pdf_path=file_path, dpi=dpi)
    content = (pytesseract.image_to_string(image=page) for page in pages)
    print('\n--page--\n'.join(content))
