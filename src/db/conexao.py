import sqlite3

def conectar(database='clinica.db'):
    sqlite3.connect(database)