from flask import Flask, Response, url_for, redirect
from flask_restplus import Api, Resource, abort
from flask_cors import CORS
from werkzeug.utils import secure_filename

from keras_retinanet.utils.image import read_image_bgr
import tensorflow as tf
import parsers
import os
import json

from config import BaseConfig
from detector import detect
from utils import load_model
from constants import ROOT_PATH

app = Flask(__name__)

CORS(app=app)
api = Api(app, version='1.0', title='Demo API', validate=False)
ns = api.namespace('api', description='api')

graph = tf.get_default_graph()

@ns.route('/')
class HelloWorld(Resource):
    def get(self):
        return {'message': 'HelloWorld'}

@ns.route('/upload')
class FileUpload(Resource):
    @ns.expect(parsers.file_upload)
    def post(self):
        # data = pars.parse_args()
        if model is None:
            abort(404, 'Model not loaded')

        if len(os.listdir(os.path.join(ROOT_PATH, 'static'))) > 0: 
            os.system('rm {}/*'.format(static))

        upload = os.path.join(ROOT_PATH, app.config['UPLOAD_FOLDER'])
        data = parsers.file_upload.parse_args()
        paths = []
        
        if data['images']:
            for index, img in enumerate(data['images']):
                mime = img.mimetype
                if mime == 'image/jpeg' or mime == 'image/png':
                    imname = secure_filename(img.filename)
                    p = os.path.join(upload, imname)
                    paths.append(p)
                    img.save(p)
                else:
                    abort(400)
        elif data['links']:
            pass
        try:
            if len(paths) == 0:
                abort(400, 'No image loaded')
            urls = detect(graph, model, paths)
            return {
                'status': '{} file processed'.format(index + 1),
                'images': urls
            }, 201
        except Exception as e:
            abort(500, str(e))
        

model = None
if __name__ == "__main__":
    model = load_model()
    
    app.config.from_object('config.BaseConfig')

    static = os.path.join(ROOT_PATH, 'static')
    if not os.path.exists(static):
        os.makedirs(static)

    upload = os.path.join(ROOT_PATH, app.config['UPLOAD_FOLDER'])
    if not os.path.exists(upload):
        os.makedirs(upload)
    
    app.run()