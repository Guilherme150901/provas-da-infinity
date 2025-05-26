import sqlite3
from classes import Produto

def conectar():
    return sqlite3.connect("vendas.db")

def criar_tabelas():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Produtos (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                descricao TEXT,
                quantidade INTEGER,
                preco DECIMAL(9,2) CHECK (preco > 0)
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Vendas (
                ID_venda INTEGER PRIMARY KEY AUTOINCREMENT,
                ID_Produto INTEGER,
                quantidade_vendida INTEGER NOT NULL,
                Data_venda DATETIME,
                FOREIGN KEY (ID_Produto) REFERENCES Produtos(ID)
            );
        """)

def inserir_produto(produto):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Produtos (nome, descricao, quantidade, preco)
            VALUES (?, ?, ?, ?)
        """, (produto.nome, produto.descricao, produto.quantidade, produto.preco))
        conn.commit()

def listar_produtos():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Produtos")
        return [Produto(*linha) for linha in cursor.fetchall()]

def atualizar_quantidade(id_produto, quantidade):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Produtos
            SET quantidade = quantidade + ?
            WHERE ID = ?
        """, (quantidade, id_produto))
        conn.commit()

def remover_produto(id_produto):
    with conectar() as conn:
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM Produtos WHERE ID = ?", (id_produto,))
        conn.commit()
