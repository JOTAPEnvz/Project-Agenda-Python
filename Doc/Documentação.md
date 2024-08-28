### Documentação da Aplicação Tkinter com Banco de Dados SQLite

---

## Sumário

1. [Introdução](#introdução)
2. [Estrutura do Projeto](#estrutura-do-projeto)
3. [Descrição das Classes](#descrição-das-classes)
   - [Classe `Main`](#classe-main)
   - [Classe `Banco`](#classe-banco)
   - [Classe `Usuario`](#classe-usuario)
   - [Classe `Application`](#classe-application)
4. [Funcionalidades](#funcionalidades)
5. [Como Executar a Aplicação](#como-executar-a-aplicação)
6. [Considerações Finais](#considerações-finais)

---

## Introdução

Esta documentação descreve o funcionamento de uma aplicação em Python que utiliza o Tkinter para a interface gráfica e o SQLite para persistência de dados. A aplicação permite gerenciar um cadastro de usuários, oferecendo operações básicas como inserção, alteração, exclusão e busca.

---

## Estrutura do Projeto

A estrutura básica do projeto é composta pelos seguintes arquivos:

- **app.py**: Contém a classe `Application`, que define a interface gráfica para o cadastro de usuários.
- **main.py**: Contém a classe `Main`, que inicializa a aplicação e configura os botões principais.
- **banco.py**: Define a classe `Banco`, que gerencia a conexão com o banco de dados SQLite.
- **usuarios_model.py**: Define a classe `Usuario`, que manipula as operações CRUD (Create, Read, Update, Delete) no banco de dados.

---

## Descrição das Classes

### Classe `Main`

- **Função:** Esta classe é responsável por criar a janela principal da aplicação e exibir os botões de navegação ("Usuário", "Cidades", "Clientes" e "Sair").
- **Métodos Principais:**
  - `__init__(self, root, master=None)`: Inicializa os botões e configura a interface principal.
  - `abrir_tela_usuario(self)`: Fecha a janela principal e abre a tela de cadastro de usuários, criando uma nova instância da classe `Application`.

### Classe `Banco`

- **Função:** Gerencia a conexão com o banco de dados SQLite e a criação da tabela `usuarios`.
- **Métodos Principais:**
  - `__init__(self)`: Estabelece a conexão com o banco de dados e chama o método `criar_tabela`.
  - `criar_tabela(self)`: Cria a tabela `usuarios` no banco de dados, caso ela ainda não exista.
  - `fechar_conexao(self)`: Fecha a conexão com o banco de dados.

### Classe `Usuario`

- **Função:** Realiza as operações CRUD na tabela `usuarios` do banco de dados.
- **Métodos Principais:**
  - `inserir(self, nome, telefone, email, usuario, senha)`: Insere um novo registro na tabela `usuarios`.
  - `alterar(self, idUsuario, nome, telefone, email, usuario, senha)`: Altera um registro existente na tabela `usuarios`.
  - `excluir(self, idUsuario)`: Exclui um registro da tabela `usuarios`.
  - `buscar(self, idUsuario)`: Busca um registro na tabela `usuarios` pelo `idUsuario`.

### Classe `Application`

- **Função:** Define a interface gráfica para o cadastro de usuários e gerencia a interação do usuário com o banco de dados.
- **Componentes da Interface:**
  - **Labels e Entradas:** Campos para entrada de dados do usuário (Nome, Telefone, Email, Usuário, Senha).
  - **Botões:** Botões para realizar as operações de inserir, alterar, excluir e buscar usuários.
  - **Mensagem de Status:** Label que exibe mensagens de sucesso ou erro ao realizar operações.
- **Métodos Principais:**
  - `buscar_usuario(self)`: Busca um usuário pelo ID e exibe os dados nos campos correspondentes.
  - `inserir_usuario(self)`: Insere um novo usuário no banco de dados com os dados fornecidos nos campos.
  - `alterar_usuario(self)`: Altera os dados de um usuário existente.
  - `excluir_usuario(self)`: Exclui um usuário do banco de dados.
  - `limpar_campos(self)`: Limpa os campos de entrada após a realização de uma operação.

---

## Funcionalidades

A aplicação oferece as seguintes funcionalidades:

1. **Inserir Usuário:** Permite adicionar um novo usuário ao banco de dados.
2. **Buscar Usuário:** Busca um usuário pelo ID e exibe seus dados.
3. **Alterar Usuário:** Altera os dados de um usuário existente no banco.
4. **Excluir Usuário:** Remove um usuário do banco de dados.

---

## Como Executar a Aplicação

1. **Pré-requisitos:** Certifique-se de ter o Python instalado em sua máquina.
2. **Instalação:** Clone ou baixe os arquivos do projeto.
3. **Execução:** No terminal, navegue até o diretório do projeto e execute o comando:

   ```
   python main.py
   ```

4. **Uso:** A interface principal exibirá quatro botões. Clique em "Usuário" para acessar a tela de cadastro de usuários.

---

## Considerações Finais

Este projeto é um exemplo simples de como integrar uma interface gráfica com um banco de dados SQLite usando Python. Ele pode ser facilmente expandido para incluir mais funcionalidades ou usar uma arquitetura mais robusta para aplicações maiores.