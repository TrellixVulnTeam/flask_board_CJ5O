from flask import Flask, render_template, request, json, session
from flaskext.mysql import MySQL
from flask_mail import Mail, Message
import config

mysql = MySQL()
app = Flask('__name__')
# db 초기화
mysql.init_app(config.db_config(app))
# mail 초기화
mail = Mail(config.mail_config(app))


@app.route('/')
def login():
    session.clear()
    return render_template('Login.html')


@app.route('/Home')
def home():
    return check_valid('Home.html')


@app.route('/About')
def about():
    return check_valid('About.html')


@app.route('/Contact')
def contact():
    return check_valid('Contact.html')


@app.route('/Signout')
def signout():
    session.clear()
    return render_template('Signout.html')


# Func : Login Process(ID/PW확인, Session저장)
@app.route('/loginProcess', methods=['POST'])
def login_process():
    _id = request.form['inputID']
    _pw = request.form['inputPassword']
    _ip = request.remote_addr
    data = login_db_conn(_id, _pw)

    if len(data) > 0:
        result = {
            'is_success': True,
            'ip': _ip
        }
        session['LoginID'] = data[0][0]
        session['LoginPW'] = data[0][1]
        session['IPAddress'] = _ip
    else:
        result = {
            'is_success': False,
            'ip': ''
        }
    return json.dumps(result)


# Func : 받는사람과 내용을 저장하여 메일전송
@app.route('/sendMail', methods=['POST'])
def send_mail():
    msg = Message('Test Title', sender='qkrdbsgh0921@gmail.com', recipients=['qkrdbsgh0921@gmail.com'], body='Test')
    mail.send(msg)
    return "Success"


# Func: session을 확인하여 비정상적 로그인은 Login화면으로 이동
def check_valid(url):
    if session.get('LoginID'):
        return render_template(url)
    else:
        return render_template('Login.html')


# Func: Login Procedure 호출
def login_db_conn(_id, _pw):
    con = mysql.connect()
    cursor = con.cursor()
    cursor.callproc('sp_LoginProcess', (_id, _pw))
    data = cursor.fetchall()
    return data


if __name__ == '__main__':
    app.run(debug=True)
