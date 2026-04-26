import functools

# A view function is the code you write to respond to requests to your application
# A Blueprint is a way to organize a group of related views and other code

# Views and other code are registered with a blueprint, 
# Then the blueprint is registered with the application when it is available

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flask_app.db import get_db

# Create a Blueprint
bp = Blueprint(
    'auth', 
    __name__, 
    # The url_prefix will be prepended to all the URLs associated with the blueprint.
    url_prefix = '/auth'
)

@bp.route('/register', methods=('GET', 'POST'))
def register():

    # the user submitted the form. start validating the input.
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        error = None
        # validate that username and password are not empty.
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        # try to insert the new user data into the database.
        db = get_db()
        if error is None:
            try:
                # execute SQL query 
                db.execute( 
                    "INSERT INTO user (username, password) VALUES (?, ?)", # ? is the placeholder
                    (username, generate_password_hash(password)), # use tuple to replace placeholders 
                    # generate_password_hash: securely hash the password
                )
                # if data is modified, we need to commit the changes 
                db.commit()
            except db.IntegrityError: # uniqueness
                error = f"User {username} is already registered."
            else:
                # url_for generates the URL for the login view based on its name 
                # it allows the changes of the URL on only one spot (not here)
                # The name associated with a view is also called the endpoint, 
                # by default the endpoint is blueprint_name.function_name
                return redirect(url_for("auth.login")) 

        # show the error to the user
        flash(error)

    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login(): 
    # if log in successfully, the user’s id will be stored in the session

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        db = get_db()
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
            # fetchone: returns one row from the query
            # fetchall: returns a list of all results
        ).fetchone()

        error = None
        if user is None:
            error = 'Incorrect username or password.'
        elif not check_password_hash(user['password'], password):
            # hashes the submitted password and compares them. If they match, the password is valid.
            error = 'Incorrect username or password.'

        if error is None:
            # session is a dict that stores data across requests 
            # The data is stored in a cookie that is sent to the browser, 
            # and the browser then sends it back with subsequent requests.
            # Flask securely signs the data so that it can’t be tampered with
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')

# user's information should be loaded for other views if logged in
# bp.before_app_request() registers a function that runs before the view function, 
#   no matter what URL is requested
@bp.before_app_request 
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

@bp.route('/logout')
def logout():
    # remove the user id from the session
    session.clear()
    return redirect(url_for('index'))


# check if the user is logged in for the view it’s applied to.
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view

