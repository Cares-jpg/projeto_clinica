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
    if 'usuario' not in session:
        flash('Faça login para acessar esta página', 'error')
        return redirect(url_for('loginPage'))
    return render_template('home.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastroPage():
    if 'usuario' not in session:
        flash('Faça login para acessar esta página', 'error')
        return redirect(url_for('loginPage'))

    try:
        especialidades = sistema.gerenciador_especialidades.get_especialidades()
        
        if request.method == 'POST':
            nome = request.form['nome'].strip()
            try:
                idade = int(request.form['idade'])
            except ValueError:
                flash('Idade inválida, insira um número.', 'error')
                return render_template('cadastro.html', especialidades=especialidades)

            especialidade = request.form['especialidade']
            resultado = sistema.adicionar_paciente(nome, especialidade, idade)
            
            # Se o resultado contiver palavras que indicam erro, use a categoria 'error'
            is_error = any(palavra in resultado.lower() for palavra in ['erro', 'inválido', 'sem vagas'])
            flash(resultado, 'error' if is_error else 'success')
            
            return render_template('cadastro.html', especialidades=especialidades)

        return render_template('cadastro.html', especialidades=especialidades)
    except Exception as e:
        flash(f'Erro no sistema: {str(e)}', 'error')
        return redirect(url_for('homePage'))

@app.route('/painel')
def painelChamada():
    if 'usuario' not in session:
        flash('Faça login para acessar esta página', 'error')
        return redirect(url_for('loginPage'))

    try:
        especialidades = sistema.gerenciador_especialidades.get_especialidades()
        return render_template('chamar.html', especialidades=especialidades)
    except Exception as e:
        flash(f'Erro ao carregar painel: {str(e)}', 'error')
        return redirect(url_for('homePage'))

@app.route('/chamar/<especialidade>')
def chamarPaciente(especialidade):
    if 'usuario' not in session:
        flash('Faça login para acessar esta página', 'error')
        return redirect(url_for('loginPage'))

    try:
        resultado = sistema.chamar_paciente(especialidade)
        especialidades = sistema.gerenciador_especialidades.get_especialidades()
        
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
                especialidades=especialidades,
                mensagem=f"Não há pacientes aguardando em {especialidade}.",
                senha_atual=None,
                nome_paciente=None,
                tipo_paciente=None,
                triagem_paciente=None,
                especialidade_atual=especialidade
            )
    except Exception as e:
        flash(f'Erro ao chamar paciente: {str(e)}', 'error')
        return redirect(url_for('painelChamada'))

@app.route('/listar', methods=['GET'])
def listarPage():
    if 'usuario' not in session:
        flash('Faça login para acessar esta página', 'error')
        return redirect(url_for('loginPage'))

    try:
        especialidades = sistema.gerenciador_especialidades.get_especialidades()
        pacientes = sistema.listar_pacientes()
        return render_template('listar.html', especialidades=especialidades, pacientes=pacientes)
    except Exception as e:
        flash(f'Erro ao listar pacientes: {str(e)}', 'error')
        return redirect(url_for('homePage'))

@app.route('/historico')
def historicoPage():
    if 'usuario' not in session:
        flash('Faça login para acessar esta página', 'error')
        return redirect(url_for('loginPage'))

    try:
        pacientes = Paciente.query.order_by(Paciente.date_created.desc()).all()
        return render_template('historico.html', pacientes=pacientes)
    except Exception as e:
        flash(f'Erro ao carregar histórico: {str(e)}', 'error')
        return redirect(url_for('homePage'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
