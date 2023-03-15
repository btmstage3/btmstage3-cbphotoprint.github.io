from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/print_photos', methods=['POST'])
def execute():
    # Call your Python file using subprocess
    subprocess.call(['python', 'print-photos.py'])
    return 'Python file executed successfully!'


@app.route('/print_photos', methods=['POST'])
def print_photos():
    num_photos = request.form['num_photos']
    # Call your Python function to generate the passport photos
    return render_template('results.html', num_photos=num_photos)

if __name__ == '__main__':
    app.run(debug=True)
