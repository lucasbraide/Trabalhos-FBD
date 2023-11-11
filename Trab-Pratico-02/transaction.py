import psycopg2
from psycopg2 import sql
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do banco e as atribui adequadamente
load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')

# Conecta ao banco e cursor 
conn = psycopg2.connect(host = DB_HOST, database = DB_NAME, user = DB_USER, password = DB_PASS)

cursor = conn.cursor()

# Tenta executar tudo numa transação
try:
    # 1. Inserir nova Movimentação
    cursor.execute("INSERT INTO Movimentacoes (id_mov, data, tipo, id_emb) VALUES (%s, %s, %s, %s)", 
                   (6, '2023-10-05', 'Manutenção', 1))


    # 2. Inserir nova Movimentação-Empregado (relacionamento)
    cursor.execute("INSERT INTO Movimentacoes_Empregados (id_mov, id_emp) VALUES (%s, %s)", (6, 1))

    # 3. Realizar consulta quantidade de movimentações que envolvem embarcações do tipo “Cargueiro”.
    cursor.execute("SELECT COUNT(*) AS qtd_mov_cargueiro FROM Movimentacoes M JOIN Embarcacoes E ON M.id_emb = E.id_emb WHERE E.tipo = 'Cargueiro'")

    qtd_cargueiro = cursor.fetchall()
    print("Quantidade de movimentacoes em navios_cargueiros:", qtd_cargueiro)

    # Commit na Transação
    conn.commit()

    cursor.close()

# Caso algum erro ocorra, não executa e printa o erro
except psycopg2.DatabaseError as error:
    print(error)
finally:
    if conn is not None:
        conn.close()

