Trabalho Faculdade

Feito em Flet

Funções :

Sistema de cadastro de livros;
Classe Pessoa(nome,data de nascimento,idade, cpf);
Criar objetos para a Biblioteca(POO);
Sistema de cadastro de Pessoa;-Validar CPF;-Gerar a idade;
Interface para usario na web;-Janela login (validar o usuário);-Dependo do usario entrar na administração;-Site responsivo;

Banco de dados:

Class Pessoa
 
Id (PK)
Nome
Data_nascimento
idade
CPF
Email
senha

Class Administração
 
Id(PK)
cargo
Nome_Funcionário
CPF
Email
Senha

Class Pedido
 
Id(PK)
valor
Data
Itens_Pedido(FK)

Class Itens_Pedido
 
Id(FK)
Nome_livro
Quantidade

Class Livro
 
id (PK)
Livro_fisico
Livro_digital

Class Livro_fisico
 
id(FK)
Nome_livro
Tema
Editora
distribuidora
Autor
Estoque

Class Livro_digital
 
id(FK)
Nome_livro
Tema
Editora
Autor
