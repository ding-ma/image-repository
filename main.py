from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
from google.cloud import vision
import io

load_dotenv()

app = Flask(__name__)
client = vision.ImageAnnotatorClient()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    option = request.form.getlist('options')

    print(option, uploaded_file)
    with io.open(uploaded_file.filename, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.label_detection(image=image)
    print(response)
    labels = response.label_annotations

    print('Labels:')
    for label in labels:
        print(label.description)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
