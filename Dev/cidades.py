import tkinter as tk
from tkinter import ttk
from usuarios_model import Cidade

class TelaCidades:
    def __init__(self, root):
        self.cidade = Cidade()

        self.root = root
        self.root.title("Cadastro de Cidades")

        # Configurar grid
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=0)
        self.root.columnconfigure(2, weight=1)

        # Frame principal
        self.frame_principal = tk.Frame(root)
        self.frame_principal.grid(row=0, column=1, padx=20, pady=20)

        # Configurar o grid do frame principal
        for i in range(3):
            self.frame_principal.columnconfigure(i, weight=1)

        # Labels e Entradas
        self.lblIdCidade = tk.Label(self.frame_principal, text="idCidade:")
        self.lblIdCidade.grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.txtIdCidade = tk.Entry(self.frame_principal, width=30)
        self.txtIdCidade.grid(row=0, column=1, columnspan=2, padx=5, pady=5, sticky="we")

        self.btnBuscar = tk.Button(self.frame_principal, text="Buscar", command=self.buscar_cidade, width=10)
        self.btnBuscar.grid(row=0, column=3, padx=5, pady=5)

        self.lblNome = tk.Label(self.frame_principal, text="Nome:")
        self.lblNome.grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.txtNome = tk.Entry(self.frame_principal, width=30)
        self.txtNome.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky="we")

        self.lblEstado = tk.Label(self.frame_principal, text="Estado:")
        self.lblEstado.grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.txtEstado = tk.Entry(self.frame_principal, width=30)
        self.txtEstado.grid(row=2, column=1, columnspan=3, padx=5, pady=5, sticky="we")

        # Frame para os botões
        self.frame_botoes = tk.Frame(root)
        self.frame_botoes.grid(row=1, column=1, pady=10)

        self.btnInserir = tk.Button(self.frame_botoes, text="Inserir", command=self.inserir_cidade, width=10)
        self.btnInserir.grid(row=0, column=0, padx=10, pady=5)

        self.btnAlterar = tk.Button(self.frame_botoes, text="Alterar", command=self.alterar_cidade, width=10)
        self.btnAlterar.grid(row=0, column=1, padx=10, pady=5)

        self.btnExcluir = tk.Button(self.frame_botoes, text="Excluir", command=self.excluir_cidade, width=10)
        self.btnExcluir.grid(row=0, column=2, padx=10, pady=5)

        self.lblMensagem = tk.Label(root, text="", fg="green")
        self.lblMensagem.grid(row=2, column=1, padx=20, pady=10, sticky="we")

        # Adicionando o Treeview para exibir as cidades
        self.tree = ttk.Treeview(root, columns=('ID', 'Nome', 'Estado'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Nome', text='Nome')
        self.tree.heading('Estado', text='Estado')
        self.tree.column('ID', width=50)
        self.tree.column('Nome', width=200)
        self.tree.column('Estado', width=100)
        self.tree.grid(row=3, column=1, padx=20, pady=10, sticky="nsew")

        # Preenchendo o Treeview com as cidades
        self.carregar_cidades()

    def carregar_cidades(self):
        # Limpa o Treeview
        for row in self.tree.get_children():
            self.tree.delete(row)
        
        # Busca as cidades no banco de dados
        cidades = self.cidade.buscar_todos()
        for cidade in cidades:
            self.tree.insert('', tk.END, values=cidade)

    def buscar_cidade(self):
        idCidade = self.txtIdCidade.get()
        resultado = self.cidade.buscar(idCidade)
        if resultado:
            self.txtNome.delete(0, tk.END)
            self.txtNome.insert(tk.END, resultado[1])
            self.txtEstado.delete(0, tk.END)
            self.txtEstado.insert(tk.END, resultado[2])
            self.lblMensagem.config(text="Busca realizada com sucesso!", fg="green")
        else:
            self.lblMensagem.config(text="Cidade não encontrada!", fg="red")

    def inserir_cidade(self):
        nome = self.txtNome.get()
        estado = self.txtEstado.get()
        self.cidade.inserir(nome, estado)
        self.lblMensagem.config(text="Cidade inserida com sucesso!", fg="green")
        self.limpar_campos()
        self.carregar_cidades()  # Atualiza o Treeview

    def alterar_cidade(self):
        idCidade = self.txtIdCidade.get()
        nome = self.txtNome.get()
        estado = self.txtEstado.get()
        self.cidade.alterar(idCidade, nome, estado)
        self.lblMensagem.config(text="Cidade alterada com sucesso!", fg="green")
        self.carregar_cidades()  # Atualiza o Treeview

    def excluir_cidade(self):
        idCidade = self.txtIdCidade.get()
        self.cidade.excluir(idCidade)
        self.lblMensagem.config(text="Cidade excluída com sucesso!", fg="green")
        self.limpar_campos()
        self.carregar_cidades()  # Atualiza o Treeview

    def limpar_campos(self):
        self.txtIdCidade.delete(0, tk.END)
        self.txtNome.delete(0, tk.END)
        self.txtEstado.delete(0, tk.END)

# Execução da interface
if __name__ == "__main__":
    root = tk.Tk()
    root.state("zoomed")
    app = TelaCidades(root)
    root.mainloop()
