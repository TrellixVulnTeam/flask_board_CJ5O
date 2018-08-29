from flask import Flask, render_template, request, json, session
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask('__name__')
app.secret_key = 'flask app secret key'

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '1234'
app.config['MYSQL_DATABASE_DB'] = 'flask_test'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


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


@app.route('/loginProcess', methods=['POST'])
def login_process():
    _id = request.form['inputID']
    _pw = request.form['inputPassword']

    data = login_db_conn(_id, _pw)

    if len(data) > 0:
        result = "Success"
        session['LoginID'] = data[0][0]
        session['LoginPW'] = data[0][1]
    else:
        result = "Fail"

    return result
    # return json.dumps({ 'id': _id, 'pw': _pw })


def check_valid(url):
    if session.get('LoginID'):
        return render_template(url)
    else:
        return render_template('Login.html')


def login_db_conn(_id, _pw):
    con = mysql.connect()
    cursor = con.cursor()
    cursor.callproc('sp_LoginProcess', (_id, _pw))
    data = cursor.fetchall()
    return data


if __name__ == '__main__':
    app.debug = True
    app.run()
