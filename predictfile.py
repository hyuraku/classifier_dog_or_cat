import os
from flask import Flask, request, redirect, url_for
from keras.models import Sequential,load_model
from werkzeug.utils import secure_filename
import keras
import sys
import numpy as np
from PIL import Image

classes = ["dog", "cat"]
num_classes = len(classes)
image_size = 50

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            # flash('No file!')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file!')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            model = load_model('./animal_cnn.h5')

            image=Image.open(filepath)
            image=image.convert('RGB')
            image=image.resize((image_size,image_size))
            data=np.asarray(image)
            X=[]
            X.append(data)
            X=np.array(X)

            result = model.predict([X])[0]
            predicted=result.argmax()
            percenrage=int(result[predicted]*100)

            return classes[predicted] + str(percenrage) + '%'

    return '''
    <!doctype html>
    <html><head>
    <meta charset–'UTF-8'>
    <title>Upload new File</title></head>
    <body>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </body>
    </html>
    '''

from flask import send_from_directory

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
