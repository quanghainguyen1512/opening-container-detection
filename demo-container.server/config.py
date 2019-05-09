import os

class BaseConfig:
    DEBUG = os.environ.get('FLASK_ENV', 'development') == 'development'
    ENV = os.environ.get('FLASK_ENV', 'development')
    PORT = os.environ.get('PORT', 5000)
    UPLOAD_FOLDER = 'upload'
    MAX_CONTENT_PATH = 2048