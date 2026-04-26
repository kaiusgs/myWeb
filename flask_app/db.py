import sqlite3
from datetime import datetime

import click
from flask import current_app, g

# Connect to the database
def get_db():
    # g: a special object unique for each request 
    #    used to store data accessed by multiple functions during the request
    if 'db' not in g:
        g.db = sqlite3.connect(
            # current_app: points to the Flask application handling the request
            current_app.config['DATABASE'],
            detect_types = sqlite3.PARSE_DECLTYPES
        )

        # tells the connection to return rows that behave like dicts
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


# Reset the database and create the tables
def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


# defines a command line command called 'init-db'
@click.command('init-db')
def init_db_command():
    init_db()
    click.echo('Successfully initialized the database.')


# tells Python how to interpret timestamp values in the database 
sqlite3.register_converter(
    # convert the value to datetime.datetime
    "timestamp", lambda v: datetime.fromisoformat(v.decode())
)


# register these database functions with the application instance 
def init_app(app):
    # call close_db function when cleaning up after returning the response 
    app.teardown_appcontext(close_db)
    # add the command which can be called with the 'flask' command 
    app.cli.add_command(init_db_command)

