# 20CE075 PARTH PARMAR
# Practical 10: Generate PDF file of your 3rd Semester Mark-sheet
# https://github.com/Morningstar000/Python-Practical-10

import img2pdf
from PIL import Image

# storing img path
img_path = "C:/Users/parth/Pictures/result.jpg"

# storing pdf path
pdf_path = "C:/Users/parth/Pictures/practical10.pdf"

# opening image
image = Image.open(img_path)

# converting into chunks
pdf_bytes = img2pdf.convert(image.filename)

# opening file
file = open(pdf_path, "wb")

# writing pdf file with chunks
file.write(pdf_bytes)

# closing image and file
image.close()
file.close()
