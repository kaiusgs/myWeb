from flask import Flask,render_template,url_for,redirect

app = Flask(__name__)

@app.route('/')
def goldentime():
    return render_template('goldentime.html')

@app.route('/drink')
def drink():
    return render_template('drink.html')

@app.route('/love')
def love():
    return render_template('love.html')

@app.route('/changsha')
def changsha():
    return render_template('changsha.html')


