import os
from flask import Flask

# application factory
def create_app(test_config = None):
    # create the app
    app = Flask(
        __name__, # the name of the current Python module
        static_folder = '../static',
        template_folder = "../templates",
        instance_relative_config = True # configuration files are relative to the instance folder.
    )

    # configure the app 
    app.config.from_mapping(
        # sets some default configuration 
        SECRET_KEY = 'dev', # should be overridden with a random value when deploying
        DATABASE = os.path.join(app.instance_path, 'flask_app.sqlite'), # the path where the SQLite database file will be saved
        # app.instance_path: By default the folder 'instance' next to the package or module is assumed to be the instance path.
    )

    if test_config is None:
        # load the instance config if it exists, when not testing
        # overrides the default configuration with values taken from the config.py file in the instance folder 
        app.config.from_pyfile('config.py', silent = True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    os.makedirs(app.instance_path, exist_ok = True)

    # # a simple page that says hello
    # @app.route('/hello')
    # def hello():
    #     return 'Hello, World!'

    # register database functions
    from . import db
    db.init_app(app)

    # register the authentication blueprint 
    from . import auth
    app.register_blueprint(auth.bp)

    # register the blog blueprint 
    from . import blog
    app.register_blueprint(blog.bp)
    # add_url_rule: associates the endpoint name 'index' with the / url 
    app.add_url_rule('/', endpoint = 'index')

    return app

# ******************************
# Few notes about Jinja 
# 
# In Flask, Jinja is configured to autoescape any data that is rendered in HTML templates
# This means that it’s safe to render user input, including '<' and '>'
# they will be escaped with safe values that look the same in the browser 
# 
# Anything between {{ and }} is an expression that will be output to the final document
# {% and %} denotes a control flow statement like if and for
# ****************************** 
