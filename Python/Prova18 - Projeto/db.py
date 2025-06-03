import sqlite3
from classes import Produto, Venda
from datetime import datetime

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

def remover_produto_db(id_produto):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Produtos WHERE ID = ?", (id_produto,))
        conn.commit()

def buscar_produto_por_id(id_produto):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Produtos WHERE ID = ?", (id_produto,))
        resultado = cursor.fetchone()
        return Produto(*resultado) if resultado else None

def registrar_venda(id_produto, quantidade):
    with conectar() as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT quantidade FROM Produtos WHERE ID = ?", (id_produto,))
        resultado = cursor.fetchone()

        if not resultado:
            return False, "Produto não encontrado."
        
        estoque_atual = resultado[0]
        if estoque_atual < quantidade:
            return False, "Estoque insuficiente para realizar a venda."

        cursor.execute("""
            UPDATE Produtos SET quantidade = quantidade - ? WHERE ID = ?
        """, (quantidade, id_produto))

        data_venda = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute("""
            INSERT INTO Vendas (ID_Produto, quantidade_vendida, Data_venda)
            VALUES (?, ?, ?)
        """, (id_produto, quantidade, data_venda))

        conn.commit()
        return True, "Venda registrada com sucesso."

def listar_vendas():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Vendas ORDER BY Data_venda DESC")
        return [Venda(*linha) for linha in cursor.fetchall()]
