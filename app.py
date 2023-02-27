from flask import Flask,render_template,url_for,redirect
import time

app = Flask(__name__)

# 默认页
@app.route('/')
def index_page():
    return render_template('index.html')

# 短文
@app.route('/pdf1')
def pdf1():
    return render_template('rss2pdf/pdf1.html')

# 其他
@app.route('/goldentime')
def goldentime():
    return render_template('goldentime.html')

@app.route('/love')
def love():
    return render_template('love.html')

# 喝酒游戏
@app.route('/drink/game')
def game():
    # t = int( time.strftime("%H", time.localtime()) )
    # if t>20 or t<12:
    #     return render_template('drink/Nogame.html')
    return render_template('drink/game.html')

@app.route('/drink/game1')
def game1():
    # t = int( time.strftime("%H", time.localtime()) )
    # if t>20 or t<12:
    #     return render_template('drink/Nogame.html')
    return render_template('drink/game1.html')

@app.route('/drink/game2')
def game2():
    # t = int( time.strftime("%H", time.localtime()) )
    # if t>20 or t<12:
    #     return render_template('drink/Nogame.html')
    return render_template('drink/game2.html')

@app.route('/drink/game3')
def game3():
    # t = int( time.strftime("%H", time.localtime()) )
    # if t>20 or t<12:
    #     return render_template('drink/Nogame.html')
    return render_template('drink/game3.html')

@app.route('/drink/game4')
def game4():
    # t = int( time.strftime("%H", time.localtime()) )
    # if t>20 or t<12:
    #     return render_template('drink/Nogame.html')
    return render_template('drink/game4.html')

@app.route('/drink/game5')
def game5():
    # t = int( time.strftime("%H", time.localtime()) )
    # if t>20 or t<12:
    #     return render_template('drink/Nogame.html')
    return render_template('drink/game5.html')

# Wang Xuanzhi 的简历
@app.route('/cv_cn_zhi')
def cv_cn_zhi():
    return render_template('zhi/cv_cn_zhi.html')

@app.route('/cv_en_zhi')
def cv_en_zhi():
    return render_template('zhi/cv_en_zhi.html')

@app.route('/shiseido_report_zhi')
def shiseido_report_zhi():
    return render_template('zhi/shiseido_report_zhi.html')

@app.route('/investment_research_report_zhi')
def investment_research_report_zhi():
    return render_template('zhi/investment_research_report_zhi.html')

@app.route('/bp_zhi')
def bp_zhi():
    return render_template('zhi/bp_zhi.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8088)