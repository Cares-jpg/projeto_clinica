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

### Como Iniciar

Para rodar a versão de console do sistema, execute o arquivo principal:
```bash
python src/main.py
```

## Tecnologias Utilizadas

* **Python versão 3**: A linguagem de programação principal para o desenvolvimento da lógica de backend e do sistema de console.
* **Módulo `sqlite3` do Python**: Esta é a biblioteca padrão do Python utilizada para interagir com o banco de dados SQLite3, permitindo a persistência dos dados dos pacientes.
* * **Flask**: Uma biblioteca web para Python, utilizado (ou a ser utilizado) para a construção da interface de usuário e gerenciamento das rotas web.
* **HTML**: Para a estrutura das páginas da interface web (ex: `login.html`).
* **CSS**: Para a estilização visual das páginas da interface web (ex: `style.css`).

---

Estrutura dos Arquivos
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

## Integrantes do grupo :
*Paulo 
*Rafaerl Mesquita 
*Guilherme Liarte de Oliveira 
*João Marcos Teixeira 
