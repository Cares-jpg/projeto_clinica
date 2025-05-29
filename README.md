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

### Como acessar

1.  **Clone o repositório:**
    ```bash
    git clone (https://github.com/Cares-jpg/projeto_clinica)
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

pip install -r requirements.txt
```


5. **Rodar a Aplicação Flask**
Agora você pode iniciar o servidor de desenvolvimento do Flask.

(Certifique-se de que está na pasta raiz do seu projeto  e que seu ambiente virtual está ativo.)

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



## Tecnologias Utilizadas

1-Python versão 3: Linguagem principal para backend e sistema de console.

2-Módulo sqlite3 do Python: Biblioteca nativa para interagir com banco de dados SQLite.

3-Flask: Framework web para construção da interface e gerenciamento de rotas.

4-HTML: Estrutura das páginas da interface (ex: login.html).

5-CSS: Estilização visual das páginas (ex: style.css).

6- SQLAlchemy — ORM para integração com o banco



---

## Estrutura dos Arquivos
```bash
projeto_clinica/
├── src/                          # Diretório principal que contém o código-fonte da sua aplicação.
│   ├── app/                      # Diretório que agrupa os módulos centrais da sua aplicação.
│   │   └── models/               # Subpacote para definir os modelos de dados da aplicação.
│   │       ├── __init__.py       # Inicializa 'models' como um pacote Python.
│   │       └── database.py       # Define a instância do SQLAlchemy (db) e as classes de modelo (ex: 'Paciente') que mapeiam para tabelas do banco de dados.
│   │       └── __init__.py       # **(Observação)** A presença de um segundo '__init__.py' na mesma pasta ('models/') é atípica e redundante. Um único '__init__.py' é suficiente para definir um pacote.
│   ├── static/                   # Contém arquivos estáticos (CSS, imagens) que são servidos diretamente ao navegador do cliente.
│   │   ├── css/                  # Folhas de estilo em cascata.
│   │   │   ├── cadastro.css      # Estilos específicos para a página de cadastro.
│   │   │   ├── chamar.css        # Estilos específicos para a página de chamada.
│   │   │   ├── home.css          # Estilos específicos para a página inicial.
│   │   │   ├── listar.css        # Estilos específicos para a página de listagem.
│   │   │   └── login.css         # Estilos específicos para a página de login.
│   │   └── image/                # Diretório para imagens da aplicação, organizado por contexto.
│   │       ├── cadastro/         # Imagens usadas na página de cadastro.
│   │       │   └── logo_clinica.png
│   │       ├── home/             # Imagens usadas na página inicial.
│   │       │   ├── bem_vindo.png
│   │       │   └── logo_clinica.png
│   │       └── login/            # Imagens usadas na página de login.
│   │           └── logo_branca_clinica.png
│   ├── templates/                # Contém os arquivos de template HTML (`.html`) que o Flask renderiza usando Jinja2.
│   │   ├── base.html             # Template base que outras páginas HTML podem herdar para manter um layout consistente.
│   │   ├── cadastro.html         # Página HTML para o formulário de cadastro de pacientes.
│   │   ├── chamar.html           # Página HTML para a funcionalidade de chamar o próximo paciente.
│   │   ├── home.html             # Página HTML de boas-vindas ou dashboard após o login.
│   │   ├── listar.html           # Página HTML para exibir a lista de pacientes.
│   │   ├── login.html            # Página HTML para autenticação de usuários.
│   │   └── historico.html        # Página HTML para visualizar o histórico de atendimentos/pacientes.
│   ├── __init__.py               # Inicializa 'src' como um pacote Python. Isso permite importações como 'from src.app.models.database import ...' ou 'from src.classes import ...'.
│   ├── app.py                    # **Arquivo principal da aplicação Flask.** É o ponto de entrada que inicializa a aplicação, configura o banco de dados e define as rotas.
│   └── classes.py                # Contém classes de lógica de negócio, como 'GerenciadorPacientes', encapsulando funcionalidades importantes do sistema.
├── .gitignore                    # Arquivo de configuração para o Git; especifica o que deve ser ignorado (ex: arquivos .pyc).
├── README.md                     # Documentação principal do projeto, contendo informações sobre como rodar e acessar.
└── requirements.txt              # Lista todas as bibliotecas Python (e suas versões) das quais o projeto depende.
``` 
## Integrantes do grupo :

### Paulo Henrique Cares
### Rafael Mesquita 
### Guilherme Liarte de Oliveira 
### João Marcos Teixeira 
