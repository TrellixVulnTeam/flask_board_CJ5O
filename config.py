# Func : DB 설정
def db_config(app):
    app.secret_key = 'flask app secret key'
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = '1234'
    app.config['MYSQL_DATABASE_DB'] = 'flask_test'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    return app


# Func : MAIL 설정
def mail_config(app):
    app.config['MAIL_SERVER']= 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'qkrdbsgh0921@gmail.com'
    app.config['MAIL_PASSWORD'] = 'password'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    return app