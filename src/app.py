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
        username = request.form['username'].strip()
        password = request.form['password']

        if username == usuario['username'] and password == usuario['password']:
            session['usuario'] = username
            return redirect(url_for('homePage'))
        else:
            flash('Login inválido', 'error')
    return render_template('login.html')


@app.route('/home')
def homePage():
    return render_template('home.html')


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastroPage():
    if request.method == 'POST':
        nome = request.form['nome'].strip()
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
        flash(resultado, 'erro')  
        especialidades = list(sistema.lista_especialidade.keys())
        return render_template('cadastro.html', especialidades=especialidades)

    especialidades = list(sistema.lista_especialidade.keys())
    return render_template('cadastro.html', especialidades=especialidades)

@app.route('/painel')
def painelChamada():
    especialidades = list(sistema.lista_especialidade.keys())  
    return render_template('chamar.html', especialidades=especialidades)


@app.route('/chamar/<especialidade>')
def chamarPaciente(especialidade):

    resultado = sistema.chamar_paciente(especialidade)
    especialidades = list(sistema.lista_especialidade.keys())
    if resultado:
        return render_template(
            'chamar.html',
            especialidades=especialidades,
            senha_atual=resultado['senha'],
            nome_paciente=resultado['nome'],
            tipo_paciente=resultado['tipo'],
            triagem_paciente=resultado['triagem'],
            especialidade_atual=resultado['especialidade']
        )
    else:
        return render_template(
            'chamar.html',
            especialidades= especialidades,
            mensagem=f"Não há pacientes aguardando em {especialidade}.",
            senha_atual=None,
            nome_paciente=None,
            tipo_paciente=None,
            triagem_paciente=None,
            especialidade_atual=especialidade
        )

@app.route('/listar', methods=['GET'])
def listarPage():
    especialidades = list(sistema.lista_especialidade.keys())
    pacientes = sistema.listar_pacientes()  
    return render_template('listar.html', especialidades=especialidades, pacientes=pacientes)


@app.route('/historico')
def historicoPage():
    pacientes = Paciente.query.order_by(Paciente.date_created.desc()).all()
    return render_template('historico.html', pacientes=pacientes)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
