from flask import Flask, render_template, request, redirect, url_for
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageOps

app = Flask(__name__, template_folder='')


@app.route('/')
def index():
    return render_template('index.html')

def create_passport_photo_sheet(num_photos: int, output_format: str):
    output_format2 = output_format
    num_photos2:int = num_photos
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
    num_photos = num_photos2
    # num_photos = int(input("Enter the number of photos to print (8, 12, or 16): "))

    # Define the size of the margin and its color
    margin_size = 1
    margin_color = (0, 0, 0)

    if num_photos == 8:
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

    elif num_photos == 12:
        # Paste the input image onto the A4 image in a 3x4 grid
        for row in range(3):
            for col in range(4):
                x = col * (photo_size[0] + 100) + 200
                y = row * (photo_size[1] + 100) + 200
                resized_image = input_image.resize(photo_size)

                # Create a new image with a black margin

                padded_size = (photo_size[0] + margin_size * 2, photo_size[1] + margin_size * 2)
                padded_image = Image.new("RGB", padded_size, margin_color)
                padded_image.paste(resized_image, (margin_size, margin_size))

                a4_image.paste(padded_image, (x, y))

    elif num_photos == 16:
        # Paste the input image onto the A4 image in a 4x4 grid
        for row in range(4):
            for col in range(4):
                x = col * (photo_size[0] + 100) + 200
                y = row * (photo_size[1] + 100) + 200
                resized_image = input_image.resize(photo_size)

                # Create a new image with a black margin
                padded_size = (photo_size[0] + margin_size * 2, photo_size[1] + margin_size * 2)
                padded_image = Image.new("RGB", padded_size, margin_color)
                padded_image.paste(resized_image, (margin_size, margin_size))

                a4_image.paste(padded_image, (x, y))

    elif num_photos == 20:
        # Calculate the total available space on the A4 sheet
        total_width = a4_size[0] - 2 * 100  # Subtract the left and right margins
        total_height = a4_size[1] - 2 * 100  # Subtract the top and bottom margins

        # Calculate the total width and height of the photos based on the number of photos
        num_rows = num_photos // 4
        num_cols = 4
        if num_photos == 20:
            num_rows = 5
        photo_width = num_cols * photo_size[0] + (num_cols - 1) * 100
        photo_height = num_rows * photo_size[1] + (num_rows - 1) * 50

        # Calculate the left and right margins for centering the photo grid horizontally
        left_margin = (total_width - photo_width) // 2 + 100
        right_margin = total_width - left_margin - photo_width

        # Calculate the top margin for centering the photo grid vertically
        top_margin = (total_height - photo_height) // 2 + 100

        # Paste the input image onto the A4 image in a grid
        for row in range(num_rows):
            for col in range(num_cols):
                x = left_margin + col * (photo_size[0] + 100)
                y = top_margin + row * (photo_size[1] + 50)
                resized_image = input_image.resize(photo_size)

                # Create a new image with a black margin
                padded_size = (photo_size[0] + margin_size * 2, photo_size[1] + margin_size * 2)
                padded_image = Image.new("RGB", padded_size, margin_color)
                padded_image.paste(resized_image, (margin_size, margin_size))

                a4_image.paste(padded_image, (x, y))


    else:
        print("Invalid number of photos selected. Please select 8, 12, or 16.")
        exit()

        # Prompt the user to enter the desired output file format
    output_format = output_format2
    # output_format = input("Enter the desired output file format (e.g. jpeg, png, etc.): ")

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

  # redirect to the initial page
    return redirect(url_for('index'))

@app.route('/print_photos', methods=['POST'])
def print_photos_post():
    num_photos = request.form['num_photos']
    output_format: str = request.form['output_format']
    if num_photos and output_format:
        create_passport_photo_sheet(int(num_photos), output_format)
    else:
        print("Please provide both number of photos and output format.")
    # Call the create_passport_photo_sheet function with the retrieved values

    # Call the create_passport_photo_sheet function with the retrieved values

    # Use the retrieved value to perform the necessary logic
    # ...
    # return 'Photos printed: ' + num_photos + "\t\t\t" + output_format
    # redirect to the initial page
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='localhost', port=9874, debug=True)



