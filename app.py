from flask import Flask,render_template,url_for,redirect
import time

app = Flask(__name__)

@app.route('/shiseido_report_zhi')
def fun1():
    return render_template('shiseido_report_zhi.html')

@app.route('/investment_research_report_zhi')
def fun2():
    return render_template('investment_research_report_zhi.html')

@app.route('/bp_zhi')
def fun3():
    return render_template('bp_zhi.html')

@app.route('/cv_cn_zhi')
def fun4():
    return render_template('cv_cn_zhi.html')

@app.route('/cv_en_zhi')
def fun5():
    return render_template('cv_en_zhi.html')

'''

@app.route('/')
def goldentime():
    return render_template('goldentime.html')

@app.route('/drink')
def drink():
    return render_template('drink.html')
'''
@app.route('/drink/game')
def game():
    t = int( time.strftime("%H", time.localtime()) )
    if t>20 or t<12:
        return render_template('Nogame.html')
    return render_template('game.html')

@app.route('/drink/game1')
def game1():
    t = int( time.strftime("%H", time.localtime()) )
    if t>20 or t<12:
        return render_template('Nogame.html')
    return render_template('game1.html')

@app.route('/drink/game2')
def game2():
    t = int( time.strftime("%H", time.localtime()) )
    if t>20 or t<12:
        return render_template('Nogame.html')
    return render_template('game2.html')

@app.route('/drink/game3')
def game3():
    t = int( time.strftime("%H", time.localtime()) )
    if t>20 or t<12:
        return render_template('Nogame.html')
    return render_template('game3.html')

@app.route('/drink/game4')
def game4():
    t = int( time.strftime("%H", time.localtime()) )
    if t>20 or t<12:
        return render_template('Nogame.html')
    return render_template('game4.html')

@app.route('/drink/game5')
def game5():
    t = int( time.strftime("%H", time.localtime()) )
    if t>20 or t<12:
        return render_template('Nogame.html')
    return render_template('game5.html')

'''
@app.route('/love')
def love():
    return render_template('love.html')

@app.route('/changsha')
def changsha():
    return render_template('changsha.html')

'''

