from flask import Flask, render_template, request, redirect, url_for, session, flash
from app.models.database import db, Paciente
from classes import GerenciadorPacientes
import secrets

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clinica.db'
app.secret_key = secrets.token_hex(16)
db.init_app(app)

sistema = GerenciadorPacientes()

usuario = {
    'username': 'admin',
    'password': '1234'
}

@app.route('/', methods=['GET', 'POST'])
def loginPage():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == usuario['username'] and password == usuario['password']:
            session['usuario'] = username
            return redirect(url_for('homePage'))
        else:
            flash('Login inválido')
    return render_template('login.html')


@app.route('/home')
def homePage():
    especialidades = list(sistema.lista_especialidade.keys())
    pacientes = sistema.listar_pacientes()  
    return render_template('home.html', especialidades=especialidades, pacientes=pacientes)


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastroPage():
    if request.method == 'POST':
        nome = request.form['nome']
        try:
            idade = int(request.form['idade'])
        except ValueError:
            flash('Idade inválida, insira um número.')
            return redirect(url_for('cadastroPage'))

        especialidade = request.form['especialidade']
        if especialidade not in sistema.lista_especialidade:
            flash('Especialidade inválida.')
            return redirect(url_for('cadastroPage'))

        resultado = sistema.adicionar_paciente(nome, especialidade, idade)
        flash(resultado)
        return redirect(url_for('homePage'))

    especialidades = list(sistema.lista_especialidade.keys())
    return render_template('cadastro.html', especialidades=especialidades)


@app.route('/chamar/<especialidade>')
def chamarPaciente(especialidade):
    if especialidade not in sistema.lista_especialidade:
        flash('Especialidade inválida.')
        return redirect(url_for('homePage'))

    resultado = sistema.chamar_paciente(especialidade)
    flash(resultado)
    return redirect(url_for('homePage'))


@app.route('/historico')
def historicoPage():
    pacientes = Paciente.query.order_by(Paciente.date_created.desc()).all()
    return render_template('historico.html', pacientes=pacientes)


with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)
