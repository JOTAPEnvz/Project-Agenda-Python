import os
import tkinter as tk
from tkinter import Frame
from app import Application

class Main:
    def __init__(self, root, master=None):
        self.root = root
        self.frame_botoes = tk.Frame(root)
        self.frame_botoes.grid(row=1, column=1, pady=10)

        self.font = ('Arial', 20)

        self.btnUsuario = tk.Button(self.frame_botoes, text="Usuário", width=20, height=5, font=self.font, command=self.abrir_tela_usuario)
        self.btnUsuario.grid(row=0, column=0, padx=10, pady=5)
        self.btnCidades = tk.Button(self.frame_botoes, text="Cidades", width=20, height=5, font=self.font)
        self.btnCidades.grid(row=0, column=1, padx=10, pady=5)
        self.btnClientes = tk.Button(self.frame_botoes, text="Clientes", width=20, height=5, font=self.font)
        self.btnClientes.grid(row=0, column=2, padx=10, pady=5)
        self.btnSair = tk.Button(self.frame_botoes, text="Sair", width=20, height=5, font=self.font, command=self.root.quit)
        self.btnSair.grid(row=0, column=3, padx=10, pady=5)

    def abrir_tela_usuario(self):
        self.root.destroy()
        os.system("python app.py")

if __name__ == "__main__":
    root = tk.Tk()
    root.state("zoomed")  
    app = Main(root)
    root.mainloop()
