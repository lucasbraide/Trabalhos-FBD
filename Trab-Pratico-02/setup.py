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

# Exclui todas as tabelas
cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
tables = cursor.fetchall()

for table in tables:
    table_name = table[0]
    truncate_query = sql.SQL("TRUNCATE TABLE {} RESTART IDENTITY CASCADE").format(sql.Identifier(table_name))
    drop_query = sql.SQL("DROP TABLE IF EXISTS {} CASCADE").format(sql.Identifier(table_name))
    cursor.execute(truncate_query)
    cursor.execute(drop_query)

print("Setup executado com sucesso.")
conn.commit()
cursor.close()
conn.close()