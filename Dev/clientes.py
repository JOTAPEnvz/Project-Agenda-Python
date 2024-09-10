import tkinter as tk
from tkinter import ttk
from usuarios_model import Cliente

class Application:
    def __init__(self, root):
        self.cliente = Cliente()

        self.root = root
        self.root.title("Cadastro de Clientes")

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
        self.lblIdCliente = tk.Label(self.frame_principal, text="ID Cliente:")
        self.lblIdCliente.grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.txtIdCliente = tk.Entry(self.frame_principal, width=30)
        self.txtIdCliente.grid(row=0, column=1, columnspan=2, padx=5, pady=5, sticky="we")

        self.lblNome = tk.Label(self.frame_principal, text="Nome:")
        self.lblNome.grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.txtNome = tk.Entry(self.frame_principal, width=30)
        self.txtNome.grid(row=1, column=1, columnspan=2, padx=5, pady=5, sticky="we")

        self.lblTelefone = tk.Label(self.frame_principal, text="Telefone:")
        self.lblTelefone.grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.txtTelefone = tk.Entry(self.frame_principal, width=30)
        self.txtTelefone.grid(row=2, column=1, columnspan=2, padx=5, pady=5, sticky="we")

        self.lblEmail = tk.Label(self.frame_principal, text="E-mail:")
        self.lblEmail.grid(row=3, column=0, sticky="e", padx=5, pady=5)
        self.txtEmail = tk.Entry(self.frame_principal, width=30)
        self.txtEmail.grid(row=3, column=1, columnspan=2, padx=5, pady=5, sticky="we")

        self.lblCidade = tk.Label(self.frame_principal, text="Cidade:")
        self.lblCidade.grid(row=4, column=0, sticky="e", padx=5, pady=5)
        self.cboCidade = ttk.Combobox(self.frame_principal, values=self.cliente.buscar_cidades(), width=28)
        self.cboCidade.grid(row=4, column=1, columnspan=2, padx=5, pady=5, sticky="we")

        # Frame para os botões, posicionado abaixo dos inputs
        self.frame_botoes = tk.Frame(root)
        self.frame_botoes.grid(row=5, column=1, pady=10)

        # Botões centralizados
        self.btnInserir = tk.Button(self.frame_botoes, text="Inserir", command=self.inserir_cliente, width=10)
        self.btnInserir.grid(row=0, column=0, padx=10, pady=5)

        self.btnBuscar = tk.Button(self.frame_botoes, text="Buscar", command=self.buscar_cliente, width=10)
        self.btnBuscar.grid(row=0, column=1, padx=10, pady=5)

        self.btnAlterar = tk.Button(self.frame_botoes, text="Alterar", command=self.alterar_cliente, width=10)
        self.btnAlterar.grid(row=0, column=2, padx=10, pady=5)

        self.btnExcluir = tk.Button(self.frame_botoes, text="Excluir", command=self.excluir_cliente, width=10)
        self.btnExcluir.grid(row=0, column=3, padx=10, pady=5)

        self.btnSair = tk.Button(self.frame_botoes, text="Sair", command=self.root.quit, width=10)
        self.btnSair.grid(row=0, column=4, padx=10, pady=5)

        # Label de mensagem centralizada abaixo dos botões
        self.lblMensagem = tk.Label(root, text="", fg="green")
        self.lblMensagem.grid(row=6, column=1, padx=20, pady=10, sticky="we")

        # Adicionando o Treeview para exibir os clientes
        self.tree = ttk.Treeview(root, columns=('ID', 'Nome', 'Telefone', 'Email', 'Cidade'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Nome', text='Nome')
        self.tree.heading('Telefone', text='Telefone')
        self.tree.heading('Email', text='E-mail')
        self.tree.heading('Cidade', text='Cidade')
        self.tree.column('ID', width=50)
        self.tree.column('Nome', width=200)
        self.tree.column('Telefone', width=100)
        self.tree.column('Email', width=200)
        self.tree.column('Cidade', width=150)
        self.tree.grid(row=7, column=1, padx=20, pady=10, sticky="nsew")

        # Preenchendo o Treeview com os clientes
        self.carregar_clientes()

    def carregar_clientes(self):
        # Limpa o Treeview
        for row in self.tree.get_children():
            self.tree.delete(row)
        
        # Busca os clientes no banco de dados
        clientes = self.cliente.buscar_todos()
        for cliente in clientes:
            self.tree.insert('', tk.END, values=cliente)

    def buscar_cliente(self):
        idCliente = self.txtIdCliente.get()
        resultado = self.cliente.buscar(idCliente)
        if resultado:
            self.txtNome.delete(0, tk.END)
            self.txtNome.insert(tk.END, resultado[1])
            self.txtTelefone.delete(0, tk.END)
            self.txtTelefone.insert(tk.END, resultado[2])
            self.txtEmail.delete(0, tk.END)
            self.txtEmail.insert(tk.END, resultado[3])
            self.cboCidade.set(resultado[4])
            self.lblMensagem.config(text="Cliente encontrado!", fg="green")
        else:
            self.lblMensagem.config(text="Cliente não encontrado!", fg="red")

    def alterar_cliente(self):
        idCliente = self.txtIdCliente.get()
        nome = self.txtNome.get()
        telefone = self.txtTelefone.get()
        email = self.txtEmail.get()
        cidade = self.cboCidade.get()
        self.cliente.alterar(idCliente, nome, telefone, email, cidade)
        self.lblMensagem.config(text="Cliente alterado com sucesso!", fg="green")
        self.carregar_clientes()  # Atualiza o Treeview

    def excluir_cliente(self):
        idCliente = self.txtIdCliente.get()
        self.cliente.excluir(idCliente)
        self.lblMensagem.config(text="Cliente excluído com sucesso!", fg="green")
        self.limpar_campos()
        self.carregar_clientes()  # Atualiza o Treeview

    def inserir_cliente(self):
        nome = self.txtNome.get()
        telefone = self.txtTelefone.get()
        email = self.txtEmail.get()
        cidade = self.cboCidade.get()
        self.cliente.inserir(nome, telefone, email, cidade)
        self.lblMensagem.config(text="Cliente inserido com sucesso!", fg="green")
        self.limpar_campos()
        self.carregar_clientes()  # Atualiza o Treeview

    def limpar_campos(self):
        self.txtIdCliente.delete(0, tk.END)
        self.txtNome.delete(0, tk.END)
        self.txtTelefone.delete(0, tk.END)
        self.txtEmail.delete(0, tk.END)
        self.cboCidade.set('')

# Execução da interface
if __name__ == "__main__":
    root = tk.Tk()
    root.state("zoomed")  # Maximiza a janela
    app = Application(root)
    root.mainloop()
