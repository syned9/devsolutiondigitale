# from flask import Flask
# current_app = Flask(__name__)

# import routes

# current_app.run(debug=True)

import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    with app.app_context():
        from app import routes
        from app import db
        engine = db.get_connection()
        db.createTable(engine)
    # a simple page that says hello
    # @app.route('/')
    # def hello():
    #     return 'Hello, World!'

    return app