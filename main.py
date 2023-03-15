from PIL import Image
import tkinter as tk
from tkinter import filedialog

# Create a file dialog box to select the input photo
root = tk.Tk()
root.withdraw()
input_file_path = filedialog.askopenfilename(filetypes=[("JPEG files", "*.jpg")])

# Open the input image file
input_image = Image.open(input_file_path)

# Prompt the user to enter the number of photos they want to print
num_photos = int(input("Enter the number of photos to print: "))

# Create a new A4 size image with white background
a4_width = 2480  # A4 width in pixels (300 dpi)
a4_height = 3508  # A4 height in pixels (300 dpi)
a4_image = Image.new("RGB", (a4_width, a4_height), "white")

# Calculate the size of each passport photo
photo_width = int(a4_width / 4) - 50
photo_height = int(a4_height / 2) - 50

# Resize the input image to fit the passport photo size
input_image = input_image.resize((photo_width, photo_height))

# Calculate the position of the first photo
x = 25
y = 25

# Paste the input image onto the A4 image in a 2x4 grid
for i in range(num_photos):
    a4_image.paste(input_image, (x, y))
    x += photo_width + 50
    if i == 3:
        x = 25
        y = photo_height + 75

# Prompt the user to save the output in their preferred format
output_format = input("Enter the desired output format (PDF, Word, Image or PNG): ")

# Create a file dialog box to select the output file location
output_file_path = filedialog.asksaveasfilename(defaultextension=output_format.lower(), filetypes=[(output_format.upper(), f"*.{output_format.lower()}")])

if output_format.lower() == "pdf":
    # Save the output as a PDF file
    a4_image.save(output_file_path, "PDF", resolution=300.0)

elif output_format.lower() == "word":
    # Save the output as a Word document (requires Python-Docx library)
    from docx import Document
    from docx.shared import Inches

    document = Document()
    section = document.sections[0]
    section.page_height = a4_height / 300.0 * Inches(1)
    section.page_width = a4_width / 300.0 * Inches(1)

    # Save the A4 image as a PNG file
    a4_image.save("output_photo.png")

    document.add_picture("output_photo.png", width=Inches(6), height=Inches(4))

    document.save(output_file_path)

else:
    # Save the output as an image file
    a4_image.save(output_file_path)
