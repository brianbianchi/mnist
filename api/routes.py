from flask import Flask, Response, request, jsonify

from api.utils import get_prediction, transform_image

app = Flask("__name__")

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
def allowed_file(filename):
    # xxx.png
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files.get('file')
        if file is None or file.filename == "":
            return jsonify({'error': 'no file'}), 400
        if not allowed_file(file.filename):
            return jsonify({'error': 'format not supported'}), 400

        try:
            img_bytes = file.read()
            tensor = transform_image(img_bytes)
            prediction = get_prediction(tensor)
            data = {'prediction': prediction.item(), 'class_name': str(prediction.item())}
            return jsonify(data), 200
        except:
            return jsonify({'error': 'error during prediction'}), 500