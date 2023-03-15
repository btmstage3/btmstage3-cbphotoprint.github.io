import cv2
import tkinter as tk
from tkinter import filedialog

# Create a file dialog box to select the input photo
root = tk.Tk()
root.withdraw()
input_file_path = filedialog.askopenfilename(filetypes=[("JPEG files", "*.jpg")])

# Load the input image
input_image = cv2.imread(input_file_path)

# Load the Haar cascade classifier for face detection
face_cascade = cv2.CascadeClassifier('https://github.com/opencv/opencv/blob/0052d46b8e33c7bfe0e1450e4bff28b88f455570/data/haarcascades/haarcascade_frontalface_default.xml')
# Detect faces in the input image
faces = face_cascade.detectMultiScale(input_image, scaleFactor=1.1, minNeighbors=5)

# Crop the image based in the center of the first detected face
if len(faces) > 0:
    x, y, w, h = faces[0]
    center_x = x + w // 2
    center_y = y + h // 2
    crop_width = 450
    crop_height = 600
    crop_x = max(center_x - crop_width // 2, 0)
    crop_y = max(center_y - crop_height // 2, 0)
    output_image = input_image[crop_y:crop_y+crop_height, crop_x:crop_x+crop_width]

    # Create a file dialog box to select the output location
    output_file_path = filedialog.asksaveasfilename(defaultextension='.jpg', filetypes=[("JPEG files", "*.jpg")])

    # Save the cropped image
    cv2.imwrite(output_file_path, output_image)
