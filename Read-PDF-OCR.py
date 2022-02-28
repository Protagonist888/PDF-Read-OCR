import time
from PIL import Image
import pytesseract
import sys
from pdf2image import convert_from_path
import os
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

PDF_file = "Johnsgard1988.pdf"

# Part1: Converting PDF to images

# Timer to calculate time to finish this step. Can be large if PDF has many pages

start1 = time.time()

# Store all the pages of the PDF in a variable
pages = convert_from_path(PDF_file, 500, first_page=1, last_page=100)

end1 = time.time()
print((end1-start1)/60)

# Counter to store images of each page of PDF
image_counter = 1

# Iterate through all pages

for page in pages:
    # Declare filename for each page of PDF as JPG
    # PDF page n -> page_n.jpg
    filename = "page_"+str(image_counter)+".jpg"
    page.save(filename, 'JPEG')
    image_counter = image_counter + 1

# Recognizing text from images using OCR

# Variable to get count of total number of pages
filelimit = image_counter-1

# Creating a text file to write output
outfile = 'out_text.txt'

# Open file in append mode so that all contents of all images are added to same file
f = open(outfile, "a")

# Iterate from 1 to total number of pages
start2 = time.time()
for i in range(1, filelimit + 1):

    filename = "page_"+str(i)+".jpg"

    # Recognize the text as string in image using pytesseract
    text = str(((pytesseract.image_to_string(Image.open(filename)))))

    text = text.replace('-\n', '')

    # Write processed text to the file.
    f.write(text)

f.close()

end2 = time.time()
print((end2-start2)/60)
