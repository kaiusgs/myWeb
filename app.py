from flask import Flask,render_template,url_for,redirect
<<<<<<< HEAD
=======
import time
>>>>>>> a60089c4137b3e51b512eabc319d6d7f6571492a

app = Flask(__name__)

@app.route('/')
def goldentime():
    return render_template('goldentime.html')

@app.route('/drink')
def drink():
    return render_template('drink.html')

<<<<<<< HEAD
=======
@app.route('/drink/game')
def game():
    t = int( time.strftime("%H", time.localtime()) )
    if t>=5 and t<20:
        return render_template('Nogame.html')
    return render_template('game.html')

@app.route('/drink/game1')
def game1():
    t = int( time.strftime("%H", time.localtime()) )
    if t>=5 and t<20:
        return render_template('Nogame.html')
    return render_template('game1.html')

@app.route('/drink/game2')
def game2():
    t = int( time.strftime("%H", time.localtime()) )
    if t>=5 and t<20:
        return render_template('Nogame.html')
    return render_template('game2.html')

@app.route('/drink/game3')
def game3():
    t = int( time.strftime("%H", time.localtime()) )
    if t>=5 and t<20:
        return render_template('Nogame.html')
    return render_template('game3.html')

@app.route('/drink/game4')
def game4():
    t = int( time.strftime("%H", time.localtime()) )
    if t>=5 and t<20:
        return render_template('Nogame.html')
    return render_template('game4.html')

@app.route('/drink/game5')
def game5():
    t = int( time.strftime("%H", time.localtime()) )
    if t>=5 and t<20:
        return render_template('Nogame.html')
    return render_template('game5.html')


>>>>>>> a60089c4137b3e51b512eabc319d6d7f6571492a
@app.route('/love')
def love():
    return render_template('love.html')

@app.route('/changsha')
def changsha():
    return render_template('changsha.html')


