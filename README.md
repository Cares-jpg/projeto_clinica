# projeto_clinica

## Descrição do Projeto

Este repositório apresenta um **Sistema de Gerenciamento de Pacientes** desenvolvido em Python. O objetivo principal é simular e otimizar o fluxo de atendimento em ambientes clínicos, permitindo o cadastro, a triagem e a chamada de pacientes de forma organizada. As informações dos pacientes são persistidas em um banco de dados **SQLite**, garantindo que os dados permaneçam salvos entre as sessões.

A arquitetura do projeto está preparada para uma **interface web**, com arquivos HTML e CSS dedicados, que permitiriam uma interação mais visual e amigável com o sistema, além da funcionalidade atual via console.

O sistema oferece:
* **Cadastro Simplificado**: Registro rápido de pacientes com nome, idade e especialidade.
* **Gerenciamento de Filas**: Organização de pacientes em filas por especialidade, com geração automática de senhas.
* **Triagem e Prioridade**: Aplicação de critérios de triagem (ex: "Preferencial" para idosos) para otimizar o atendimento.
* **Persistência de Dados**: Armazenamento seguro de todos os dados dos pacientes em um banco de dados SQLite.

## Instruções de Execução

Siga os passos abaixo para configurar e rodar o sistema em sua máquina local:

### Pré-requisitos

Certifique-se de que você tem o **Python versão 3** instalado. Você pode baixá-lo em [python.org](https://www.python.org/).

### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/nome-do-seu-repositorio.git](https://github.com/seu-usuario/nome-do-seu-repositorio.git)
    ```
    (Substitua `seu-usuario/nome-do-seu-repositorio` pelo caminho correto do seu repositório no GitHub.)

2.  **Acesse a pasta do projeto:**
    ```bash
    cd nome-do-seu-repositorio
    ```
3. **Configurar o Ambiente Virtual**
É altamente recomendável usar um ambiente virtual para isolar as dependências do seu projeto.

Criar o Ambiente Virtual:

```Bash

python -m venv venv

```
(Este comando cria uma pasta chamada venv dentro do seu projeto.)

Ativar o Ambiente Virtual:

No Windows (PowerShell/CMD):
```Bash

.\venv\Scripts\activate

```
No Linux/macOS (Bash, Zsh, etc.):
```Bash

source venv/bin/activate
```
(Você verá (venv) no início da linha do seu terminal, indicando que o ambiente está ativo.)

4. **Instalar as Dependências**
Com o ambiente virtual ativado, instale as bibliotecas Python necessárias para o projeto.

```Bash

pip install Flask Flask-SQLAlchemy
```
(Se você tiver um arquivo requirements.txt no projeto listando todas as dependências, pode usar pip install -r requirements.txt)

5. **Rodar a Aplicação Flask**
Agora você pode iniciar o servidor de desenvolvimento do Flask.

Certifique-se de que está na pasta raiz do seu projeto  e que seu ambiente virtual está ativo.

```Bash

python src/app.py
```
Você verá uma mensagem no terminal indicando que o servidor está rodando, geralmente algo como:
Running on http://127.0.0.1:5000/

6. **Acessar a Aplicação no Navegador**
Abra seu navegador web e digite o endereço fornecido no terminal (geralmente http://127.0.0.1:5000/).

Você será direcionado para a página de login.

7. **Credenciais de Login (Para Atendentes)**
Para acessar o sistema como atendente, utilize as seguintes credenciais:

Nome de Usuário (Username): admin
Senha (Password): 1234
### Como Iniciar

Para rodar a versão de console do sistema, execute o arquivo principal:
```bash
python src/main.py
```

## Tecnologias Utilizadas

1-Python versão 3: Linguagem principal para backend e sistema de console.

2-Módulo sqlite3 do Python: Biblioteca nativa para interagir com banco de dados SQLite.

3-Flask: Framework web para construção da interface e gerenciamento de rotas.

4-HTML: Estrutura das páginas da interface (ex: login.html).

5-CSS: Estilização visual das páginas (ex: style.css).



---

## Estrutura dos Arquivos
```bash
.
├── src/
│   ├── db/
│   │   ├── clinica.db              # Arquivo do banco de dados SQLite (criado na primeira execução).
│   │   ├── conexao.py              # Módulo para estabelecer a conexão com o banco de dados SQLite.
│   │   └── tabelas.py              # Módulo que define as funções para criar a tabela de usuários e realizar operações CRUD básicas.
│   ├── classes.py                  # Contém a lógica de negócio do sistema e a estrutura de fila (ex: `GerenciadorPacientes`).
│   └── main.py                     # Script principal que executa o menu interativo e interage com o sistema.
├── templates/                      # Pasta que contém os arquivos de template HTML.
│   ├── pages/                      # Subpasta para organizar as diferentes páginas HTML.
│   │   └── login.html              # Exemplo de uma página de login.
│   └── styles/                     # Pasta que contém os arquivos de estilo para a interface web.
│       └── css/                    # Subpasta para arquivos CSS.
│           └── style.css           # Arquivo principal de estilos CSS.
├── .gitignore                      # Arquivo que especifica quais arquivos e diretórios o Git deve ignorar (ex: arquivos de banco de dados,                                     caches, etc.).
└── README.md                       # Este arquivo, contendo a descrição do projeto e instruções.
``` 
## Integrantes do grupo :

### Paulo Henrique
### Rafael Mesquita 
### Guilherme Liarte de Oliveira 
### João Marcos Teixeira 
