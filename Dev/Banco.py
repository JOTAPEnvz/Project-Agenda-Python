import sqlite3

class Banco:
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.criar_tabela()

    def criar_tabela(self):
        cursor = self.conexao.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                idUsuario INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                telefone TEXT,
                email TEXT,
                usuario TEXT,
                senha TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cidades (
                idCidade INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                estado TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                idCliente INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                telefone TEXT,
                email TEXT,
                idCidade INTEGER,
                FOREIGN KEY (idCidade) REFERENCES cidades (idCidade)
            )
        ''')
        self.conexao.commit()

    def fechar_conexao(self):
        self.conexao.close()
