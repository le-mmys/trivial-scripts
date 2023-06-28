import PyPDF2
import os
import argparse

def extractpages(original_path, start_page, end_page, output_path):
    original_path = os.path.expanduser(original_path)
    output_path = os.path.expanduser(output_path)
    start_page = int(start_page)
    end_page = int(end_page)
    with open(original_path,'rb') as original_pdf:
        reader = PyPDF2.PdfReader(original_pdf)
        writer = PyPDF2.PdfWriter()
        for page_num in range(start_page-1, end_page):
            page = reader.pages[page_num]
            writer.add_page(page)

        with open(output_path, 'wb') as output_pdf:
            writer.write(output_pdf)

# original_path = "~/Documents/Sheldon Ross - A First Course in Probability-Pearson (2009).pdf"
# start_page = 1
# end_page = 2
# output_path = "~/Documents/Testresult.pdf"

def main():
    parser = argparse.ArgumentParser(description="PDF page extractor")
    parser.add_argument("original_path", help = "")
    parser.add_argument("start_page", help = "")
    parser.add_argument("end_page", help = "")
    parser.add_argument("output_path", help = "")
    args = parser.parse_args()
    extractpages(args.original_path, args.start_page, args.end_page, args.output_path)



if __name__ == "__main__":
    main()
