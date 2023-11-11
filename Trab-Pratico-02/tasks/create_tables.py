import psycopg2
from psycopg2 import sql

def create_tables(conn):
    cursor = conn.cursor()
    queries = ["CREATE TABLE IF NOT EXISTS Embarcacoes (id_emb SERIAL PRIMARY KEY, nome VARCHAR, tipo VARCHAR)", 
                "CREATE TABLE IF NOT EXISTS Tripulantes (id_trp SERIAL PRIMARY KEY, nome VARCHAR, data_nasc DATE, funcao VARCHAR, id_emb INT REFERENCES Embarcacoes(id_emb))",
                "CREATE TABLE IF NOT EXISTS Empregados (id_emp SERIAL PRIMARY KEY, nome VARCHAR, data_nasc DATE, funcao VARCHAR)",
                "CREATE TABLE IF NOT EXISTS Movimentacoes (id_mov SERIAL PRIMARY KEY, data DATE, tipo VARCHAR, id_emb INT REFERENCES Embarcacoes(id_emb))",
                "CREATE TABLE IF NOT EXISTS Movimentacoes_Empregados (id_mov INT REFERENCES Movimentacoes(id_mov), id_emp INT REFERENCES Empregados(id_emp), PRIMARY KEY (id_mov, id_emp))" ]

    for query in queries:
        cursor.execute(query)
        print("Comando executado com sucesso: %s", query)

    conn.commit()
    cursor.close()