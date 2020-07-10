from app import app
from flask import request, render_template, session, redirect, url_for
from app.auth_block import check_register, authorize


@app.route('/')
@app.route('/index')
def index():
    if session.get('user') is None:
        return redirect(url_for('login'))
    else:
        del session['user']
        return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login2.html')
    else:
        login = request.form['login']
        password = request.form['pswrd']
        result = authorize(login, password)
        if result[0] == True:
            session['user'] = login
            return redirect(url_for('index'))
        else:
            return redirect(url_for('error_page', text=result[1]))


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        login = request.form['login']
        password = request.form['pswrd']
        passwordCheck = request.form['pswrdCheck']
        result = check_register(login, password, passwordCheck)
        if result[0] == True:
            session['user'] = login
            return redirect(url_for('index'))
        else:
            return redirect(url_for('error_page', text=result[1]))



@app.route('/error_page/<text>')
def error_page(text):
    return render_template('error_page.html', error_text=text)

