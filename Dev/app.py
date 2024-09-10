import tkinter as tk
from tkinter import ttk  # Importar ttk para o Treeview
from usuarios_model import Usuario

class Application:
    def __init__(self, root):
        self.usuario = Usuario()

        self.root = root
        self.root.title("Cadastro de Usuários")

        # Configurar o grid principal com 3 colunas para centralizar o conteúdo
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=0)
        self.root.columnconfigure(2, weight=1)

        # Frame principal para centralizar os widgets
        self.frame_principal = tk.Frame(root)
        self.frame_principal.grid(row=0, column=1, padx=20, pady=20)

        # Configurar o grid do frame principal
        for i in range(3):
            self.frame_principal.columnconfigure(i, weight=1)

        # Labels e Entradas
        self.lblIdUsuario = tk.Label(self.frame_principal, text="idUsuario:")
        self.lblIdUsuario.grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.txtIdUsuario = tk.Entry(self.frame_principal, width=30)
        self.txtIdUsuario.grid(row=0, column=1, columnspan=2, padx=5, pady=5, sticky="we")

        self.btnBuscar = tk.Button(self.frame_principal, text="Buscar", command=self.buscar_usuario, width=10)
        self.btnBuscar.grid(row=0, column=3, padx=5, pady=5)

        self.lblNome = tk.Label(self.frame_principal, text="Nome:")
        self.lblNome.grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.txtNome = tk.Entry(self.frame_principal, width=30)
        self.txtNome.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky="we")

        self.lblTelefone = tk.Label(self.frame_principal, text="Telefone:")
        self.lblTelefone.grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.txtTelefone = tk.Entry(self.frame_principal, width=30)
        self.txtTelefone.grid(row=2, column=1, columnspan=3, padx=5, pady=5, sticky="we")

        self.lblEmail = tk.Label(self.frame_principal, text="E-mail:")
        self.lblEmail.grid(row=3, column=0, sticky="e", padx=5, pady=5)
        self.txtEmail = tk.Entry(self.frame_principal, width=30)
        self.txtEmail.grid(row=3, column=1, columnspan=3, padx=5, pady=5, sticky="we")

        self.lblUsuario = tk.Label(self.frame_principal, text="Usuário:")
        self.lblUsuario.grid(row=4, column=0, sticky="e", padx=5, pady=5)
        self.txtUsuario = tk.Entry(self.frame_principal, width=30)
        self.txtUsuario.grid(row=4, column=1, columnspan=3, padx=5, pady=5, sticky="we")

        self.lblSenha = tk.Label(self.frame_principal, text="Senha:")
        self.lblSenha.grid(row=5, column=0, sticky="e", padx=5, pady=5)
        self.txtSenha = tk.Entry(self.frame_principal, show="*", width=30)
        self.txtSenha.grid(row=5, column=1, columnspan=3, padx=5, pady=5, sticky="we")

        # Frame para os botões, posicionado abaixo dos inputs
        self.frame_botoes = tk.Frame(root)
        self.frame_botoes.grid(row=1, column=1, pady=10)

        # Botões centralizados
        self.btnInserir = tk.Button(self.frame_botoes, text="Inserir", command=self.inserir_usuario, width=10)
        self.btnInserir.grid(row=0, column=0, padx=10, pady=5)

        self.btnAlterar = tk.Button(self.frame_botoes, text="Alterar", command=self.alterar_usuario, width=10)
        self.btnAlterar.grid(row=0, column=1, padx=10, pady=5)

        self.btnExcluir = tk.Button(self.frame_botoes, text="Excluir", command=self.excluir_usuario, width=10)
        self.btnExcluir.grid(row=0, column=2, padx=10, pady=5)

        # Label de mensagem centralizada abaixo dos botões
        self.lblMensagem = tk.Label(root, text="", fg="green")
        self.lblMensagem.grid(row=2, column=1, padx=20, pady=10, sticky="we")

        # Adicionar o Treeview abaixo dos botões
        self.treeview = ttk.Treeview(root, columns=("id", "nome", "telefone", "email", "usuario"), show="headings")
        self.treeview.grid(row=3, column=1, padx=20, pady=10, sticky="nsew")

        # Definir cabeçalhos
        self.treeview.heading("id", text="ID")
        self.treeview.heading("nome", text="Nome")
        self.treeview.heading("telefone", text="Telefone")
        self.treeview.heading("email", text="Email")
        self.treeview.heading("usuario", text="Usuário")

        # Ajustar tamanho das colunas
        self.treeview.column("id", width=50, anchor="center")
        self.treeview.column("nome", width=150, anchor="w")
        self.treeview.column("telefone", width=100, anchor="center")
        self.treeview.column("email", width=200, anchor="w")
        self.treeview.column("usuario", width=100, anchor="center")

        # Carregar os dados na inicialização
        self.carregar_usuarios()

    def carregar_usuarios(self):
        # Limpar dados anteriores
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        # Obter todos os usuários
        usuarios = self.usuario.buscar_todos()

        # Inserir novos dados no Treeview
        for usuario in usuarios:
            self.treeview.insert("", "end", values=usuario)

    def buscar_usuario(self):
        idUsuario = self.txtIdUsuario.get()
        resultado = self.usuario.buscar(idUsuario)
        if resultado:
            self.txtNome.delete(0, tk.END)
            self.txtNome.insert(tk.END, resultado[1])
            self.txtTelefone.delete(0, tk.END)
            self.txtTelefone.insert(tk.END, resultado[2])
            self.txtEmail.delete(0, tk.END)
            self.txtEmail.insert(tk.END, resultado[3])
            self.txtUsuario.delete(0, tk.END)
            self.txtUsuario.insert(tk.END, resultado[4])
            self.txtSenha.delete(0, tk.END)
            self.txtSenha.insert(tk.END, resultado[5])
            self.lblMensagem.config(text="Busca realizada com sucesso!", fg="green")
        else:
            self.lblMensagem.config(text="Usuário não encontrado!", fg="red")

    def inserir_usuario(self):
        nome = self.txtNome.get()
        telefone = self.txtTelefone.get()
        email = self.txtEmail.get()
        usuario = self.txtUsuario.get()
        senha = self.txtSenha.get()
        self.usuario.inserir(nome, telefone, email, usuario, senha)
        self.lblMensagem.config(text="Usuário inserido com sucesso!", fg="green")
        self.limpar_campos()
        self.carregar_usuarios()  # Recarregar dados

    def alterar_usuario(self):
        idUsuario = self.txtIdUsuario.get()
        nome = self.txtNome.get()
        telefone = self.txtTelefone.get()
        email = self.txtEmail.get()
        usuario = self.txtUsuario.get()
        senha = self.txtSenha.get()
        self.usuario.alterar(idUsuario, nome, telefone, email, usuario, senha)
        self.lblMensagem.config(text="Usuário alterado com sucesso!", fg="green")
        self.carregar_usuarios()  # Recarregar dados

    def excluir_usuario(self):
        idUsuario = self.txtIdUsuario.get()
        self.usuario.excluir(idUsuario)
        self.lblMensagem.config(text="Usuário excluído com sucesso!", fg="green")
        self.limpar_campos()
        self.carregar_usuarios()  # Recarregar dados

    def limpar_campos(self):
        self.txtIdUsuario.delete(0, tk.END)
        self.txtNome.delete(0, tk.END)
        self.txtTelefone.delete(0, tk.END)
        self.txtEmail.delete(0, tk.END)
        self.txtUsuario.delete(0, tk.END)
        self.txtSenha.delete(0, tk.END)

# Execução da interface
if __name__ == "__main__":
    root = tk.Tk()
    root.state("zoomed")  # Maximiza a janela
    app = Application(root)
    root.mainloop()
