from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

from dotenv import load_dotenv
from google.cloud import vision
import io
import os

load_dotenv()

app = Flask(__name__)
client = vision.ImageAnnotatorClient()


@app.route('/')
def index():
    return render_template('index.html')


def search_by_image(img):
    response = client.label_detection(image=img)
    print(response)
    labels = response.label_annotations

    print('Labels:')
    label_found = []
    for label in labels:
        print(label.description)
        label_found.append(
            f"https://www.google.com/search?q={label.description}")
    return set(label_found)


def search_by_text(img):
    response = client.text_detection(image=img)
    texts = response.text_annotations
    print('Texts:')

    text_found = []
    for text in texts:
        for t in text.description.split("\n"):
            if t == '':
                continue
            text_found.append(f"https://www.google.com/search?q={t}")
    return set(text_found)


@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    option = request.form.getlist('options')

    print(option, uploaded_file)
    if len(option) == 0 or uploaded_file.filename == '':
        return render_template('error.html')

    uploaded_file.save(secure_filename(uploaded_file.filename))

    with io.open(uploaded_file.filename, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    if option[0] == "text":
        ans = search_by_text(image)
    else:
        ans = search_by_image(image)

    return render_template('index.html', data=ans)


if __name__ == '__main__':
    app.run(threaded=True, host="0.0.0.0",
            port=int(os.environ.get("PORT", 8080)))
