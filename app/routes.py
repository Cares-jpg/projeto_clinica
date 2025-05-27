from flask import Flask, render_template, url_for, request, redirect, session, flash
from models.database import db, Paciente
import secrets

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clinica.db'
app.secret_key = secrets.token_hex(16)
db.init_app(app)


usuario = {
    'username': 'admin',
    'password': '1234'
}


@app.route('/', methods = ['GET', 'POST'])
def loginPage():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == usuario['username'] and password == usuario['password']:
            session['usuario'] = username
            return redirect(url_for('homePage'))
    
        else:
            flash('Login invalido, tente novamente')
            return redirect(url_for('loginPage'))
    return render_template('login.html')

@app.route('/home')
def homePage():
    return render_template('home.html')

@app.route('/cadastro', methods = ['GET','POST'])
def cadastroPage():
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        especialidade = request.form['especialidade']
        return redirect(url_for('home'))
    return render_template('cadastro.html')

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)