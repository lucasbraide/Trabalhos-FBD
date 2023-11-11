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

try:
    # Criação do Stored Procedure empregado do mes que recebe como
    # parâmetro uma data e retorna o id e nome do empregado que participou de mais movimentações naquela
    # combinação Ano/Mês;
    cursor.execute("""CREATE OR REPLACE PROCEDURE empregado_do_mes (date DATE)
                        LANGUAGE SQL AS $$
                        SELECT E.id_emp, E.nome FROM (CELITO COMPLETA)""")

    # Chama o Stored Procedure
    cursor.callproc("empregado_do_mes", ("2023-10-01"))
    empregado_do_mes = cursor.fetchall()

    # Printa o Stored Procedure
    print(empregado_do_mes)
    cursor.close()

except psycopg2.DatabaseError as error:
    print(error)
finally:
    if conn is not None:
        conn.close()