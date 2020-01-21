""""
A script to test the accuracy of pdf to text script.
Sample data set is expected to be a directory of .pdf files with .txt files of same name n the same directory
containing the original text to be scanned.
"""
import argparse
from glob import glob

from utils.accuracy import diff_percentage
from utils.pdf import pdf_to_text, DEFAULT_DPI

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Test accuracy of pdf to text. Make sure each .pdf file in the data dir has a .txt file'
                    ' with the correct content.')
    parser.add_argument('dir', type=str, nargs=1, help='The path to the data set dir')
    parser.add_argument('--dpi', '-d',
                        metavar='D',
                        type=int, nargs=1, default=DEFAULT_DPI,
                        help=f"The dpi value to use while converting pdf into images. Defaults to {DEFAULT_DPI}.")

    args = parser.parse_args()
    data_dir = args.dir[0]
    dpi = args.dpi
    pdf_files = glob(f"{data_dir}/*.pdf")
    accuracy_data = []
    print(f"Processing sample set of {len(pdf_files)} files with dpi: {dpi}..")
    for file_path in pdf_files:
        with open(f"{file_path[:-3]}txt") as original_text_file:
            scanned_text = pdf_to_text(file_path=file_path, dpi=dpi)
            original_text = original_text_file.read()
            # result is a list of 2-tuples in the form: (%accuracy, file path)
            accuracy_data.append((diff_percentage(original_text, scanned_text), file_path))
    for data in accuracy_data:
        print(data)
