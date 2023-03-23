# btmstage3.github.io

#Passport Size Photo Generator

This is a simple command-line tool that allows you to quickly generate passport size photos in various output formats. Simply provide an input image, specify the number of copies you want to generate, and choose an output format. The tool will produce high-quality passport photos in no time, saving you the hassle of going to a photo studio.

Installation
To use this tool, you need to have Python 3 installed on your system. You can download Python from the official website: https://www.python.org/downloads/

Once you have Python installed, you can install the Passport Size Photo Generator tool by following these steps:

Clone this repository to your local machine using Git or download the ZIP file and extract it to a folder.

Open a terminal or command prompt and navigate to the folder where the repository is located.

Install the required dependencies by running the following command:

 
pip install -r requirements.txt
This will install the Pillow library, which is used for image processing.

Usage
To generate passport size photos, run the generate.py script in a terminal or command prompt. The script takes three arguments:

--input or -i: The path to the input image file. This can be a JPEG, PNG, or BMP file.

--copies or -c: The number of copies you want to generate. This should be a positive integer.

--format or -f: The output format you want to use. This can be one of the following:

jpg: JPEG format
png: PNG format
bmp: BMP format
If you don't specify an output format, the tool will use the same format as the input image.

For example, to generate two JPEG-format passport size photos from an input image file named input.jpg, run the following command:

css
 
python generate.py --input input.jpg --copies 2 --format jpg
The tool will create two new files in the same directory as the input file, named input_1.jpg and input_2.jpg.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contact
If you have any questions or suggestions about this tool, please feel free to contact me at [macromkarthick@gmail.com].
