import psycopg2
from psycopg2 import sql
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do banco e as atribui adequadamente
load_dotenv()

DB_HOST = os.getenv('DB_HOST')
print(DB_HOST)
DB_NAME = os.getenv('DB_NAME')
print(DB_NAME)
DB_USER = os.getenv('DB_USER')
print(DB_USER)
DB_PASS = os.getenv('DB_PASS')
print(DB_PASS)

# Conecta ao banco e cursor 
conn = psycopg2.connect(host = DB_HOST, database = DB_NAME, user = DB_USER, password = DB_PASS)

cursor = conn.cursor()

queries = ["CREATE TABLE IF NOT EXISTS Embarcacoes (id_emb SERIAL PRIMARY KEY, nome VARCHAR, tipo VARCHAR)", 
           "CREATE TABLE IF NOT EXISTS Tripulantes (id_trp SERIAL PRIMARY KEY, nome VARCHAR, data_nasc DATE, funcao VARCHAR, id_emb INT REFERENCES Embarcacoes(id_emb))",
           "CREATE TABLE IF NOT EXISTS Empregados (id_emp SERIAL PRIMARY KEY, nome VARCHAR, data_nasc DATE, funcao VARCHAR)",
           "CREATE TABLE IF NOT EXISTS Movimentacao (id_mov SERIAL PRIMARY KEY, data TIMESTAMP, tipo VARCHAR, id_emb INT REFERENCES Embarcacoes(id_emb))",
           "CREATE TABLE IF NOT EXISTS Movimentacao_Empregados (id_mov INT REFERENCES Movimentacao(id_mov), id_emp INT REFERENCES Empregados(id_emp), PRIMARY KEY (id_mov, id_emp))" ]

for query in queries:
    cursor.execute(query)
    print("Comando executado com sucesso: %s", query)

conn.commit()
cursor.close()
conn.close()