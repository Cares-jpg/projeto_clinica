import logging
import os
from datetime import datetime

# Criar o diretório de logs se não existir
if not os.path.exists('logs'):
    os.makedirs('logs')

# Configurar o logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(
            filename=f'logs/clinica_{datetime.now().strftime("%Y-%m-%d")}.log',
            encoding='utf-8'
        ),
        logging.StreamHandler()
    ]
)   