from flask import Flask, render_template, url_for,redirect,request
from models.database import db, Paciente
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clinica.db'

db.init_app(app)

@app.route('/')
def loginPage():
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