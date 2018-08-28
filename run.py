from flask import Flask, render_template, request, json, session

app = Flask('__name__')

@app.route('/')
def login():
    return render_template('Login.html')

@app.route('/Layout')
def layout():
    return render_template('Layout.html')

@app.route('/Home')
def Home():
    return render_template('Home.html')

@app.route('/About')
def About():
    return render_template('About.html')

@app.route('/Contact')
def Contact():
    return render_template('Contact.html')

@app.route('/loginProcess', methods=['POST'])
def loginProcess():
    tmp_account = {'id': 'qwer', 'pw': '1234'}

    _id = request.form['inputID']
    _pw = request.form['inputPassword']

    if _id == tmp_account['id'] and _pw == tmp_account['pw']:
        result = 'Success'
        # session['LoginID'] = request.form['inputID']
        # session['LoginPW'] = request.form['inputPassword']
    elif _id == tmp_account['id'] and _pw != tmp_account['pw']:
        result = 'NotMatchPW'
    elif _id != tmp_account['id'] and _pw == tmp_account['pw']:
        result = 'NotMatchID'
    else:
        result = 'Fail'

    return json.dumps(result)


    # return json.dumps({ 'id': _id, 'pw': _pw })

if __name__ == '__main__':
    app.debug = True
    app.run()