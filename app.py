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

@app.route('/pdf2')
def pdf2():
    return render_template('rss2pdf/pdf2.html')

@app.route('/pdf3')
def pdf3():
    return render_template('rss2pdf/pdf3.html')

@app.route('/pdf4')
def pdf4():
    return render_template('rss2pdf/pdf4.html')

@app.route('/pdf5')
def pdf5():
    return render_template('rss2pdf/pdf5.html')

@app.route('/pdf6')
def pdf6():
    return render_template('rss2pdf/pdf6.html')

@app.route('/pdf7')
def pdf7():
    return render_template('rss2pdf/pdf7.html')

@app.route('/pdf8')
def pdf8():
    return render_template('rss2pdf/pdf8.html')

@app.route('/pdf9')
def pdf9():
    return render_template('rss2pdf/pdf9.html')

@app.route('/pdf10')
def pdf10():
    return render_template('rss2pdf/pdf10.html')

@app.route('/pdf11')
def pdf11():
    return render_template('rss2pdf/pdf11.html')

@app.route('/pdf12')
def pdf12():
    return render_template('rss2pdf/pdf12.html')

@app.route('/pdf13')
def pdf13():
    return render_template('rss2pdf/pdf13.html')

@app.route('/pdf14')
def pdf14():
    return render_template('rss2pdf/pdf14.html')

@app.route('/pdf15')
def pdf15():
    return render_template('rss2pdf/pdf15.html')

@app.route('/pdf16')
def pdf16():
    return render_template('rss2pdf/pdf16.html')

@app.route('/pdf17')
def pdf17():
    return render_template('rss2pdf/pdf17.html')

@app.route('/pdf18')
def pdf18():
    return render_template('rss2pdf/pdf18.html')

@app.route('/pdf19')
def pdf19():
    return render_template('rss2pdf/pdf19.html')

@app.route('/pdf20')
def pdf20():
    return render_template('rss2pdf/pdf20.html')

@app.route('/pdf21')
def pdf21():
    return render_template('rss2pdf/pdf21.html')

@app.route('/pdf22')
def pdf22():
    return render_template('rss2pdf/pdf22.html')

@app.route('/pdf23')
def pdf23():
    return render_template('rss2pdf/pdf23.html')

@app.route('/pdf24')
def pdf24():
    return render_template('rss2pdf/pdf24.html')

@app.route('/pdf25')
def pdf25():
    return render_template('rss2pdf/pdf25.html')

@app.route('/pdf26')
def pdf26():
    return render_template('rss2pdf/pdf26.html')

@app.route('/pdf27')
def pdf27():
    return render_template('rss2pdf/pdf27.html')

@app.route('/pdf28')
def pdf28():
    return render_template('rss2pdf/pdf28.html')

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