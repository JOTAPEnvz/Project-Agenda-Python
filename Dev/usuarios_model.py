from Banco import Banco

class Usuario:
    def __init__(self):
        self.banco = Banco()

    def inserir(self, nome, telefone, email, usuario, senha):
        cursor = self.banco.conexao.cursor()
        cursor.execute('''
            INSERT INTO usuarios (nome, telefone, email, usuario, senha)
            VALUES (?, ?, ?, ?, ?)
        ''', (nome, telefone, email, usuario, senha))
        self.banco.conexao.commit()

    def alterar(self, idUsuario, nome, telefone, email, usuario, senha):
        cursor = self.banco.conexao.cursor()
        cursor.execute('''
            UPDATE usuarios SET nome=?, telefone=?, email=?, usuario=?, senha=?
            WHERE idUsuario=?
        ''', (nome, telefone, email, usuario, senha, idUsuario))
        self.banco.conexao.commit()

    def excluir(self, idUsuario):
        cursor = self.banco.conexao.cursor()
        cursor.execute('DELETE FROM usuarios WHERE idUsuario=?', (idUsuario,))
        self.banco.conexao.commit()

    def buscar(self, idUsuario):
        cursor = self.banco.conexao.cursor()
        cursor.execute('SELECT * FROM usuarios WHERE idUsuario=?', (idUsuario,))
        return cursor.fetchone()
    
    def buscar_todos(self):
        cursor = self.banco.conexao.cursor()  # Obtém o cursor a partir da conexão
        cursor.execute("SELECT * FROM usuarios")  # Executa a consulta para buscar todos os usuários
        return cursor.fetchall()  # Retorna todos os resultados como uma lista de tuplas

    
class Cidade:
    def __init__(self):
        self.banco = Banco()

    def inserir(self, nome, estado):
        cursor = self.banco.conexao.cursor()
        cursor.execute('''
            INSERT INTO cidades (nome, estado)
            VALUES (?, ?)
        ''', (nome, estado))
        self.banco.conexao.commit()

    def alterar(self, idCidade, nome, estado):
        cursor = self.banco.conexao.cursor()
        cursor.execute('''
            UPDATE cidades SET nome=?, estado=?
            WHERE idCidade=?
        ''', (nome, estado, idCidade))
        self.banco.conexao.commit()

    def excluir(self, idCidade):
        cursor = self.banco.conexao.cursor()
        cursor.execute('DELETE FROM cidades WHERE idCidade=?', (idCidade,))
        self.banco.conexao.commit()

    def buscar(self, idCidade):
        cursor = self.banco.conexao.cursor()
        cursor.execute('SELECT * FROM cidades WHERE idCidade=?', (idCidade,))
        return cursor.fetchone()
    
    def buscar_todos(self):
        cursor = self.banco.conexao.cursor()  # Obtém o cursor a partir da conexão
        cursor.execute("SELECT * FROM usuarios")  # Executa a consulta para buscar todos os usuários
        return cursor.fetchall()  # Retorna todos os resultados como uma lista de tuplas

class Cliente:
    def __init__(self):
        self.banco = Banco()

    def inserir(self, nome, telefone, email, cidade):
        cursor = self.banco.conexao.cursor()
        cursor.execute('''
            INSERT INTO clientes (nome, telefone, email, idCidade)
            VALUES (?, ?, ?, ?)
        ''', (nome, telefone, email, cidade))
        self.banco.conexao.commit()

    def alterar(self, idCliente, nome, telefone, email, cidade):
        cursor = self.banco.conexao.cursor()
        cursor.execute('''
            UPDATE clientes SET nome=?, telefone=?, email=?, idCidade=?
            WHERE idCliente=?
        ''', (nome, telefone, email, cidade, idCliente))
        self.banco.conexao.commit()

    def excluir(self, idCliente):
        cursor = self.banco.conexao.cursor()
        cursor.execute('DELETE FROM clientes WHERE idCliente=?', (idCliente,))
        self.banco.conexao.commit()

    def buscar(self, idCliente):
        cursor = self.banco.conexao.cursor()
        cursor.execute('SELECT * FROM clientes WHERE idCliente=?', (idCliente,))
        return cursor.fetchone()

    def buscar_cidades(self):
        cursor = self.banco.conexao.cursor()
        cursor.execute('SELECT nome FROM cidades')
        cidades = [row[0] for row in cursor.fetchall()]
        return cidades
    
    def buscar_todos(self):
        cursor = self.banco.conexao.cursor()  # Obtém o cursor a partir da conexão
        cursor.execute("SELECT * FROM usuarios")  # Executa a consulta para buscar todos os usuários
        return cursor.fetchall()  # Retorna todos os resultados como uma lista de tuplas