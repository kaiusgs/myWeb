from flask import Flask,render_template,url_for,redirect
import time

app = Flask(__name__)

# 默认页
@app.route('/')
def goldentime():
    return render_template('goldentime.html')

@app.route('/love')
def love():
    return render_template('love.html')

@app.route('/changsha')
def changsha():
    return render_template('changsha.html')

@app.route('/drink')
def drink():
    return render_template('drink/drink.html')

# 喝酒游戏
# @app.route('/drink/game')
# def game():
#     t = int( time.strftime("%H", time.localtime()) )
#     if t>20 or t<12:
#         return render_template('Nogame.html')
#     return render_template('game.html')

# @app.route('/drink/game1')
# def game1():
#     t = int( time.strftime("%H", time.localtime()) )
#     if t>20 or t<12:
#         return render_template('Nogame.html')
#     return render_template('game1.html')

# @app.route('/drink/game2')
# def game2():
#     t = int( time.strftime("%H", time.localtime()) )
#     if t>20 or t<12:
#         return render_template('Nogame.html')
#     return render_template('game2.html')

# @app.route('/drink/game3')
# def game3():
#     t = int( time.strftime("%H", time.localtime()) )
#     if t>20 or t<12:
#         return render_template('Nogame.html')
#     return render_template('game3.html')

# @app.route('/drink/game4')
# def game4():
#     t = int( time.strftime("%H", time.localtime()) )
#     if t>20 or t<12:
#         return render_template('Nogame.html')
#     return render_template('game4.html')

# @app.route('/drink/game5')
# def game5():
#     t = int( time.strftime("%H", time.localtime()) )
#     if t>20 or t<12:
#         return render_template('Nogame.html')
#     return render_template('game5.html')

# Wang Xuanzhi 的简历
@app.route('/cv_cn_zhi')
def fun4():
    return render_template('zhi/cv_cn_zhi.html')

@app.route('/cv_en_zhi')
def fun5():
    return render_template('zhi/cv_en_zhi.html')

@app.route('/shiseido_report_zhi')
def fun1():
    return render_template('zhi/shiseido_report_zhi.html')

@app.route('/investment_research_report_zhi')
def fun2():
    return render_template('zhi/investment_research_report_zhi.html')

@app.route('/bp_zhi')
def fun3():
    return render_template('zhi/bp_zhi.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8088)