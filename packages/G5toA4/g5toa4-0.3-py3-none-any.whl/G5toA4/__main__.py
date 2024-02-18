#!/usr/bin/python3
# (C) 2024 Massimo Girondi girondi@kth.se - GNU GPL v3


from pypdf import *
from tqdm import tqdm
import sys
import os
import pathlib
import argparse
from reportlab.pdfgen.canvas import Canvas
import io
import datetime
import subprocess

parser = argparse.ArgumentParser(
    #:prog=sys.argv[0],
    prog="G5toA4",
    # formatter_class=argparse.RawTextHelpFormatter,
    description="Shrink a PDF G5 book into a A4, maintaining the real sizes.",
    epilog="(C) 2024 Massimo Girondi girondi@kth.se - GNU GPL v3")

parser.add_argument("input", help="Input filename")
parser.add_argument("output", help="Output file name", nargs="?")
args = parser.parse_args()

in_file = args.input
if (not in_file.endswith(".pdf")) and (not in_file.endswith(".pdf")):
    print("Warning! The input file should be a PDF, but it doesn't have a .pdf extension!")
    path = pathlib.Path(in_file)
    if not path.exists():
        print("Error: the input file doesn't exist!")
        exit(1)

if args.output:
    out_file = args.output
    path = pathlib.Path(out_file)
    if not path.parent.exists():
        print("Error: the output directory doesn't exist!")
        exit(1)
else:
    # Build the path with "A4" in the name
    path = pathlib.Path(in_file)
    out_file = str(path.parent / path.stem)
    out_file += ".A4.pdf"

pdf_reader = PdfReader(in_file)
pdf_writer = PdfWriter()

crop_l = Transformation()
crop_r = Transformation()

# How are pages moved inside the new page
crop_l = crop_l.translate(tx=-25, ty=-60)
crop_r = crop_r.translate(tx=380, ty=-60)

# The very first page will be on the right side
currentPage = PageObject().create_blank_page(width=PaperSize.A4.height, height=PaperSize.A4.width)

for page in tqdm(pdf_reader.pages):
    if currentPage:
        currentPage.merge_transformed_page(page, crop_r)
        pdf_writer.add_page(currentPage)
        currentPage = None
    else:
        currentPage = PageObject().create_blank_page(width=PaperSize.A4.height, height=PaperSize.A4.width)
        currentPage.merge_transformed_page(page, crop_l)

# Attach the last page if missing
if currentPage:
    pdf_writer.add_page(currentPage)

last_edit = datetime.datetime.fromtimestamp(os.stat(in_file).st_mtime)

# Try to get a md5sum of the file. But don't fail completely
# TODO: We should use md5 Python module to ensure portability!

try:
  md5_cmd = ["md5sum", in_file]
  md5_output = subprocess.check_output(md5_cmd).decode().split(" ")[0]
except Exception as ex:
  print("Error during md5sum:", ex)
  md5_output = None


# Build the report for the fist page

report = "cmdline: " + " ".join(sys.argv)
report += "\nInput file: " + str(pathlib.Path(in_file).resolve())
report += "\nInput pages: " + str(len(pdf_reader.pages))
report += "\nLast modification: " + str(last_edit.isoformat())

if md5_output:
  report += "\n\n" + " ".join(md5_cmd) + ":"
  report += "\n" + md5_output

report += "\n\nOutput file: " + str(pathlib.Path(out_file).resolve())
report += "\nFinished at: " + str(datetime.datetime.now().isoformat())
report += "\nOutput pages: " + str(len(pdf_writer.pages))

packet = io.BytesIO()
canvas = Canvas(packet)
canvas.setPageSize((1690, 2390))

textobject = canvas.beginText()
textobject.setTextOrigin(20, 180)
textobject.textLines(report)
canvas.drawText(textobject)
canvas.save()
packet.seek(0)
front = PdfReader(packet)

pdf_writer.pages[0].merge_page(front.pages[0])

print("Writing result to", out_file)
pdf_writer.write(out_file)
