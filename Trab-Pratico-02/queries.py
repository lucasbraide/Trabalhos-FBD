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

# 1- Retorne todas as embarcações e o número de tripulantes de cada embarcação.
cursor.execute("SELECT E.nome AS nome_embarcacao, COUNT(T.id_trp) as numero_tripulantes FROM Embarcacoes E JOIN Tripulantes T ON E.id_emb = T.id_emb GROUP BY E.nome")

tripulantes_embarcacao = cursor.fetchall()

print("1- Retorne todas as embarcações e o número de tripulantes de cada embarcação.")
for item in tripulantes_embarcacao:
    print(item)

cursor.close()
conn.close()