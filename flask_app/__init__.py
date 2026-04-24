import os
from flask import Flask

# application factory
def create_app(test_config = None):
    # create the app
    app = Flask(
        __name__, # the name of the current Python module
        instance_relative_config = True # configuration files are relative to the instance folder.
    )

    # configure the app 
    app.config.from_mapping(
        # sets some default configuration 
        SECRET_KEY = 'dev', # should be overridden with a random value when deploying
        DATABASE = os.path.join(app.instance_path, 'flask_app.sqlite'), # the path where the SQLite database file will be saved
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        # overrides the default configuration with values taken from the config.py file in the instance folder 
        app.config.from_pyfile('config.py', silent = True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    os.makedirs(app.instance_path, exist_ok = True)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # register database functions
    from . import db
    db.init_app(app)

    # register the authentication blueprint 
    from . import auth
    app.register_blueprint(auth.bp)

    return app
