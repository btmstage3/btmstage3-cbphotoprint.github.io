from PIL import Image
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/print_photos', methods=['POST'])
def print_photos():
    # Get the selected number of photos from the form
    num_photos = int(request.form['num_photos'])
    print(num_photos)
    # Add the rest of your code here to print the photos

    return 'Photos printed successfully!'

if __name__ == '__main__':
    app.run(debug=True)
