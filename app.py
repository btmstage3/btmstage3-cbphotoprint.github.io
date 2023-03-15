from flask import Flask, request

app = Flask(__name__)

@app.route('/print_photos', methods=['POST'])
def print_photos():
    num_photos = request.form['num_photos']
    print(str(num_photos))
    # Use the retrieved value to perform the necessary logic
    # ...
    return 'Photos printed: ' + num_photos
