from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
import numpy as np
import os

app = Flask(__name__)

# Carpeta donde se guardan las imágenes cargadas
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return redirect(request.url)
    
    file = request.files['image']
    
    if file.filename == '':
        return redirect(request.url)

    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        
        # Convertir la imagen a matriz
        image = Image.open(filepath)
        matriz = np.array(image)
        
        # Convertir la matriz a una string para mostrarla
        matriz_str = str(matriz)

        return render_template('result.html', image_url=filepath, matriz=matriz_str)

if __name__ == '__main__':
    app.run(debug=True)

