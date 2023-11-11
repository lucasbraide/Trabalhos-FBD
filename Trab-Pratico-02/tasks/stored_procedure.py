import psycopg2
from psycopg2 import sql
import db_config

conn = db_config.db_conn()
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