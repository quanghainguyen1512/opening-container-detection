from src.app import app
from src.constants import ROOT_PATH
import os


if __name__ == "__main__":
    application = app
    application.config.from_object('src.config.BaseConfig')

    static = os.path.join(ROOT_PATH, 'static')
    if not os.path.exists(static):
        os.makedirs(static)

    upload = os.path.join(ROOT_PATH, application.config['UPLOAD_FOLDER'])
    if not os.path.exists(upload):
        os.makedirs(upload)
    
    application.run()
