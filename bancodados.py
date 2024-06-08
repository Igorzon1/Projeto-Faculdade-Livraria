import sqlite3

conn = sqlite3.connect("biblioteca.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Pessoa (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT,
    Data_nascimento DATE,
    Idade INTEGER,
    CPF TEXT,
    Email TEXT,
    Senha TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Administracao (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Cargo TEXT,
    Nome_Funcionario TEXT,
    CPF TEXT,
    Email TEXT,
    Senha TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Pedido (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Valor REAL,
    Data DATE,
    Itens_Pedido INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Itens_Pedido (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome_livro TEXT,
    Quantidade INTEGER,
    Pedido_Id INTEGER,
    FOREIGN KEY (Pedido_Id) REFERENCES Pedido(Id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Livro_fisico (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome_livro TEXT,
    Tema TEXT,
    Editora TEXT ,
    Distribuidora TEXT,
    Autor TEXT,
    Estoque INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Livro_digital (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome_livro TEXT,
    Tema TEXT,
    Editora TEXT,
    Autor TEXT
)
""")

conn.commit()
conn.close()