from flask import current_app as flask_app

DEBUG = False
SQLALCHEMY_DATABASE_URI = flask_app.config['JAWSDB_URL']