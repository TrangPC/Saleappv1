import os.path

from flask import Flask, Blueprint, request, jsonify
from minio import Minio
from minio.error import ServerError
app = Blueprint('minio_manager', __name__)
MINIO_ENDPOINT= 'localhost:9000'
MINIO_ACCESS_KEY = 'minioadmin'
MINIO_SECRET_KEY = 'minioadmin'
minio_client = Minio(MINIO_ENDPOINT, access_key=MINIO_ACCESS_KEY, secret_key=MINIO_SECRET_KEY, secure=False)

IMG_FOLDER = './static/images'
app.config['UPLOAD_FOLDER'] = IMG_FOLDER
@app.route('/upload-image', methods = ['POST'])
def upload():
    if 'img' not in request.files:
        return jsonify('error: No file'), 400
    file = request.files['img']
    if file.filename:
        try:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            with open(file_path, 'rb') as data:
                minio_client.put_object('images', file.filename, data, length=os.path.getsize(file_path), content_type=file.content_type)
                os.remove(file_path)
                img_url = minio_client.presigned_get_object('images', file.filename)
                return jsonify({'img_url': img_url}), 200
        except ServerError as e:
          return jsonify('error:' + str(e)), 500

    else:
        return jsonify('error: no file selected'), 400


