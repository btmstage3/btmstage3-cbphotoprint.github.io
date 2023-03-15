#!/usr/bin/env python

from PIL import Image
import os
import sys

# Get input from the web form
input_file_path = sys.argv[1]
num_photos = int(sys.argv[2])
output_format = sys.argv[3]
output_file_path = sys.argv[4]

# Open the input image file
input_image = Image.open(input_file_path)

# Create a new A4 size image with white background
a4_size = (2480, 3508)  # A4 size in pixels (300 dpi)
a4_image = Image.new("RGB", a4_size, "white")

# Calculate the size of each passport photo
photo_size = (450, 600)

# Define the size of the margin and its color
margin_size = 1
margin_color = (0, 0, 0)

# Paste the input image onto the A4 image in a 2x4 grid
for row in range(2):
    for col in range(4):
        x = col * (photo_size[0] + 100) + 200
        y = row * (photo_size[1] + 100) + 200
        resized_image = input_image.resize(photo_size)

        # Create a new image with a black margin
        padded_size = (photo_size[0] + margin_size * 2, photo_size[1] + margin_size * 2)
        padded_image = Image.new("RGB", padded_size, margin_color)
        padded_image.paste(resized_image, (margin_size, margin_size))

        a4_image.paste(padded_image, (x, y))

if output_format == "pdf":
    # Save the output as a PDF file
    a4_image.save(output_file_path, "PDF", resolution=300.0)

elif output_format == "word":
    # Save the output as a Word document (requires Python-Docx library)
    from docx import Document
    from docx.shared import Inches

    document = Document()
    section = document.sections[0]
    section.page_height = a4_size[1] / 300.0 * Inches(1)
    section.page_width = a4_size[0] / 300.0 * Inches(1)

    # Save the A4 image as a PNG file
    a4_image.save("output_photo.png")

    document.add_picture("output_photo.png", width=Inches(6), height=Inches(4))

    document.save(output_file_path)

else:
    # Save the output as an image file
    a4_image.save(output_file_path)

# Print a success message and the path to the output file
print("Success!")
print("The output file has been generated at: %s" % output_file_path)
