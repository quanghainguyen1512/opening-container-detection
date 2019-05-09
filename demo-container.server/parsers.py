from flask_restplus import reqparse
import werkzeug

file_upload = reqparse.RequestParser()
file_upload.add_argument('images', type=werkzeug.datastructures.FileStorage, location='files', required='True', action='append')