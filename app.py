from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/print_photos', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num_photos = request.form['num_photos']
        # Call your Python function to generate the passport photos
        return render_template('results.html', num_photos=num_photos)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
