import os
import uuid

import pyautogui
import tkinter as tk
from tkinter import filedialog
from PIL import Image

# Define the size of the custom crop
crop_size = (450, 600)

# Create a file dialog box to select the input photo
root = tk.Tk()
root.withdraw()
input_file_path = filedialog.askopenfilename(filetypes=[("JPEG files", "*.jpg")])

# Open the input image file
input_image = Image.open(input_file_path)

# Open the input image file in an external editor (in this case, Microsoft Paint on Windows)
os.startfile(input_file_path)

# Wait for the external editor to open and become active
pyautogui.sleep(1)

# Simulate keyboard and mouse clicks to perform the crop operation
pyautogui.hotkey('ctrl', 'e')
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'w')
pyautogui.press('enter')
pyautogui.sleep(1)
pyautogui.click(100, 100)
pyautogui.dragTo(550, 700, button='left')
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('ctrl', 'n')
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('ctrl', 's')
pyautogui.press('enter')
pyautogui.sleep(1)



# Generate a unique name for the output file
output_file_name = str(uuid.uuid4()) + '.jpg'

# Get the directory of the input file
input_file_directory = os.path.dirname(input_file_path)





# Get the file name of the output image
output_file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg")])

# Load the cropped image from the output file
cropped_image = Image.open(output_file_path).resize(crop_size)

# Save the cropped image with the unique name in the same directory as the input file
output_file_path = os.path.join(input_file_directory, output_file_name)
cropped_image.save(output_file_path)