import os

from flask import Flask

def create_app(config_type):
    # create and configure the app
    app = Flask(__name__)
  
    config_file = os.path.join(os.getcwd() + '/config', config_type + '.py')
    app.config.from_pyfile(config_file)

    return app
