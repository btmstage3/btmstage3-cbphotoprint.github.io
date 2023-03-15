from PIL import Image
import tkinter as tk
from tkinter import filedialog

# Create a file dialog box to select the input photo
root = tk.Tk()
root.withdraw()
input_file_path = filedialog.askopenfilename(filetypes=[("JPEG files", "*.jpg")])

# Open the input image file
input_image = Image.open(input_file_path)

# Create a new A4 size image with white background
a4_size = (2480, 3508)  # A4 size in pixels (300 dpi)
a4_image = Image.new("RGB", a4_size, "white")

# Calculate the size of each passport photo
photo_size = (450, 600)

# Prompt the user to select the number of photos to print
num_photos = int(input("Enter the number of photos to print (8, 12, or 16): "))

if num_photos == 8:
    # Paste the input image onto the A4 image in a 2x4 grid
    for row in range(2):
        for col in range(4):
            x = col * (photo_size[0] + 100) + 200
            y = row * (photo_size[1] + 100) + 200
            resized_image = input_image.resize(photo_size)
            a4_image.paste(resized_image, (x, y))

elif num_photos == 12:
    # Paste the input image onto the A4 image in a 3x4 grid
    for row in range(3):
        for col in range(4):
            x = col * (photo_size[0] + 100) + 200
            y = row * (photo_size[1] + 100) + 200
            resized_image = input_image.resize(photo_size)
            a4_image.paste(resized_image, (x, y))

elif num_photos == 16:
    # Paste the input image onto the A4 image in a 4x4 grid
    for row in range(4):
        for col in range(4):
            x = col * (photo_size[0] + 100) + 200
            y = row * (photo_size[1] + 100) + 200
            resized_image = input_image.resize(photo_size)
            a4_image.paste(resized_image, (x, y))

else:
    print("Invalid number of photos selected. Please select 8, 12, or 16.")
    exit()

    # Prompt the user to enter the desired output file format
output_format = input("Enter the desired output file format (e.g. jpeg, png, etc.): ")

# Create a file dialog box to select the output file location
output_file_path = filedialog.asksaveasfilename(defaultextension=output_format.lower(),
                                                filetypes=[(output_format.upper(), f"*.{output_format.lower()}")])

if output_format.lower() == "pdf":
    # Save the output as a PDF file
    a4_image.save(output_file_path, "PDF", resolution=300.0)

elif output_format.lower() == "word":
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