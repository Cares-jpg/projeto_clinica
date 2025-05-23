from db.conexao import conectar

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome CHAR(80) NOT NULL,
            especialidade TEXT NOT NULL,
            tipo TEXT NOT NULL,
            senha TEXT NOT NULL,
            triagem TEXT NOT null
                
        )
    ''')
    conn.commit()
    conn.close()

def inserir_usuario(nome, especialidade, tipo, senha, triagem):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO usuarios (nome, especialidade, tipo, senha, triagem) VALUES (?, ?, ?, ?, ?)', (nome, especialidade, tipo, senha, triagem))
    conn.commit()
    conn.close()

def listar_usuarios():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    conn.close()
    return usuarios
