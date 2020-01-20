- Make sure tesseract is installed and is executable. see: https://github.com/tesseract-ocr/tesseract/wiki
- Sample commands:
    - Use default dpi:
        - `(venv)$ python ./pdf_to_text.py "./data/Adv.pdf"`
    - Specify a dpi value:
        - `(venv)$ python ./pdf_to_text.py -d 200 "./data/Adv.pdf"`